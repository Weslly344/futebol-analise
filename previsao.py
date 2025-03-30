import streamlit as st
import pandas as pd
import numpy as np

# URL do Google Sheets com os dados
URL_PLANILHA = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTyccDH9AtZAbTyyb5hbTgs791s4nh7OZv6aK5zVsIHgXvKVzFsVtVhmTQAGhAKUVRWxNXzU8xHi22u/pubhtml"

@st.cache_data
def carregar_dados():
    df = pd.read_csv(URL_PLANILHA)
    return df

def calcular_probabilidades(df):
    # Simulação de probabilidades básicas
    df["Probabilidade Vitória Casa"] = np.random.uniform(30, 70, size=len(df))
    df["Probabilidade Empate"] = np.random.uniform(10, 40, size=len(df))
    df["Probabilidade Vitória Visitante"] = 100 - (df["Probabilidade Vitória Casa"] + df["Probabilidade Empate"])
    
    df["Probabilidade +2.5 Gols"] = np.random.uniform(40, 80, size=len(df))
    df["Probabilidade -2.5 Gols"] = 100 - df["Probabilidade +2.5 Gols"]

    return df

st.title("🔮 Probabilidades de Jogos de Futebol")

df = carregar_dados()
df = calcular_probabilidades(df)

st.dataframe(df[["Time Casa", "Time Visitante", "Probabilidade Vitória Casa", "Probabilidade Empate", "Probabilidade Vitória Visitante", "Probabilidade +2.5 Gols", "Probabilidade -2.5 Gols"]])

st.bar_chart(df[["Probabilidade Vitória Casa", "Probabilidade Empate", "Probabilidade Vitória Visitante"]])
