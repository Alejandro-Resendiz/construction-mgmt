# Single Source of Truth for all Module Schemas

MACHINERY_SCHEMA = {
    'id': {'en': "ID", 'es': "Código"},
    'machinery': {'en': "Machinery", 'es': "MAQUINARIA"},
    'lifespan_years': {'en': "Lifespan (Years)", 'es': "VIDA ÚTIL (AÑOS)"},
    'purchase_value': {'en': "Purchase Value", 'es': "VALOR DE COMPRA"},
    'rescue_value_percent': {'en': "Rescue Value (%)", 'es': "VALOR DE RESCATE (%)"},
    'diesel_consumption_in_liters': {'en': "Diesel Consumption (L)", 'es': "CONSUMO DE DIÉSEL (L)"},
    'diesel_price': {'en': "Diesel Price", 'es': "PRECIO DE DÍESEL"},
    'operator_wage': {'en': "Operator Wage", 'es': "SUELDO POR OPERADOR"},
    'maintenance_cost': {'en': "Maintenance Cost", 'es': "COSTO DE MANTENIMIENTO"},
    'worked_hours': {'en': "Worked Hours", 'es': "HORAS TRABAJADAS"},
    'utility_percent': {'en': "Utility (%)", 'es': "Utilidad (%)"},
}

WEEKLY_SCHEMA = {
    'machine': {'en': "Machine", 'es': "MÁQUINA"},
    'machine_model': {'en': "Model", 'es': "MODELO"},
    'machine_serial_number': {'en': "Number of Serie", 'es': "NÚMERO DE SERIE"},
    'project_name': {'en': "Project", 'es': "PROYECTO"},
    'operator_name': {'en': "Operator", 'es': "OPERADOR"},
    'activity_name': {'en': "Activity", 'es': "ACTIVIDAD"},
    'worked_hours_forecasted': {'en': "Planned Hours", 'es': "HORAS TRABAJADAS ESTIMADAS EN PLAN"},
    'worked_hours_registered': {'en': "Registered Hours", 'es': "HORAS TRABAJADAS REALES REGISTRADAS"},
    'fuel_average_usage': {'en': "Avg. Fuel Usage (L/h)", 'es': "USO PROMEDIO DE COMBUSTIBLE"},
    'liters_real_consumption': {'en': "Real Liters Consumed", 'es': "LITROS CONSUMIDOS REALES"},
}

HR_SCHEMA = {
    'person_full_name': {'en': "Name", 'es': "ID/Nombre"},
    'position': {'en': "Position", 'es': "Vacante"},
    'seniority': {'en': "Seniority", 'es': "Nivel"},
    'source': {'en': "Source", 'es': "Fuente"},
    'application_date': {'en': "Application Date", 'es': "Fecha_aplicacion"},
    'screening': {'en': "Screening", 'es': "Screening"},
    'hr_filter': {'en': "HR Filter", 'es': "Filtro_HR"},
    'technical_interview': {'en': "Technical Interview", 'es': "Entrevista_Tecnica"},
    'references': {'en': "References", 'es': "Referencias"},
    'offer': {'en': "Offer", 'es': "Oferta"},
    'offer_date': {'en': "Offer Date", 'es': "Fecha_oferta"},
    'start_date': {'en': "Start Date", 'es': "Fecha_ingreso"},
    'comments': {'en': "Comments", 'es': "Comentarios"},
}
