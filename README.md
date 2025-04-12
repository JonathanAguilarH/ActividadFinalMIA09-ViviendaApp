
# Visualización Interactiva de Datos de Vivienda 🏠

Este proyecto es una aplicación web interactiva desarrollada con **Streamlit**, que permite visualizar y explorar datos de viviendas mediante filtros dinámicos y mapas interactivos. Es ideal para realizar análisis exploratorio de datos de viviendas con geolocalización, valores promedio, edad, población, entre otros.

## 📁 Contenido del Repositorio

- `valorcasa.py`: Script principal de la aplicación.
- `README.md`: Este archivo con instrucciones para la instalación y ejecución.

## 🚀 Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instalado lo siguiente:

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### 📦 Bibliotecas necesarias

Instala las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

Si no cuentas con un archivo `requirements.txt`, puedes instalar las dependencias directamente con:

```bash
pip install streamlit pandas folium streamlit-folium scikit-learn
```

## ▶️ Ejecución de la Aplicación

1. Clona este repositorio o descarga los archivos manualmente:

```bash
git clone https://github.com/tu-usuario/nombre-repo.git
cd nombre-repo
```

2. Ejecuta la aplicación con el siguiente comando:

```bash
streamlit run valorcasa.py
```

3. Se abrirá una nueva pestaña en tu navegador predeterminado con la aplicación.

## 📝 Instrucciones de Uso

1. Sube un archivo `.csv` con los datos de viviendas. El archivo debe incluir las siguientes columnas:

   - `latitude`
   - `longitude`
   - `median_house_value`
   - `population`
   - `households`
   - `total_rooms`
   - `housing_median_age`
   - `ocean_proximity`

2. Utiliza la barra lateral izquierda para:

   - Filtrar por rango de valores de vivienda.
   - Seleccionar la densidad de población por hogar.
   - Ajustar la edad media de la vivienda.
   - Filtrar por proximidad al océano.
   - Elegir el atributo que define el tamaño de los círculos del mapa.

3. Visualiza las viviendas en un mapa interactivo con agrupamiento (cluster) y explora los detalles emergentes.

4. Consulta los datos filtrados directamente en la interfaz.

## 🌍 Funcionalidades Principales

- 📊 Filtros dinámicos para análisis personalizado.
- 📌 Mapa interactivo con markers agrupados (MarkerCluster).
- 🧠 Normalización de datos para mejor representación.
- 📈 Visualización del DataFrame filtrado.
- 🖱️ Interfaz intuitiva con Streamlit.

## 🧪 Ejemplo de Datos

Puedes utilizar el dataset de California Housing disponible en [Kaggle](https://www.kaggle.com/datasets/camnugent/california-housing-prices) o cualquier otro archivo `.csv` con la estructura mencionada anteriormente.

## 📬 Contacto

Para dudas o sugerencias, contacta al autor del repositorio a través de GitHub o correo electrónico.

---

¡Disfruta explorando los datos de vivienda! 🏡📍
