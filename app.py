import pandas as pd
import plotly.express as px
import streamlit as st

# título de la aplicación
st.header('Análisis Vehículos Usados')

# cargar los datos con caché para optimizar el rendimiento  
@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv') 

car_data = load_data()

# Sección organizada con expanders
with st.expander("Acerca de esta app"):
    st.write("""
    Explora el dataset de vehículos usados. 
    Genera visualizaciones con los botones siguientes.
    """)

hist_button = st.button('Histograma (Millaje)') # crear un botón
     
if hist_button: # al hacer clic en el botón
   
    st.write('Distribución de millaje de los vehículos')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer",
                       title="Millaje de Vehículos Usados") # Título del gráfico
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_lineplot = st.checkbox('Construir evolución precio promedio por día')

if build_lineplot: # si la casilla de verificación está seleccionada
    st.write('Evolución del precio promedio según la condición del vehículo')
    
    # agrupar los datos por fecha de publicación y condición del vehículo
    df_agrupado = car_data.groupby(['date_posted', 'condition'])['price'].mean().reset_index()
    
    fig_2 = px.line(df_agrupado, x='date_posted', y='price', color='condition',title= 'Precio promedio según la condición del vehículo')  
    
    # mostrar el gráfico interactivo
    st.plotly_chart(fig_2, use_container_width=True)
    
    