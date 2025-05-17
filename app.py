import streamlit as st
from views import charge, analysis, indicators, home

st.title("FILE X")
st.sidebar.title("Menú")
st.sidebar.header("Navegar")

selected_page = st.sidebar.radio("Dirigir a:", ["Inicio", "Cargar archivo", "Análisis exploratorio", "Indicadores", "Gráficas"])

if selected_page == "Inicio":
    home.show()
elif selected_page == "Cargar archivo":
    charge.charge_file()
elif selected_page == "Análisis exploratorio":
    analysis.basic_analysis()
elif selected_page == "Indicadores":
    indicators.show()
else:
    st.title("Estado pendientes")
    st.write("Contact us at: example@email.com")