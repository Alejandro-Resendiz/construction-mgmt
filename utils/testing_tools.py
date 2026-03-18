import pandas as pd
import random
import io
import numpy as np
from datetime import datetime, timedelta
from tests.data_contracts import MACHINERY_SCHEMA, WEEKLY_SCHEMA, HR_SCHEMA

def generate_mock_csv(module_type="machinery", lang="es", rows=10, profile="happy_path"):
    """
    Generates a mock CSV string based on schemas and profiles.
    Profiles: 'happy_path', 'noisy' (bad types), 'incomplete' (missing cols)
    """
    if module_type == "machinery": schema = MACHINERY_SCHEMA
    elif module_type == "weekly": schema = WEEKLY_SCHEMA
    else: schema = HR_SCHEMA
    
    cols = [details[lang] for details in schema.values()]
    
    if profile == "incomplete":
        cols.pop(random.randint(0, len(cols)-1))
        
    data = []
    for i in range(rows):
        row = {}
        for key, details in schema.items():
            display_name = details[lang]
            if display_name not in cols:
                continue
                
            if profile == "noisy" and random.random() < 0.1:
                row[display_name] = "NOT_A_VAL"
            else:
                row[display_name] = _generate_value(module_type, key, i)
        data.append(row)
        
    df = pd.DataFrame(data)
    output = io.StringIO()
    df.to_csv(output, index=False)
    return output.getvalue()

def _generate_value(module, key, index):
    if module == "machinery":
        if key == 'id': return f"M-{index+1:03d}"
        if key == 'machinery': return f"Machine {index+1}"
        if key == 'lifespan_years': return random.randint(5, 15)
        if key == 'purchase_value': return random.randint(50000, 250000)
        if key == 'rescue_value_percent': return 0.2
        if key in ['diesel_consumption_in_liters', 'diesel_price', 'operator_wage', 'maintenance_cost']:
            return random.randint(10, 100)
        if key == 'worked_hours': return random.randint(100, 2000)
        if key == 'utility_percent': return 0.25
        
    if module == "weekly":
        if key == 'machine': return f"M-{index+1:03d}"
        if key == 'machine_model': return f"Model X-{index}"
        if key == 'machine_serial_number': return f"SN-{random.randint(1000, 9999)}"
        if key == 'project_name': return random.choice(["Alpha", "Beta", "Gamma"])
        if key == 'operator_name': return random.choice(["John", "Jane", "Doe"])
        if key == 'activity_name': return random.choice(["Excavation", "Loading", "Transport"])
        if key == 'worked_hours_forecasted': return 40
        if key == 'worked_hours_registered': return random.randint(35, 45)
        if key == 'fuel_average_usage': return 10.5
        if key == 'liters_real_consumption': return random.randint(300, 500)

    if module == "hr":
        if key == 'person_full_name': return f"Candidate {index+1}"
        if key == 'position': return random.choice(["Operator", "Driver", "Engineer", "Mechanic"])
        if key == 'seniority': return random.choice(["Junior", "Semi Senior", "Senior", "Concretera"])
        if key == 'source': return random.choice(["LinkedIn", "Referral", "Indeed", "Website"])
        
        # Date generation
        base_date = datetime(2024, 1, 1)
        app_date = base_date + timedelta(days=random.randint(0, 60))
        if key == 'application_date': return app_date.strftime('%d/%m/%Y')
        
        # Success probabilities
        passed_screening = random.random() < 0.8
        passed_hr = passed_screening and random.random() < 0.7
        passed_tech = passed_hr and random.random() < 0.6
        passed_refs = passed_tech and random.random() < 0.9
        accepted_offer = passed_refs and random.random() < 0.8
        
        if key == 'screening': return "Aprobado" if passed_screening else "No aprobado"
        if key == 'hr_filter': return "Aprobado" if passed_hr else "No aprobado"
        if key == 'technical_interview': return "Aprobado" if passed_tech else "No aprobado"
        if key == 'references': return "Aprobado" if passed_refs else ("Negativas" if passed_tech else "Pendiente")
        if key == 'offer': return "Aceptada" if accepted_offer else ("Rechazada" if passed_refs else "Pendiente")
        
        if key == 'offer_date': 
            return (app_date + timedelta(days=15)).strftime('%d/%m/%Y') if passed_refs else "N/A"
        if key == 'start_date':
            return (app_date + timedelta(days=30)).strftime('%d/%m/%Y') if accepted_offer else "N/A"
        if key == 'comments': return "N/A"
        
    return 0
