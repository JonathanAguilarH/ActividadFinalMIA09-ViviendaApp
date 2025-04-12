import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from sklearn.preprocessing import MinMaxScaler
from folium.plugins import MarkerCluster

# Función para formatear números con separadores de miles
def formatear_miles(valor):
    return "{:,}".format(int(valor)).replace(",", ".")

# Título de la aplicación
st.title("Visualización de Datos de Vivienda")

# Subir el dataset
st.write("Por favor, sube un archivo CSV con datos de viviendas.")
uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Calcular densidad de población y tamaño promedio de habitaciones
    df['poblacion_por_hogar'] = df['population'] / df['households']
    df['habitaciones_por_hogar'] = df['total_rooms'] / df['households']

    # Eliminar valores atípicos (densidad de población > 10)
    df = df[df['poblacion_por_hogar'] <= 10]

    # Normalizar habitaciones_por_hogar
    scaler = MinMaxScaler()
    df['habitaciones_por_hogar_normalizado'] = scaler.fit_transform(df[['habitaciones_por_hogar']])

    # Filtros
    st.sidebar.header("Filtros")

    # Rango de valor de la casa
    valor_min_raw, valor_max_raw = st.sidebar.slider(
        "Rango de valor de la casa",
        min_value=int(df['median_house_value'].min()),
        max_value=int(df['median_house_value'].max()),
        value=(int(df['median_house_value'].min()), int(df['median_house_value'].max()))
    )

    # Mostrar valores formateados junto al slider
    st.sidebar.write(f"Rango: ${formatear_miles(valor_min_raw)} - ${formatear_miles(valor_max_raw)}")

    # Rango de densidad de población
    poblacion_min, poblacion_max = st.sidebar.slider(
        "Rango de población por hogar",
        min_value=float(df['poblacion_por_hogar'].min()),
        max_value=float(df['poblacion_por_hogar'].max()),
        value=(float(df['poblacion_por_hogar'].min()), float(df['poblacion_por_hogar'].max()))
    )

    # Rango de edad de la vivienda
    edad_min, edad_max = st.sidebar.slider(
        "Rango de edad de la vivienda",
        min_value=int(df['housing_median_age'].min()),
        max_value=int(df['housing_median_age'].max()),
        value=(int(df['housing_median_age'].min()), int(df['housing_median_age'].max()))
    )

    # Filtro por proximidad al océano
    ocean_proximity = st.sidebar.multiselect(
        "Proximidad al océano",
        options=df['ocean_proximity'].unique(),
        default=df['ocean_proximity'].unique()
    )

    # Variable para el tamaño de los círculos
    tamaño_variable = st.radio(
        "Tamaño de los círculos por:",
        options=["Habitaciones/Hogar", "Valor de la Vivienda", "Población/Hogar", "Edad de la Vivienda"]
    )

    # Filtrar el DataFrame
    df_filtrado = df[
        (df['median_house_value'] >= valor_min_raw) & (df['median_house_value'] <= valor_max_raw) &
        (df['poblacion_por_hogar'] >= poblacion_min) & (df['poblacion_por_hogar'] <= poblacion_max) &
        (df['housing_median_age'] >= edad_min) & (df['housing_median_age'] <= edad_max) &
        (df['ocean_proximity'].isin(ocean_proximity))
    ]

    # Mapa de puntos mejorado con clustering
    st.subheader("Mapa de Viviendas")
    mapa = folium.Map()
    marker_cluster = MarkerCluster().add_to(mapa)

    for index, row in df_filtrado.iterrows():
        if tamaño_variable == "Habitaciones/Hogar":
            tamaño = row['habitaciones_por_hogar_normalizado'] * 100
            popup_text = f"Valor: ${formatear_miles(row['median_house_value'])}, Habitaciones/Hogar: {row['habitaciones_por_hogar']:.2f}, Población/Hogar: {row['poblacion_por_hogar']:.2f}, Edad: {row['housing_median_age']}"
        elif tamaño_variable == "Valor de la Vivienda":
            tamaño = row['median_house_value'] / df_filtrado['median_house_value'].max() * 100
            popup_text = f"Valor: ${formatear_miles(row['median_house_value'])}, Habitaciones/Hogar: {row['habitaciones_por_hogar']:.2f}, Población/Hogar: {row['poblacion_por_hogar']:.2f}, Edad: {row['housing_median_age']}"
        elif tamaño_variable == "Población/Hogar":
            tamaño = row['poblacion_por_hogar'] / df_filtrado['poblacion_por_hogar'].max() * 100
            popup_text = f"Valor: ${formatear_miles(row['median_house_value'])}, Habitaciones/Hogar: {row['habitaciones_por_hogar']:.2f}, Población/Hogar: {row['poblacion_por_hogar']:.2f}, Edad: {row['housing_median_age']}"
        else:  # Edad de la Vivienda
            tamaño = row['housing_median_age'] / df_filtrado['housing_median_age'].max() * 100
            popup_text = f"Valor: ${formatear_miles(row['median_house_value'])}, Habitaciones/Hogar: {row['habitaciones_por_hogar']:.2f}, Población/Hogar: {row['poblacion_por_hogar']:.2f}, Edad: {row['housing_median_age']}"

        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=tamaño,
            popup=popup_text,
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        ).add_to(marker_cluster)

    # Ajustar el zoom del mapa a los límites de los datos
    mapa.fit_bounds([[df_filtrado['latitude'].min(), df_filtrado['longitude'].min()], [df_filtrado['latitude'].max(), df_filtrado['longitude'].max()]])

    st_folium(mapa, width=700, height=500)

    # Mostrar datos filtrados
    st.subheader(f"Datos Filtrados ({len(df_filtrado)} filas)") # se agrega el numero de filas
    st.write(df_filtrado)
else:
    st.write("Por favor, sube un archivo CSV para comenzar.")