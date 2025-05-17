import streamlit as st
import pandas as pd

def basic_analysis():
    st.title("Análisis")
    if 'data' in st.session_state and 'columns' in st.session_state:
        data = st.session_state['data']
        columns = st.session_state['columns']
        
        st.write("Número de filas y columnas (filas, columnas):")    
        st.write(data.shape)
        
        columns_df = pd.DataFrame(columns, columns=["Nombre de columna"])
        st.write("Lista de columnas:")
        st.dataframe(columns_df)

        st.write("Primeras filas")
        st.write(data.head(10))
        
        st.write("Estadísticas generales")
        st.dataframe(data.describe())
    else:
        st.warning("No se ha cargado un archivo aún.")