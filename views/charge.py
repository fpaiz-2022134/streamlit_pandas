import streamlit as st
import pandas as pd

def charge_file():
    st.title("Cargar Archivo")
    st.write("Bienvenido al cargador de documentos FileX")
    file_uploaded = st.file_uploader("Agrega el archivo para procesar (CSV): ", accept_multiple_files=False)

    if file_uploaded is not None:
        try:
            data = pd.read_csv(file_uploaded)
            columns = data.columns.to_list()
        except pd.errors.ParserError:
            data = pd.read_excel(file_uploaded)

        st.session_state['data'] = data
        st.session_state['columns'] = columns

        st.success("Archivo cargado exitosamente")
        st.dataframe(data)