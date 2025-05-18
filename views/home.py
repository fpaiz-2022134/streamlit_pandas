import streamlit as st

st.set_page_config(
    page_title="Gladiator Analytics",
    layout="centered"
)

def show():
    st.markdown("""
    <style>
        .title {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 0.5rem;
        }
        .subtitle {
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="title"> FILE X GLADIATOR ANALYTICS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Herramienta de análisis estratégico para combates en la arena</p>', unsafe_allow_html=True)

    st.subheader("Características Principales")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**Análisis de Datos**\n\nExplora estadísticas detalladas")
    
    with col2:
        st.info("**Indicadores Clave**\n\nMétricas de rendimiento")
    
    with col3:
        st.info("**Visualizaciones**\n\nGráficos interactivos")


    st.subheader("Sobre el Programa")
    st.write("""
    Plataforma de análisis estratégico para:
    - Evaluar rendimiento
    - Identificar fortalezas
    - Tomar decisiones con datos
    - Descubrir patrones
    """)


    st.markdown("---")
    if st.button("**Comenzar Análisis**", use_container_width=True):
        st.session_state.page = "Cargar archivo"


    st.markdown("---")
    st.caption("Developed by Franco Paiz")