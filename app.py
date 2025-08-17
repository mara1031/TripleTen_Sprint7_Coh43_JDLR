import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de ventas de vehículos usados') # título de la aplicación

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de vehículos usados')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
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
    
    