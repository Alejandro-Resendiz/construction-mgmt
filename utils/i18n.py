from utils.config import APP_NAME

translations = {
    'en': {
        'title': f"{APP_NAME} Management System",
        'select_module': "Select Module",
        'machinery_cost': "Machinery Cost",
        'future_module': "Future Module...",
        'upload_title': "🚜 Machinery Cost Calculation",
        'upload_desc': "Upload the machinery cost CSV file. Requirements: Pure numeric values (e.g., 0.2 for 20%), no currency symbols.",
        'choose_file': "Choose a CSV file",
        'validation': "1. Data Validation & Cleaning",
        'missing_cols_error': "Missing required columns: {cols}",
        'non_numeric_error': "Column '{col}' contains non-numeric values at rows: {rows}",
        'success_data': "All data is valid and numeric.",
        'settings': "Settings",
        'working_hours': "Working Hours per Year",
        'calc_button': "Calculate Costs",
        'results': "2. Calculated Results",
        'dashboard': "3. Fleet Dashboard",
        'kpi_investment': "Total Fleet Investment",
        'kpi_rent': "Avg. Rent Rate / Hour",
        'kpi_count': "Active Machinery Count",
        'chart_breakdown': "Cost Breakdown per Machine",
        'chart_rent_vs_cost': "Rent Rate vs. Total Cost",
        'export': "4. Export Results",
        'download_button': "Download Calculations as CSV",
        'error_processing': "Error processing file: {error}",
        # Internal keys to display names
        'col_id': "ID",
        'col_machinery': "Machinery",
        'col_lifespan_years': "Lifespan (Years)",
        'col_purchase_value': "Purchase Value",
        'col_rescue_value_percent': "Rescue Value (%)",
        'col_depreciation_estimated_per_hour': "Estimated Depreciation ($/h)",
        'col_diesel_consumption_in_liters': "Diesel Consumption (L)",
        'col_diesel_price': "Diesel Price",
        'col_operator_wage': "Operator Wage",
        'col_maintenance_cost': "Maintenance Cost",
        'col_worked_hours': "Worked Hours",
        'col_utility_percent': "Utility (%)",
        'col_rescue_value': "Rescue Value",
        'col_fuel_cost_per_hour': "Fuel Cost ($/h)",
        'col_operator_cost_per_hour': "Operator Cost ($/h)",
        'col_maintenance_cost_per_hour': "Maintenance Cost ($/h)",
        'col_depreciation_cost_per_hour': "Depreciation Cost ($/h)",
        'col_total_cost_per_hour': "Total Cost ($/h)",
        'col_rent_rate_per_hour': "Rent Rate ($/h)",
        # Components
        'fuel': "Fuel",
        'operator': "Operator",
        'maintenance': "Maintenance",
        'depreciation': "Depreciation",
        'cost_component': "Cost Component"
    },
    'es': {
        'title': f"Sistema de Gestión {APP_NAME}",
        'select_module': "Seleccionar Módulo",
        'machinery_cost': "Costo de Maquinaria",
        'future_module': "Próximo Módulo...",
        'upload_title': "🚜 Cálculo de Costos de Maquinaria",
        'upload_desc': "Cargue el archivo CSV. Requisitos: Valores numéricos puros (ej. 0.2 para 20%), sin símbolos de moneda.",
        'choose_file': "Seleccione un archivo CSV",
        'validation': "1. Validación y Limpieza de Datos",
        'missing_cols_error': "Faltan columnas requeridas: {cols}",
        'non_numeric_error': "La columna '{col}' contiene valores no numéricos en las filas: {rows}",
        'success_data': "Todos los datos son válidos y numéricos.",
        'settings': "Configuración",
        'working_hours': "Horas de Trabajo por Año",
        'calc_button': "Calcular Costos",
        'results': "2. Resultados Calculados",
        'dashboard': "3. Panel de Control de la Flota",
        'kpi_investment': "Inversión Total de la Flota",
        'kpi_rent': "Tarifa de Renta Promedio / Hora",
        'kpi_count': "Cantidad de Maquinaria Activa",
        'chart_breakdown': "Desglose de Costos por Máquina",
        'chart_rent_vs_cost': "Tarifa de Renta vs. Costo Total",
        'export': "4. Exportar Resultados",
        'download_button': "Descargar Cálculos como CSV",
        'error_processing': "Error al procesar el archivo: {error}",
        # Internal keys to display names
        'col_id': "Código",
        'col_machinery': "Maquinaria",
        'col_lifespan_years': "Vida Útil (Años)",
        'col_purchase_value': "Valor de Compra",
        'col_rescue_value_percent': "Valor de Rescate (%)",
        'col_depreciation_estimated_per_hour': "Depreciación Estimada ($/h)",
        'col_diesel_consumption_in_liters': "Consumo de Diésel (L)",
        'col_diesel_price': "Precio de Diésel",
        'col_operator_wage': "Sueldo por Operador",
        'col_maintenance_cost': "Costo de Mantenimiento",
        'col_worked_hours': "Horas Trabajadas",
        'col_utility_percent': "Utilidad (%)",
        'col_rescue_value': "Valor de Rescate",
        'col_fuel_cost_per_hour': "Costo Combustible ($/h)",
        'col_operator_cost_per_hour': "Costo Operador ($/h)",
        'col_maintenance_cost_per_hour': "Costo Mantenimiento ($/h)",
        'col_depreciation_cost_per_hour': "Costo Depreciación ($/h)",
        'col_total_cost_per_hour': "Costo Total por Hora",
        'col_rent_rate_per_hour': "Tarifa Renta por Hora",
        # Components
        'fuel': "Combustible",
        'operator': "Operador",
        'maintenance': "Mantenimiento",
        'depreciation': "Depreciación",
        'cost_component': "Componente de Costo"
    }
}

def translate(key, lang='en', **kwargs):
    text = translations.get(lang, translations['en']).get(key, key)
    if kwargs:
        return text.format(**kwargs)
    return text

def get_column_map(lang='en'):
    """Returns a map of internal keys to translated display names."""
    keys = [
        'id', 'machinery', 'lifespan_years', 'purchase_value', 'rescue_value_percent',
        'depreciation_estimated_per_hour', 'diesel_consumption_in_liters', 'diesel_price',
        'operator_wage', 'maintenance_cost', 'worked_hours', 'utility_percent',
        'rescue_value', 'fuel_cost_per_hour', 'operator_cost_per_hour', 
        'maintenance_cost_per_hour', 'depreciation_cost_per_hour', 
        'total_cost_per_hour', 'rent_rate_per_hour'
    ]
    return {k: translate(f'col_{k}', lang) for k in keys}
