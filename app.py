import streamlit as st
import pandas as pd
import plotly.express as px
from utils.config import APP_NAME
from modules.machinery import load_and_map_data, calculate_costs, validate_data, DEFAULT_WORKING_HOURS
from modules.weekly import load_and_map_data as load_weekly, calculate_weekly, validate_data as validate_weekly
from utils.i18n import translate, get_column_map

st.set_page_config(page_title=f"{APP_NAME} Management System", layout="wide")

def main():
    if 'lang' not in st.session_state:
        st.session_state.lang = 'es'
    
    st.sidebar.title(translate('title', st.session_state.lang))
    
    lang_options = {'Español': 'es', 'English': 'en'}
    selected_lang_name = st.sidebar.selectbox("Language / Idioma", list(lang_options.keys()), 
                                            index=0 if st.session_state.lang == 'es' else 1)
    st.session_state.lang = lang_options[selected_lang_name]
    
    module_options = {
        translate('machinery_cost', st.session_state.lang): "Machinery Cost",
        translate('weekly_breakdown', st.session_state.lang): "Weekly Breakdown",
        translate('future_module', st.session_state.lang): "Future Module"
    }
    
    module_label = st.sidebar.selectbox(translate('select_module', st.session_state.lang), list(module_options.keys()))
    module = module_options[module_label]

    if module == "Machinery Cost":
        machinery_cost_module()
    elif module == "Weekly Breakdown":
        weekly_breakdown_module()
    else:
        st.info(translate('future_module', st.session_state.lang))

def weekly_breakdown_module():
    lang = st.session_state.lang
    st.title(translate('weekly_title', lang))
    st.markdown(translate('weekly_desc', lang))

    uploaded_file = st.file_uploader(translate('choose_file', lang), type="csv")

    if uploaded_file is not None:
        try:
            df = load_weekly(uploaded_file, lang)
            
            st.subheader(translate('validation', lang))
            errors = validate_weekly(df, lang)
            
            if errors:
                for err in errors:
                    st.error(err)
                return

            st.success(translate('success_data', lang))

            st.sidebar.subheader(translate('settings', lang))
            weekly_diesel_price = st.sidebar.number_input(translate('diesel_price', lang), value=22.0, step=0.1)

            if st.button(translate('calc_button', lang)):
                results = calculate_weekly(df)
                # Calculate fuel spent
                results['fuel_spent'] = results['liters_real_consumption'] * weekly_diesel_price
                
                st.subheader(translate('results', lang))
                display_map = get_column_map(lang, module='weekly')
                display_results = results.rename(columns=display_map)
                
                st.dataframe(display_results.style.format({
                    display_map['hours_variation']: '{:.2%}',
                    display_map['liters_variation']: '{:.2%}',
                    display_map['liters_real_per_hour']: '{:.2f} L/h',
                    display_map['liters_forecasted']: '{:.1f} L',
                    display_map['fuel_spent']: '${:,.2f}'
                }))

                st.subheader(translate('dashboard', lang))
                kpi1, kpi2, kpi3, kpi4 = st.columns(4)
                with kpi1:
                    avg_hours_var = results['hours_variation'].mean()
                    st.metric(translate('kpi_avg_hours_var', lang), f"{avg_hours_var:.2%}")
                with kpi2:
                    avg_fuel_var = results['liters_variation'].mean()
                    st.metric(translate('kpi_avg_fuel_var', lang), f"{avg_fuel_var:.2%}")
                with kpi3:
                    total_liters = results['liters_real_consumption'].sum()
                    st.metric(translate('kpi_total_liters', lang), f"{total_liters:,.1f} L")
                with kpi4:
                    total_spent = results['fuel_spent'].sum()
                    st.metric(translate('kpi_total_spent', lang), f"${total_spent:,.2f}")

                col_chart1, col_chart2 = st.columns(2)
                with col_chart1:
                    # Hours by Activity
                    fig_activity = px.bar(results, x='activity_name', y='worked_hours_registered', 
                                         color='project_name', title=translate('chart_activity_hours', lang),
                                         labels={'activity_name': translate('col_activity_name', lang), 
                                                 'worked_hours_registered': translate('col_worked_hours_registered', lang),
                                                 'project_name': translate('col_project_name', lang)})
                    st.plotly_chart(fig_activity, use_container_width=True)

                with col_chart2:
                    # Fuel by Project
                    fig_project = px.pie(results, names='project_name', values='liters_real_consumption', 
                                        title=translate('chart_project_fuel', lang),
                                        labels={'project_name': translate('col_project_name', lang), 
                                                'liters_real_consumption': translate('col_liters_real_consumption', lang)})
                    st.plotly_chart(fig_project, use_container_width=True)

                # NEW CHART: Spent by Project
                spent_by_project = results.groupby('project_name')['fuel_spent'].sum().reset_index()
                fig_spent = px.bar(spent_by_project, x='project_name', y='fuel_spent', 
                                  title=translate('chart_project_spent', lang),
                                  labels={'project_name': translate('col_project_name', lang), 
                                          'fuel_spent': translate('col_fuel_spent', lang)},
                                  text_auto='.2s')
                st.plotly_chart(fig_spent, use_container_width=True)

                # Performance Chart
                fig_perf = px.scatter(results, x='worked_hours_registered', y='liters_real_per_hour', 
                                     hover_name='machine', color='machine_model', size='liters_real_consumption',
                                     title=translate('chart_fuel_performance', lang),
                                     labels={'worked_hours_registered': translate('col_worked_hours_registered', lang), 
                                             'liters_real_per_hour': translate('col_liters_real_per_hour', lang),
                                             'machine': translate('col_machine', lang)})
                st.plotly_chart(fig_perf, use_container_width=True)

                st.subheader(translate('export', lang))
                csv = display_results.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label=translate('download_button', lang),
                    data=csv,
                    file_name="weekly_breakdown_results.csv",
                    mime="text/csv",
                )

        except Exception as e:
            st.error(translate('error_processing', lang, error=str(e)))

def machinery_cost_module():
    lang = st.session_state.lang
    st.title(translate('upload_title', lang))
    st.markdown(translate('upload_desc', lang))

    uploaded_file = st.file_uploader(translate('choose_file', lang), type="csv")

    if uploaded_file is not None:
        try:
            df = load_and_map_data(uploaded_file, lang)
            
            st.subheader(translate('validation', lang))
            errors = validate_data(df, lang)
            
            if errors:
                for err in errors:
                    st.error(err)
                return

            st.success(translate('success_data', lang))

            st.sidebar.subheader(translate('settings', lang))
            working_hours = st.sidebar.number_input(translate('working_hours', lang), value=DEFAULT_WORKING_HOURS, step=1)

            if st.button(translate('calc_button', lang)):
                results = calculate_costs(df, working_hours)
                results = results[results['id'].notna()]
                
                st.subheader(translate('results', lang))
                
                # Get translated column map for display
                display_map = get_column_map(lang)
                display_results = results.rename(columns=display_map)
                
                st.dataframe(display_results.style.format({
                    display_map['purchase_value']: '${:,.2f}',
                    display_map['total_cost_per_hour']: '${:,.2f}',
                    display_map['rent_rate_per_hour']: '${:,.2f}',
                    display_map['fuel_cost_per_hour']: '${:,.2f}',
                    display_map['operator_cost_per_hour']: '${:,.2f}',
                    display_map['maintenance_cost_per_hour']: '${:,.2f}',
                    display_map['depreciation_cost_per_hour']: '${:,.2f}'
                }))

                st.subheader(translate('dashboard', lang))
                kpi1, kpi2, kpi3 = st.columns(3)
                with kpi1:
                    total_inv = results['purchase_value'].sum()
                    st.metric(translate('kpi_investment', lang), f"${total_inv:,.2f}")
                with kpi2:
                    avg_rent = results['rent_rate_per_hour'].mean()
                    st.metric(translate('kpi_rent', lang), f"${avg_rent:,.2f}")
                with kpi3:
                    total_machines = len(results)
                    st.metric(translate('kpi_count', lang), total_machines)

                col_chart1, col_chart2 = st.columns(2)
                with col_chart1:
                    # Cost Breakdown Chart
                    cost_components = {
                        'fuel_cost_per_hour': translate('fuel', lang),
                        'operator_cost_per_hour': translate('operator', lang),
                        'maintenance_cost_per_hour': translate('maintenance', lang),
                        'depreciation_cost_per_hour': translate('depreciation', lang)
                    }
                    df_melted = results.melt(id_vars=['machinery'], value_vars=list(cost_components.keys()), 
                                            var_name=translate('cost_component', lang), value_name='Cost')
                    df_melted[translate('cost_component', lang)] = df_melted[translate('cost_component', lang)].map(cost_components)
                    
                    fig_costs = px.bar(df_melted, x='machinery', y='Cost', color=translate('cost_component', lang), 
                                      title=translate('chart_breakdown', lang),
                                      labels={'machinery': translate('col_machinery', lang), 'Cost': '$/h'})
                    st.plotly_chart(fig_costs, use_container_width=True)

                with col_chart2:
                    # Rent vs Total Cost
                    fig_rent = px.scatter(results, x='total_cost_per_hour', y='rent_rate_per_hour', 
                                         hover_name='machinery', title=translate('chart_rent_vs_cost', lang),
                                         labels={'total_cost_per_hour': translate('col_total_cost_per_hour', lang), 
                                                 'rent_rate_per_hour': translate('col_rent_rate_per_hour', lang),
                                                 'machinery': translate('col_machinery', lang)},
                                         trendline="ols")
                    st.plotly_chart(fig_rent, use_container_width=True)

                st.subheader(translate('export', lang))
                csv = display_results.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label=translate('download_button', lang),
                    data=csv,
                    file_name="machinery_calculations.csv",
                    mime="text/csv",
                )

        except Exception as e:
            st.error(translate('error_processing', lang, error=str(e)))

if __name__ == "__main__":
    main()
