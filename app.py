import streamlit as st
import requests

def converter_moeda(valor, moeda_origem, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    dados = response.json()
    taxa = dados["rates"].get(moeda_destino)

    if taxa is None:
        return None

    return valor * taxa

st.set_page_config(page_title="Conversor de Moedas", page_icon="💱")

st.title("💱 Conversor de Moedas")

valor = st.number_input("Digite o valor:", min_value=0.0, step=1.0)

moeda_origem = st.selectbox(
    "Moeda de origem:",
    ["USD", "BRL", "EUR"]
)

moeda_destino = st.selectbox(
    "Moeda de destino:",
    ["USD", "BRL", "EUR"]
)

if st.button("Converter"):
    resultado = converter_moeda(valor, moeda_origem, moeda_destino)

    if resultado is None:
        st.error("Erro ao converter. Tente novamente.")
    else:
        st.success(f"Valor convertido: {resultado:.2f} {moeda_destino}")