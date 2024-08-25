import streamlit as st
from random import choice

st.set_page_config(page_title="War", page_icon="🎲", layout="centered")

# Função para rolar os dados
def rola_dados(dado, quantos):
    resultados = []
    for _ in range(quantos):
        resultados.append(choice(dado))
    return resultados

# Define os dados
d4 = list(range(1, 5))
d6 = list(range(1, 7))
d8 = list(range(1, 9))
d10 = list(range(1, 11))
d12 = list(range(1, 13))
d20 = list(range(1, 21))

rolagem = 0

# Sacola de dados para escolha no Streamlit
sacola_de_dados = {
    "D4": d4,
    "D6": d6,
    "D8": d8,
    "D10": d10,
    "D12": d12,
    "D20": d20
}

# Quantidade de dados que o usuário pode escolher
quantos_dados = [1, 2, 3]

# Inputs
with st.sidebar:
    tipo_dado = st.radio("Escolha o tipo de dado:", list(sacola_de_dados.keys()))
    quantos = st.radio("Quantos dados?", quantos_dados)
    
    if st.button('Rolar os dados'):
        dado_selecionado = sacola_de_dados[tipo_dado]
        rolagem = rola_dados(dado_selecionado, quantos)
        st.write(f"Resultados das rolagens: {rolagem}")

# Outputs
if rolagem != 0:
    st.markdown(f"### Resultados das rolagens: {rolagem}")
