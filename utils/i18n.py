from utils.config import APP_NAME
from tests.data_contracts import MACHINERY_SCHEMA, WEEKLY_SCHEMA, HR_SCHEMA

translations = {
    'en': {
        'title': f"{APP_NAME} Management System",
        'select_module': "Select Module",
        'machinery_cost': "Machinery Cost",
        'weekly_breakdown': "Weekly Breakdown",
        'hr_pipeline': "HR Pipeline",
        'future_module': "Future Module...",
        'upload_title': "🚜 Machinery Cost Calculation",
        'weekly_title': "📅 Weekly Consolidated Report",
        'hr_title': "👥 Recruitment Pipeline",
        'upload_desc': "Upload the machinery cost CSV file. Requirements: Pure numeric values (e.g., 0.2 for 20%), no currency symbols.",
        'weekly_desc': "Upload the weekly registered hours and fuel CSV file. All numeric values must be pure (no symbols).",
        'hr_desc': "Upload the recruitment pipeline CSV file. Date format: MM/DD/YYYY.",
        'choose_file': "Choose a CSV file",
        'validation': "1. Data Validation & Cleaning",
        'missing_cols_error': "Missing required columns: {cols}",
        'non_numeric_error': "Column '{col}' contains non-numeric values at rows: {rows}",
        'success_data': "All data is valid.",
        'settings': "Settings",
        'working_hours': "Working Hours per Year",
        'diesel_price': "Diesel Price ($/L)",
        'calc_button': "Calculate Results",
        'results': "2. Calculated Results",
        'dashboard': "3. Analytics Dashboard",
        'kpi_investment': "Total Fleet Investment",
        'kpi_rent': "Avg. Rent Rate / Hour",
        'kpi_count': "Active Machinery Count",
        'kpi_avg_hours_var': "Avg. Hours Variation",
        'kpi_avg_fuel_var': "Avg. Fuel Variation",
        'kpi_total_liters': "Total Registered Liters",
        'kpi_total_spent': "Total Fuel Expenditure",
        # HR KPIs
        'kpi_candidates': "Total Candidates",
        'kpi_hired': "Hired Count",
        'kpi_conversion': "Conversion Rate",
        'kpi_avg_time_to_hire': "Avg. Time to Hire (Days)",
        # HR Stages
        'stage_screening': "Screening",
        'stage_hr_filter': "HR Filter",
        'stage_interview': "Interview",
        'stage_references': "References",
        'stage_offer': "Offer",
        'stage_hired': "Hired",
        # Charts
        'chart_breakdown': "Cost Breakdown per Machine",
        'chart_rent_vs_cost': "Rent Rate vs. Total Cost",
        'chart_activity_hours': "Registered Hours by Activity",
        'chart_project_fuel': "Fuel Consumption by Project (Liters)",
        'chart_project_spent': "Fuel Expenditure by Project ($)",
        'chart_fuel_performance': "Liters per Hour vs. Registered Hours",
        'chart_hr_funnel': "Recruitment Funnel",
        'chart_hr_source': "Source Effectiveness",
        'chart_hr_position': "Candidates by Position",
        'chart_hr_status': "Final Status Distribution",
        'export': "4. Export Results",
        'download_button': "Download Results as CSV",
        'error_processing': "Error processing file: {error}",
        # Components
        'fuel': "Fuel",
        'operator': "Operator",
        'maintenance': "Maintenance",
        'depreciation': "Depreciation",
        'cost_component': "Cost Component",
        # Calculated
        'col_rescue_value': "Rescue Value",
        'col_fuel_cost_per_hour': "Fuel Cost ($/h)",
        'col_operator_cost_per_hour': "Operator Cost ($/h)",
        'col_maintenance_cost_per_hour': "Maintenance Cost ($/h)",
        'col_depreciation_cost_per_hour': "Depreciation Cost ($/h)",
        'col_total_cost_per_hour': "Total Cost ($/h)",
        'col_rent_rate_per_hour': "Rent Rate ($/h)",
        'col_liters_forecasted': "Planned Liters",
        'col_hours_variation': "Hours Variation",
        'col_liters_variation': "Fuel Variation",
        'col_liters_real_per_hour': "Real Liters / h",
        'col_fuel_spent': "Fuel Expenditure",
        'col_current_stage': "Current Stage",
        'col_final_status': "Final Status",
        'col_time_to_hire': "Time to Hire (Days)",
    },
    'es': {
        'title': f"Sistema de Gestión {APP_NAME}",
        'select_module': "Seleccionar Módulo",
        'machinery_cost': "Costo de Maquinaria",
        'weekly_breakdown': "Consolidado Semanal",
        'hr_pipeline': "Pipeline de Reclutamiento",
        'future_module': "Próximo Módulo...",
        'upload_title': "🚜 Cálculo de Costos de Maquinaria",
        'weekly_title': "📅 Consolidado Semanal de Reportes",
        'hr_title': "👥 Pipeline de Reclutamiento",
        'upload_desc': "Cargue el archivo CSV. Requisitos: Valores numéricos puros (ej. 0.2 para 20%), sin símbolos de moneda.",
        'weekly_desc': "Cargue el archivo CSV de horas registradas y combustible semanal. Los valores numéricos deben ser puros.",
        'hr_desc': "Cargue el archivo CSV del pipeline. Formato de fecha: MM/DD/YYYY.",
        'choose_file': "Seleccione un archivo CSV",
        'validation': "1. Validación y Limpieza de Datos",
        'missing_cols_error': "Faltan columnas requeridas: {cols}",
        'non_numeric_error': "La columna '{col}' contiene valores no numéricos en las filas: {rows}",
        'success_data': "Todos los datos son válidos.",
        'settings': "Configuración",
        'working_hours': "Horas de Trabajo por Año",
        'diesel_price': "Precio de Diésel ($/L)",
        'calc_button': "Calcular Resultados",
        'results': "2. Resultados Calculados",
        'dashboard': "3. Panel de Control Analítico",
        'kpi_investment': "Inversión Total de la Flota",
        'kpi_rent': "Tarifa de Renta Promedio / Hora",
        'kpi_count': "Cantidad de Maquinaria Activa",
        'kpi_avg_hours_var': "Variación Promedio de Horas",
        'kpi_avg_fuel_var': "Variación Promedio de Combustible",
        'kpi_total_liters': "Total Litros Registrados",
        'kpi_total_spent': "Gasto Total en Combustible",
        # HR KPIs
        'kpi_candidates': "Total Candidatos",
        'kpi_hired': "Contratados",
        'kpi_conversion': "Tasa de Conversión",
        'kpi_avg_time_to_hire': "Tiempo de Contratación Prom. (Días)",
        # HR Stages
        'stage_screening': "Screening",
        'stage_hr_filter': "Filtro HR",
        'stage_interview': "Entrevista",
        'stage_references': "Referencias",
        'stage_offer': "Oferta",
        'stage_hired': "Ingreso",
        # Charts
        'chart_breakdown': "Desglose de Costos por Máquina",
        'chart_rent_vs_cost': "Tarifa de Renta vs. Costo Total",
        'chart_activity_hours': "Horas Registradas por Actividad",
        'chart_project_fuel': "Consumo de Combustible por Proyecto (Litros)",
        'chart_project_spent': "Gasto de Combustible por Proyecto ($)",
        'chart_fuel_performance': "Litros por Hora vs. Horas Registradas",
        'chart_hr_funnel': "Embudo de Reclutamiento",
        'chart_hr_source': "Efectividad por Fuente",
        'chart_hr_position': "Candidatos por Vacante",
        'chart_hr_status': "Distribución de Estatus Final",
        'export': "4. Exportar Resultados",
        'download_button': "Descargar Resultados como CSV",
        'error_processing': "Error al procesar el archivo: {error}",
        # Components
        'fuel': "Combustible",
        'operator': "Operador",
        'maintenance': "Mantenimiento",
        'depreciation': "Depreciación",
        'cost_component': "Componente de Costo",
        # Calculated
        'col_rescue_value': "Valor de Rescate",
        'col_fuel_cost_per_hour': "Costo Combustible ($/h)",
        'col_operator_cost_per_hour': "Costo Operador ($/h)",
        'col_maintenance_cost_per_hour': "Costo Mantenimiento ($/h)",
        'col_depreciation_cost_per_hour': "Costo Depreciación ($/h)",
        'col_total_cost_per_hour': "Costo Total por Hora",
        'col_rent_rate_per_hour': "Tarifa Renta por Hora",
        'col_liters_forecasted': "Litros Estimados Plan",
        'col_hours_variation': "Variación de Horas",
        'col_liters_variation': "Variación de Combustible",
        'col_liters_real_per_hour': "Litros por Hora [Real]",
        'col_fuel_spent': "Monto Gastado en Combustible",
        'col_current_stage': "Etapa Actual",
        'col_final_status': "Estatus Final",
        'col_time_to_hire': "Tiempo para Contratar (Días)",
    }
}

def translate(key, lang='en', **kwargs):
    text = translations.get(lang, translations['en']).get(key, key)
    if kwargs:
        return text.format(**kwargs)
    return text

def get_column_map(lang='en', module='machinery'):
    """Returns a map of internal keys to translated display names based on module."""
    if module == 'machinery':
        schema = MACHINERY_SCHEMA
        calculated_keys = ['rescue_value', 'fuel_cost_per_hour', 'operator_cost_per_hour', 
                           'maintenance_cost_per_hour', 'depreciation_cost_per_hour', 
                           'total_cost_per_hour', 'rent_rate_per_hour']
    elif module == 'weekly':
        schema = WEEKLY_SCHEMA
        calculated_keys = ['liters_forecasted', 'hours_variation', 'liters_variation', 
                           'liters_real_per_hour', 'fuel_spent']
    else: # hr
        schema = HR_SCHEMA
        calculated_keys = ['current_stage', 'final_status', 'time_to_hire']
    
    col_map = {k: details[lang] for k, details in schema.items()}
    for k in calculated_keys:
        col_map[k] = translate(f'col_{k}', lang)
        
    return col_map
