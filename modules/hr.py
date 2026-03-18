import pandas as pd
import numpy as np
from utils.i18n import get_column_map, translate
from tests.data_contracts import HR_SCHEMA

REQUIRED_INPUT_KEYS = list(HR_SCHEMA.keys())

def load_and_map_data(file_obj, lang='en'):
    """
    Loads CSV, validates headers (en or es), and maps to internal keys.
    """
    df = pd.read_csv(file_obj)
    
    en_map = get_column_map('en', module='hr')
    es_map = get_column_map('es', module='hr')
    
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
    
    missing_keys = [k for k in REQUIRED_INPUT_KEYS if k not in df.columns]
    if missing_keys:
        translated_missing = [translate(f'col_{k}', lang) for k in missing_keys]
        raise ValueError(translate('missing_cols_error', lang, cols=", ".join(translated_missing)))
        
    return df[REQUIRED_INPUT_KEYS]

def validate_data(df, lang='en'):
    """
    Validates categorical and date data for HR pipeline.
    """
    errors = []
    # Check date formats
    date_cols = ['application_date', 'offer_date', 'start_date']
    for col in date_cols:
        # Fill N/A with NaT or handle them
        # We don't clean, but we check if they are parsable when not 'N/A'
        valid_dates = df[col].astype(str).str.upper().replace('N/A', np.nan)
        try:
            pd.to_datetime(valid_dates, errors='raise', format='%d/%m/%Y')
        except Exception:
            errors.append(translate('error_processing', lang, error=f"Invalid date format in {translate(f'col_{col}', lang)}. Expected DD/MM/YYYY"))
            
    return errors

def calculate_hr(df):
    """
    Performs calculations based on hierarchical logic.
    """
    # 1. current_stage
    def get_stage(row):
        if str(row['offer']).strip() == 'Aceptada': return 'Ingreso'
        if str(row['references']).strip() == 'Aprobado': return 'Oferta'
        if str(row['technical_interview']).strip() == 'Aprobado': return 'Referencias'
        if str(row['hr_filter']).strip() == 'Aprobado': return 'Entrevista'
        if str(row['screening']).strip() == 'Aprobado': return 'Filtro_HR'
        return 'Screening'

    df['current_stage'] = df.apply(get_stage, axis=1)

    # 2. final_status
    def get_status(row):
        rejected_vals = ['No aprobado', 'Negativas', 'Rechazada']
        if (str(row['screening']) == 'No aprobado' or 
            str(row['hr_filter']) == 'No aprobado' or 
            str(row['technical_interview']) == 'No aprobado' or 
            str(row['references']) == 'Negativas' or 
            str(row['offer']) == 'Rechazada'):
            return 'Rechazado'
        if str(row['offer']) == 'Aceptada':
            return 'Contratado'
        return 'Proceso activo'

    df['final_status'] = df.apply(get_status, axis=1)

    # 3. time_to_hire
    # Convert to datetime for calculation
    app_date = pd.to_datetime(df['application_date'], errors='coerce', format='%d/%m/%Y')
    start_date = pd.to_datetime(df['start_date'], errors='coerce', format='%d/%m/%Y')
    
    df['time_to_hire'] = (start_date - app_date).dt.days
    
    return df
