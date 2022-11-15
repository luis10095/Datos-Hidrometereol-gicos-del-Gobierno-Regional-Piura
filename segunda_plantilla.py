import streamlit as st
import pandas as pd
import numpy as np
import urllib.request

st.title('Datos Hidrometereológicos del Gobierno Regional Piura')

#@st.experimental_memo #@staticmethod
#def download_data():
#	url = 'https://www.datosabiertos.gob.pe/node/10105/download'
#	filename = 'datos_piura.csv'
#	urllib.request.urlretrieve(url, filename)

#download_data()

#crear un funcion para leer dataset
def leer_dataset(filename):
	'''funcion para leer datasets'''
	df = pd.read_csv(filename)
	return df 

dt1 = leer_dataset('https://www.datosabiertos.gob.pe/node/10105/download')

#informacion del dataset
st.markdown('''
	Este dataset muestra los datos hidrometereológicos registrados de las presas, estaciones hidrológicas e hidrométricas.
	- **Base de Datos:** (https://www.datosabiertos.gob.pe/node/10105/download)''')

#nombre del dataset
st.header('Dataset Hidrometereológico')
#grafica el dataset
st.dataframe(dt1)

#estadisticas del dataset
st.header('Estadisticas del dataset')
st.dataframe(dt1.describe())

#selectbox de tipo de estaciones 
lista_tipo_estacion = []
for elem in dt1['TIPO_ESTACION'].unique():
  lista_tipo_estacion.append(elem)

st.header('Evaluacion hidrometereológica por tipo de estaciones')
#mostrar las opciones
op1 = st.selectbox('Evaluacion de datos hidrometereológicos por tipo de estacion', tuple(sorted(lista_tipo_estacion)))
st.write('Tipo de estacion seleccionada:', op1)

#selectbox de departamento/provincia/distrito
lista_ubicacion = []
for item in dt1['PROVINCIA'].unique():
	for comp in dt1['DISTRITO'].unique():
		lista_ubicacion.append('PIURA' + '/' + item.upper() + '/' + comp.upper())

st.header('Evaluacion hidrometereológica por departamento/provincia/distrito')
#mostrar las opciones
op2 = st.selectbox('Evaluacion de datos hidrometereológicos por ubicacion', tuple(sorted(lista_ubicacion)))
st.write('Ubicacion seleccionada:', op2)

