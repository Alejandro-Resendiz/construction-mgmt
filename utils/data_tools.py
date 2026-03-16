import pandas as pd
import numpy as np
import re

def clean_currency(value):
    """
    Parses currency strings like '$1,234.56' or '1234.56' into floats.
    Handles Excel error strings by returning NaN.
    """
    if pd.isna(value) or str(value).startswith('#'):
        return np.nan
    if isinstance(value, (int, float)):
        return float(value)
    
    # Remove '$', ',', and whitespace
    clean_str = re.sub(r'[\$,\s]', '', str(value))
    try:
        return float(clean_str)
    except ValueError:
        return np.nan

def clean_percent(value):
    """
    Parses percentage strings like '25.00%' or '0.25' into floats (0.25).
    """
    if pd.isna(value) or str(value).startswith('#'):
        return np.nan
    if isinstance(value, (int, float)):
        return float(value)
    
    clean_str = str(value).strip()
    if clean_str.endswith('%'):
        try:
            return float(clean_str.replace('%', '')) / 100.0
        except ValueError:
            return np.nan
    try:
        return float(clean_str)
    except ValueError:
        return np.nan
