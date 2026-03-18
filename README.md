# Hiv Management System

An automated tool to manage Construction Machinery fleet, starting with cost calculation and KPI monitoring.

> **Note:** The application name is configurable. Set the `APP_NAME` environment variable to customize it across the UI.

## 🚀 Development Setup

### Prerequisites
- Python 3.11
- `pyenv` (recommended)

### Environment Configuration
1.  **Set the application name (optional):**
    ```bash
    export APP_NAME="MyCompanyName"
    ```

2.  **Create and activate the virtual environment:**
    ```bash
    pyenv virtualenv 3.11 machinery-mgmt
    pyenv activate machinery-mgmt
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

---

## 📂 Project Structure
- `app.py`: Main Streamlit entry point.
- `modules/`: Contains business logic modules (e.g., `machinery.py`).
- `utils/`: Shared utility functions for data parsing and cleaning.
- `Data/`: Folder for source CSV files.

---

## 🚜 Machinery Cost Module

### Input Requirements
The application expects a CSV file with the following Spanish headers (mapping to English keys automatically):
- `Código` (id)
- `MAQUINARIA` (machinery)
- `VIDA ÚTIL (AÑOS)` (lifespan_years)
- `VALOR DE COMPRA` (purchase_value)
- `VALOR DE RESCATE (%)` (rescue_value_percent)
- `CONSUMO DE DIÉSEL (L)` (diesel_consumption_in_liters)
- `PRECIO DE DÍESEL` (diesel_price)
- `SUELDO POR OPERADOR` (operator_wage)
- `COSTO DE MANTENIMIENTO` (maintenance_cost)
- `HORAS TRABAJADAS` (worked_hours)
- `Utilidad (%)` (utility_percent)

### Formulas Used
- **Rescue Value:** `purchase_value * rescue_value_percent`
- **Fuel Cost/hr:** `(diesel_consumption * diesel_price) / worked_hours`
- **Operator Cost/hr:** `operator_wage / worked_hours`
- **Maintenance Cost/hr:** `maintenance_cost / worked_hours`
- **Depreciation Cost/hr:** `(purchase_value - rescue_value) / lifespan_years / 2112`
- **Total Cost/hr:** Sum of all hourly costs.
- **Rent Rate/hr:** `total_cost * (1 + utility_percent)`

---

## 🚜 Weekly Breakdown Module

### Input Requirements
The application expects a CSV file with the following Spanish headers (mapping to English keys automatically):
- `MÁQUINA` (machine)
- `MODELO` (machine_model)
- `NÚMERO DE SERIE` (machine_serial_number)
- `PROYECTO` (project_name)
- `OPERADOR` (operator_name)
- `ACTIVIDAD` (activity_name)
- `HORAS TRABAJADAS ESTIMADAS EN PLAN` (worked_hours_forecasted)
- `HORAS TRABAJADAS REALES REGISTRADAS` (worked_hours_registered)
- `USO PROMEDIO DE COMBUSTIBLE` (fuel_average_usage)
- `LITROS CONSUMIDOS REALES` (liters_real_consumption)

### Formulas Used
- **LITROS ESTIMADOS EN PLAN (liters_forecasted)**: `fuel_average_usage * worked_hours_forecasted`
- **VARIACIÓN EN HORAS (hours_variation):** `worked_hours_registered / worked_hours_forecasted`
- **VARIACIÓN EN LITROS (liters_variation):** `liters_real_consumption / liters_forecasted`
- **LITROS POR HORA [REALES] (liters_real_per_hour)**: `liters_real_consumption / worked_hours_registered`

---

## 🚜 HR Pipeline Module

### Input Requirements
The application expects a CSV file with the following Spanish headers (mapping to English keys automatically):
- `ID/Nombre` (person_full_name)
- `Vacante` (position)
- `Nivel` (seniority) -> Senior | Semi Senior | Junior | Concretera
- `Fuente` (source)
- `Fecha_aplicacion` (application_date) DD/MM/YYYY
- `Screening` (screening) -> Aprobado | No aprobado
- `Filtro_HR` (hr_filter) ->  Aprobado | No aprobado
- `Entrevista_Tecnica` (technical_interview) ->  Aprobado | No aprobado
- `Referencias` (references) ->  Aprobado | Pendiente | Negativas
- `Oferta` (offer) ->  Pendiente | Aceptada | Rechazada
- `Fecha_oferta` (offer_date) -> N/A | DD/MM/YYYY
- `Fecha_ingreso` (start_date) -> N/A | DD/MM/YYYY
- `Comentarios` (comments)

### Formulas Used
- **Etapa_actual (current_stage)**: 
    - Ingreso: `offer == 'Aceptada'`
    - Oferta: `references == 'Aprobado'`
    - Referencias: `technical_interview == 'Aprobado'`
    - Entrevista: `hr_filter == 'Aprobado'`
    - Filtro_HR: `screening == 'Aprobado'`
    - Screening: `default`
- **Estatus_final (final_status)**: 
    - Rechazado: `screening == 'No aprobado | hr_filter == 'No aprobado | technical_interview == 'No aprobado | references == 'Negativas | offer == 'Rechazada`
    - Contratado: `offer == 'Aceptada'`
    - Proceso activo: `default`
- **Time_to_Hire (time_to_hire)**: `difference_in_days(start_date, application_date)` 

### KPIs
- **Total candidatos (candidate_count)**: `count(ID/Nombre)`
- **Screening (screening_count):** `count(current_stage == 'Screening')`
- **Filtro HR (hr_filter_count):** `count(current_stage == 'Filtro_HR')`
- **Entrevista (interview_count):** `count(current_stage == 'Entrevista')`
- **Referencias (reference_count):** `count(current_stage == 'Referencias')`
- **Oferta (offer_count):** `count(current_stage == 'Oferta')`
- **Contratados (hired_count):** `count(current_stage == 'Ingreso')`
- **Time to Hire promedio (time_to_hire_avg):** `avg(time_to_hire)`
- **Conversion Rate (conversion_rate):** `hired_count / candidate_count`