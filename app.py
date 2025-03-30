import streamlit as st
import pandas as pd

# URL do Google Sheets com os dados
URL_PLANILHA = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTyccDH9AtZAbTyyb5hbTgs791s4nh7OZv6aK5zVsIHgXvKVzFsVtVhmTQAGhAKUVRWxNXzU8xHi22u/pub?output=csv"

@st.cache_data
def carregar_dados():
    df = pd.read_csv(https://docs.google.com/spreadsheets/d/e/2PACX-1vTyccDH9AtZAbTyyb5hbTgs791s4nh7OZv6aK5zVsIHgXvKVzFsVtVhmTQAGhAKUVRWxNXzU8xHi22u/pub?output=csv)
    return df

st.title("📊 Análise de Jogos de Futebol")

df = carregar_dados()

st.dataframe(df)

st.bar_chart(df[["Placar Casa", "Placar Visitante"]])
