import streamlit as st
import pandas as pd

# criando uma série
s1 = pd.Series(["🥇 Lindemberg", "🥈 César", "🥉 Cezimar"], index= [1, 2, 3], name="Ranking") # isto é uma série do pandas (que recebe o nome de "Flores como parâmetro"), que nada mais é que uma coluna com índice (o índice está personalizado de 1 a 4)
s2 = pd.Series([9, 7, 5], index= [1, 2, 3], name="Pontos")

# criando um DataFrame a partir de uma ou mais séries
df_placar = pd.DataFrame([s1,s2])
df_placar = df_placar.T

# configuração1
st.set_page_config(page_title="War ", page_icon="🎲", layout="centered")



# título

st.html("<img src='https://i.pinimg.com/564x/25/cd/d4/25cdd4a1905f515995a57df6e3737b8e.jpg' alt='dados'>")




# tabela

st.dataframe(df_placar)
st.markdown("""
            *"Você precisa levar o oponente até uma floresta escura e profunda na qual 2+2 = 5 é o único caminho que leva à saída e que só tem espaço para um."*
            -- Mikhail Tal - Grande Mestre de Xadrez
            """)
