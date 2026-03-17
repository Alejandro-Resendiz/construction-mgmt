# Architectural Decisions & System Overview

This document outlines the high-level architecture and key design decisions made for the Management System.

## 🏗️ High-Level Architecture

The application is built as a **Modular Streamlit Dashboard**, prioritizing scalability and separation of concerns.

### 1. Modular Design
- **Core Engine (`app.py`):** Acts as the central orchestrator and navigation hub.
- **Business Modules (`modules/`):** Each business unit (e.g., `machinery.py`) contains its own logic, constants (like `DEFAULT_WORKING_HOURS`), and data mapping rules.
- **Shared Utilities (`utils/`):** Contains cross-cutting concerns like internationalization (`i18n.py`), configuration (`config.py`), and specialized data cleaning tools.

### 2. Internationalization (i18n) & Whitelabeling
- **Dynamic App Name:** The application name is configurable via the `APP_NAME` environment variable.
- **Dictionary-Based Mapping:** A central `translations` dictionary maps internal English keys to English and Spanish display names.
- **Dynamic UI:** All labels, charts, and table headers update reactively based on the user's language selection.
- **Standardized Keys:** Internal logic uses snake_case keys (e.g., `total_cost_per_hour`), while the UI and Export files use the translated human-readable equivalents (e.g., `Costo Total por Hora`).

### 3. Data Integrity & Validation
- **Strict Numeric Input:** To ensure accuracy and prevent legacy spreadsheet errors (like `#DIV/0!`), the system enforces pure numeric input.
- **Name-Based Mapping:** The system dynamically identifies headers in either English or Spanish, removing reliance on fixed column indexes which are prone to breakage if the source CSV structure changes.
- **Row-Level Error Reporting:** Instead of failing silently, the app provides specific row/column feedback to the user for data correction.

---

## 🚀 Application Features

### 🚜 Machinery Cost Module
- **Automated Calculations:** Computes Fuel, Operator, Maintenance, and Depreciation costs per hour based on industry-standard formulas.
- **Configurable Parameters:** Allows real-time adjustment of operational constants like "Working Hours per Year."
- **Data Mapping:** Automatically translates Spanish spreadsheet headers into a standardized internal data format.

### 📅 Weekly Breakdown Module (Consolidado Semanal)
- **Efficiency Tracking:** Compares planned vs. registered hours and fuel consumption.
- **Variation Analysis:** Automatically calculates variation percentages for hours and fuel usage.
- **Operational Metrics:** Computes real liters per hour (L/h) for actual fleet performance monitoring.

### 📊 Interactive Dashboard
- **Fleet Summary KPIs:** Instant visibility into total fleet investment, average rent rates, hour/fuel variation, and total consumption.
- **Visual Analytics:** Stacked bar charts for cost breakdowns and activity distribution; pie charts for project-based consumption.
- **Performance Mapping:** Scatter plots to identify machine performance outliers and operational efficiency.

### 📥 Export & Integration
- **Localized Exports:** Generates clean CSV results with headers matching the user's active language.
- **Mock Data Generation:** Built-in capability to generate "perfect" templates for testing and onboarding new machinery.

---

## 🛠️ Technology Stack
- **Language:** Python 3.11
- **Frontend/App Framework:** Streamlit
- **Data Processing:** Pandas & NumPy
- **Visualizations:** Plotly Express
- **Statistical Analysis:** Statsmodels (for dashboard trendlines)
