import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Vehicle Health Monitor & Fault Predictor")

@st.cache_data
def load_data():
    return pd.read_csv("data/vehicle_sensor_data.csv")

df = load_data()

if st.checkbox("Mostrar dados brutos"):
    st.write(df.head())

st.subheader("Estatísticas Gerais")
st.write(df.describe())

st.subheader("Distribuições")
fig, ax = plt.subplots(figsize=(10, 6))
df.hist(ax=ax, bins=30, layout=(2, 3), figsize=(10,6))
st.pyplot(fig)

st.subheader("Matriz de Correlação")
fig_corr, ax_corr = plt.subplots(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax_corr)
st.pyplot(fig_corr)
