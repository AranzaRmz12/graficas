# Importamos la biblioteca streamlit
import streamlit as st
import pandas as pd

# Creamos el título de la App
st.title("Titanic App")
st.header("Demo titanic app")
st.write("Gráficas del titanic")

# Comando para correr: python -m streamlit run hola.py

# Leemos el dataset de Titanic y lo ponemos en un dataframe
titanic_link = "titanic.csv"
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)