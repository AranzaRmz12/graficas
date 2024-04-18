# Importamos la biblioteca streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Creamos el título de la App
st.title("Titanic App")
st.header("Aranza Ramírez Mora")
st.write("Gráficas del titanic")

# Comando para correr: python -m streamlit run hola.py

# Leemos el dataset de Titanic y lo ponemos en un dataframe
titanic_link = "titanic.csv"
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)

fig, ax = plt.subplots()
ax.hist(titanic_data["Fare"])
st.header("Histograma del Titanic")
st.pyplot(fig)