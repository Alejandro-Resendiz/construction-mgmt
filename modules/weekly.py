import pandas as pd
import numpy as np
from utils.i18n import get_column_map, translate

REQUIRED_INPUT_KEYS = [
    'machine', 'machine_model', 'machine_serial_number', 'project_name',
    'operator_name', 'activity_name', 'worked_hours_forecasted',
    'worked_hours_registered', 'fuel_average_usage', 'liters_real_consumption'
]

def load_and_map_data(file_obj, lang='en'):
    """
    Loads CSV, validates headers (en or es), and maps to internal keys.
    """
    df = pd.read_csv(file_obj)
    
    en_map = get_column_map('en', module='weekly')
    es_map = get_column_map('es', module='weekly')
    
    # Create case-insensitive reverse maps
    rev_en = {v.lower(): k for k, v in en_map.items()}
    rev_es = {v.lower(): k for k, v in es_map.items()}
    
    actual_cols = df.columns.tolist()
    
    final_mapping = {}
    for col in actual_cols:
        col_lower = str(col).lower().strip()
        if col_lower in rev_en:
            final_mapping[col] = rev_en[col_lower]
        elif col_lower in rev_es:
            final_mapping[col] = rev_es[col_lower]
            
    df = df.rename(columns=final_mapping)
    
    missing_keys = [k for k in REQUIRED_INPUT_KEYS if k not in df.columns]
    if missing_keys:
        translated_missing = [translate(f'col_{k}', lang) for k in missing_keys]
        raise ValueError(translate('missing_cols_error', lang, cols=", ".join(translated_missing)))
        
    return df[REQUIRED_INPUT_KEYS]

def validate_data(df, lang='en'):
    """
    Validates that all numeric columns are numeric.
    """
    errors = []
    numeric_cols = [
        'worked_hours_forecasted', 'worked_hours_registered', 
        'fuel_average_usage', 'liters_real_consumption'
    ]
    
    for col in numeric_cols:
        if not pd.api.types.is_numeric_dtype(df[col]):
            non_numeric_mask = pd.to_numeric(df[col], errors='coerce').isna()
            if non_numeric_mask.any():
                bad_rows = np.where(non_numeric_mask)[0] + 2
                errors.append(translate('non_numeric_error', lang, col=translate(f'col_{col}', lang), rows=", ".join(map(str, bad_rows))))
    
    return errors

def calculate_weekly(df):
    """
    Performs calculations based on defined formulas.
    """
    # Ensure numeric
    numeric_cols = [
        'worked_hours_forecasted', 'worked_hours_registered', 
        'fuel_average_usage', 'liters_real_consumption'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # 1. liters_forecasted = fuel_average_usage * worked_hours_forecasted
    df['liters_forecasted'] = df['fuel_average_usage'] * df['worked_hours_forecasted']
    
    # 2. hours_variation = worked_hours_registered / worked_hours_forecasted
    df['hours_variation'] = np.where(
        df['worked_hours_forecasted'] > 0,
        df['worked_hours_registered'] / df['worked_hours_forecasted'],
        1.0
    )
    
    # 3. liters_variation = liters_real_consumption / liters_forecasted
    df['liters_variation'] = np.where(
        df['liters_forecasted'] > 0,
        df['liters_real_consumption'] / df['liters_forecasted'],
        1.0
    )
    
    # 4. liters_real_per_hour = liters_real_consumption / worked_hours_registered
    df['liters_real_per_hour'] = np.where(
        df['worked_hours_registered'] > 0,
        df['liters_real_consumption'] / df['worked_hours_registered'],
        0.0
    )
    
    return df
