import streamlit as st
import pandas as pd
from random import choice

# criando uma série
s1 = pd.Series(["🥇 Lindemberg", "🥈 César", "🥉 Cezimar"], index= [1, 2, 3], name="Ranking") # isto é uma série do pandas (que recebe o nome de "Flores como parâmetro"), que nada mais é que uma coluna com índice (o índice está personalizado de 1 a 4)
s2 = pd.Series([9, 7, 5], index= [1, 2, 3], name="Pontos")

# criando um DataFrame a partir de uma ou mais séries
df_placar = pd.DataFrame([s1,s2])
df_placar = df_placar.T

# configuração1
st.set_page_config(page_title="War", initial_sidebar_state="expanded", page_icon="🎲", layout="centered")



# título

st.html("<img src='https://i.pinimg.com/564x/25/cd/d4/25cdd4a1905f515995a57df6e3737b8e.jpg' alt='dados' width='90%'>")




# tabela

st.dataframe(df_placar)
st.html("<hr/>")
st.bar_chart(df_placar, y="Pontos", x="Ranking")
st.markdown("""
            *"Você precisa levar o oponente até uma floresta escura e profunda na qual 2+2 = 5 é o único caminho que leva à saída e que só tem espaço para um."*
            -- Mikhail Tal - Grande Mestre de Xadrez
            """)




# Função para rolar os dados
def rola_dados(dado, quantos):
    resultados = []
    for _ in range(quantos):
        resultados.append(choice(dado))
    return resultados

# Define os dados
#d4 = list(range(1, 5))
d6 = list(range(1, 7))
d8 = list(range(1, 9))
#d10 = list(range(1, 11))
#d12 = list(range(1, 13))
#d20 = list(range(1, 21))
avioes = [0, 0, 0, 1, 2, 3]

rolagem = 0

# Sacola de dados para escolha no Streamlit
#sacola_de_dados = {"D4": d4, "D6": d6, "D8": d8, "D10": d10, "D12": d12, "D20": d20, "Ataque/Defesa Aérea": avioes}

sacola_de_dados = {
    "D6": d6,
    "D8": d8,
    "Ataque/Defesa Aérea": avioes
}


# Quantidade de dados que o usuário pode escolher
quantos_dados = [1, 2, 3]

# Inputs
with st.sidebar:
    st.html("<h2>Dados Simulator Tabajara</h2>")
    tipo_dado = st.radio("Escolha o tipo de dado:", list(sacola_de_dados.keys()))
    quantos = st.radio("Quantos dados?", quantos_dados)
    
    if st.button('Rolar os dados'):
        dado_selecionado = sacola_de_dados[tipo_dado]
        rolagem = rola_dados(dado_selecionado, quantos)
        st.html(f"<h3>Resultados das rolagens: {rolagem}</h3>")

# Outputs
#if rolagem != 0:
#    st.markdown(f"### Resultados das rolagens: {rolagem}")

st.markdown('''
# RESUMO DE REGRA

> A partir da segunda rodada, cada jogador, na sua vez, cumpre as seguintes etapas:

1) Recebe novos exércitos

* em função dos territórios possuidos

* em função dos CE's possuídos

* se possuir um continente inteiro, de acordo com a TABELA

* em função da troca de cartas

2) Coloca esses exércitos no tabuleiro

* de acordo com sua estratégia

3) Recebe aviões

* em função dos CE's possuídos, e os coloca em sua base aérea

* em função da troca de cartas (para efetuar ataques)

4) Efetua seus ataques terrestres e aéreos

* se desejar

5) Recebe uma carta de território

* se conquistar no mínimo um território (o número de cartas em sua mão NÃO pode exceder 5 cartas).
''')