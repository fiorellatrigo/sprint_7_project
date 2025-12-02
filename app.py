import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leemos los datos del archivo CSV
car_data = pd.read_csv(
    r"C:\Users\USED\Desktop\Curso TripleTen\Sprint 7\Proyecto Final\sprint_7_project\vehicles_us.csv")

# Creamos el encabezado
st.header('Análisis de datos de anuncios de venta de coches')

# Creamos un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Creamos otro botón para un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

# Lógica a ejecutar cuando se hace clic en el botón 2
if scatter_button:
    # Escribimos un mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Creamos un gráfico de dispersión utilizando plotly.graph_objects
    fig = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)
