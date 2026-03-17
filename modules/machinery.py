import pandas as pd
import numpy as np
from utils.i18n import get_column_map, translate

REQUIRED_INPUT_KEYS = [
    'id', 'machinery', 'lifespan_years', 'purchase_value', 'rescue_value_percent',
    'diesel_consumption_in_liters', 'diesel_price',
    'operator_wage', 'maintenance_cost', 'worked_hours', 'utility_percent'
]

def load_and_map_data(file_obj, lang='en'):
    """
    Loads CSV, validates headers (en or es), and maps to internal keys.
    Normalization: Lowercase and strip whitespace for matching.
    """
    df = pd.read_csv(file_obj)
    
    # Get maps for both languages
    en_map = get_column_map('en', module='machinery')
    es_map = get_column_map('es', module='machinery')
    
    # Create normalized reverse maps: lowercase(Display Name) -> Internal Key
    rev_en = {v.lower().strip(): k for k, v in en_map.items()}
    rev_es = {v.lower().strip(): k for k, v in es_map.items()}
    
    actual_cols = df.columns.tolist()
    
    final_mapping = {}
    for col in actual_cols:
        col_norm = str(col).lower().strip()
        if col_norm in rev_en:
            final_mapping[col] = rev_en[col_norm]
        elif col_norm in rev_es:
            final_mapping[col] = rev_es[col_norm]
            
    df = df.rename(columns=final_mapping)
    
    # Check if all required keys are now in the dataframe
    missing_keys = [k for k in REQUIRED_INPUT_KEYS if k not in df.columns]
    if missing_keys:
        # Use translated names for the error message
        translated_missing = [translate(f'col_{k}', lang) for k in missing_keys]
        raise ValueError(translate('missing_cols_error', lang, cols=", ".join(translated_missing)))
        
    return df[REQUIRED_INPUT_KEYS]

def validate_data(df, lang='en'):
    """
    Strictly validates that all columns (except id and machinery) are numeric.
    Returns list of error messages.
    """
    errors = []
    numeric_cols = [k for k in REQUIRED_INPUT_KEYS if k not in ['id', 'machinery']]
    
    for col in numeric_cols:
        if not pd.api.types.is_numeric_dtype(df[col]):
            non_numeric_mask = pd.to_numeric(df[col], errors='coerce').isna()
            if non_numeric_mask.any():
                bad_rows = np.where(non_numeric_mask)[0] + 2
                errors.append(translate('non_numeric_error', lang, col=translate(f'col_{col}', lang), rows=", ".join(map(str, bad_rows))))
    
    return errors

DEFAULT_WORKING_HOURS = 2112

def calculate_costs(df, working_hours_per_year=DEFAULT_WORKING_HOURS):
    """
    Performs calculations based on internal snake_case keys.
    """
    numeric_cols = [k for k in REQUIRED_INPUT_KEYS if k not in ['id', 'machinery']]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['rescue_value'] = df['purchase_value'] * df['rescue_value_percent']
    
    df['fuel_cost_per_hour'] = np.where(
        df['worked_hours'] > 0,
        df['diesel_consumption_in_liters'] * df['diesel_price'] / df['worked_hours'],
        0.0
    )
    
    df['operator_cost_per_hour'] = np.where(
        df['worked_hours'] > 0,
        df['operator_wage'] / df['worked_hours'],
        0.0
    )
    
    df['maintenance_cost_per_hour'] = np.where(
        df['worked_hours'] > 0,
        df['maintenance_cost'] / df['worked_hours'],
        0.0
    )
    
    df['depreciation_cost_per_hour'] = np.where(
        df['lifespan_years'] > 0,
        (df['purchase_value'] - df['rescue_value'].fillna(0)) / df['lifespan_years'] / working_hours_per_year,
        0.0
    )
    
    df['total_cost_per_hour'] = (
        df['fuel_cost_per_hour'] + 
        df['operator_cost_per_hour'] + 
        df['maintenance_cost_per_hour'] + 
        df['depreciation_cost_per_hour']
    )
    
    df['rent_rate_per_hour'] = df['total_cost_per_hour'] * (1 + df['utility_percent'].fillna(0))
    
    return df
