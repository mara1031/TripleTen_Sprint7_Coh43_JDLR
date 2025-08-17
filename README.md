# TripleTen_Sprint7_Coh43_JDLR
Sprint 7 del bootcamp de Análisis de Datos de TripleTen, enfocado en introducir el desarrollo de aplicaciones web con Streamlit.

# Análisis de Vehículos Usados

Aplicación web interactiva creada con Streamlit para visualizar datos de vehículos usados. Proyecto desarrollado como parte del bootcamp de TripleTen.

## Funcionalidades

- **Histograma de millaje**: Muestra la distribución de kilometraje de los vehículos.
- **Evolución de precios**: Gráfico de líneas que compara el precio promedio por condición del vehículo a lo largo del tiempo.

## Cómo Usar

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

2. Ejecutar la aplicación:
   streamlit run app.py

3. Interactuar:

- Haz clic en Histograma (Millaje) para ver la distribución de kilometraje.
- Marca la casilla Construir evolución precio promedio por día para analizar tendencias de precios.

Datos:
- Dataset: vehicles_us.csv (anuncios de vehículos usados)
- Columnas principales: odometer (millaje), price (precio), condition (condición), date_posted (fecha de publicación).

Tecnologías:

- Python 3
- Streamlit (interfaz web)
- Plotly Express (visualizaciones)
- Pandas (análisis de datos)
