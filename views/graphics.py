import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    st.title("Gráficas de Análisis de Gladiadores")
    
    if 'data' not in st.session_state:
        st.warning("No se ha cargado un archivo aún. Por favor carga los datos en la pestaña 'Cargar archivo'.")
        return
    
    data = st.session_state['data']
    
    # SOLUCIÓN: Usar estilos disponibles actuales
    available_styles = plt.style.available
    print("Estilos disponibles:", available_styles)  # Para diagnóstico
    
    # Configuración de estilo segura
    try:
        plt.style.use('seaborn-v0_8-pastel')  # Estilo moderno equivalente
    except:
        plt.style.use('ggplot')  # Fallback a un estilo básico
    
    sns.set_theme(style="whitegrid")
    
    # Gráfica 1: Cantidad de Gladiadores por Categoría
    st.subheader("1. Cantidad de Gladiadores por Categoría")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    category_counts = data['Category'].value_counts()
    category_counts.plot(kind='bar', ax=ax1, color=sns.color_palette("pastel"))
    ax1.set_xlabel('Categoría de Gladiador')
    ax1.set_ylabel('Cantidad')
    ax1.set_title('Distribución de Gladiadores por Categoría')
    plt.xticks(rotation=45)
    st.pyplot(fig1)
    
    st.write("""
    **Análisis:** Esta gráfica muestra cuántos gladiadores hay en cada categoría. 
    Nos ayuda a entender qué tipos de gladiadores son más comunes en el dataset.
    """)
    
    # Gráfica 2: Promedio de Victorias por Categoría de Gladiador
    st.subheader("2. Promedio de Victorias por Categoría de Gladiador")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    avg_wins = data.groupby('Category')['Wins'].mean().sort_values(ascending=False)
    avg_wins.plot(kind='bar', ax=ax2, color=sns.color_palette("pastel"))
    ax2.set_xlabel('Categoría de Gladiador')
    ax2.set_ylabel('Promedio de Victorias')
    ax2.set_title('Rendimiento Promedio por Categoría')
    plt.xticks(rotation=45)
    st.pyplot(fig2)
    
    st.write("""
    **Análisis:** Esta gráfica compara el rendimiento promedio de las diferentes categorías de gladiadores.
    Muestra qué tipos de gladiadores tienden a tener más victorias en promedio.
    """)
    
    # Gráfica 3: Relación entre Experiencia de Batalla y Conocimiento Táctico
    st.subheader("3. Relación entre Experiencia y Conocimiento Táctico")
    
    tactical_mapping = {'Novice': 0, 'Intermediate': 1, 'Advanced': 2, 'Expert': 3}
    data['Tactical Level'] = data['Tactical Knowledge'].map(tactical_mapping)
    
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=data, x='Battle Experience', y='Tactical Level', 
                   hue='Survived', style='Survived', s=100, ax=ax3,
                   palette="pastel")
    ax3.set_xlabel('Experiencia de Batalla (número de combates)')
    ax3.set_ylabel('Nivel de Conocimiento Táctico')
    ax3.set_title('Relación entre Experiencia y Conocimiento Táctico\n(coloreado por supervivencia)')
    
    handles, labels = ax3.get_legend_handles_labels()
    ax3.legend(handles=handles[1:], labels=['No Sobrevivió', 'Sobrevivió'], 
              title='Supervivencia', loc='upper left')
    
    ax3.set_yticks([0, 1, 2, 3])
    ax3.set_yticklabels(['Novato', 'Intermedio', 'Avanzado', 'Experto'])
    
    st.pyplot(fig3)
    
    st.write("""
    **Análisis:** Esta gráfica explora la relación entre la experiencia en combate (número de batallas) 
    y el nivel de conocimiento táctico del gladiador, diferenciando entre quienes sobrevivieron y quienes no.
    """)