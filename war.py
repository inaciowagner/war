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
# Manual de Regras 
st.markdown('''
1. Cada jogador pega um dado e o lança. Aquele que obtiver o ponto mais alto será o dis- tribuidor, cabendo-lhe a tarefa de separar as 12 cartas dos Centros Estratégicos, embaralhá-las e distribuí-las, uma a uma, a todos os participantes, começando por si próprio e seguindo pelo jo-

gador à sua esquerda. Após a distribuição, os jogadores colocam 2 exércitos em cada um dos Centros Estratégicos

recebidos.

NOTA: Algumas cartas possuem mais de 1 território, mas as peças devem ser colocadas apenas no que possui o sinal de Centro Estratégico.

Distribuição para 5 jogadores:

Nesse caso, distribuem-se inicialmente apenas 10 cartas de CE (2 para cada um). Os jogadores colocam então no tabuleiro os exércitos a que tiverem direito, da forma acima descrita.

Em seguida cada jogador, na sua vez, pode optar: a) Por uma das duas cartas de CE restantes, colocando 2 exércitos no território correspondente. b) Por dois territórios quaisquer, desde que já não estejam ocupados, não sejam Centros Estraté- gicos e não sejam ambos no mesmo continente, colocando apenas um exército em cada um deles.

O jogador, na sua vez, poderá não ter opções. Isso acontece quando não existirem mais cartas de CE, restando somente a opção "b", ou quan- do três outros jogadores já tiverem optado pela escolha de 2 territórios, restando somente a op- ção "a".

Terminada esta fase, as cartas devem ser novamente embaralhadas com as 49 restantes do ma- ço (cartas de números e territórios) e colocadas com a face para baixo em uma área livre do ta- buleiro. Feito isto, o distribuidor coloca um exército em um território vago à sua escolha, seguido pelo jogador que está à sua esquerda e assim sucessivamente. Esse processo deve ser repetido até que todos os territórios estejam ocupados.

OBJETIVOS

Em seguida a distribuição dos exércitos e dos territórios, é feito o sorteio dos objetivos, receben- do cada jogador 1 objetivo dentre os 20 existentes, tomando conhecimento do seu teor e evitan- do revela-lo aos seus adversários. É recomendado aos jogadores que estão se iniciando no jogo que, antes do sorteio, seja feita

uma leitura de todos os objetivos possíveis.

OBS. 1: No caso do número de jogadores ser inferior a 6, os objetivos relacionados com os exér-

citos não participantes devem ser excluídos do sorteio.

OBS. 2: Se algum jogador, no transcorrer do jogo, ficar reduzido a 1 único território, seu objetivo passa automaticamente a ser conquistar três Centros Estratégicos quaisquer.

4-0 JOGO

Inicia o jogo o participante seguinte ao que ocupou o último território na distribuição dos territórios.

Primeira Rodada:

a) Todos os jogadores, cada um na sua vez, colocam sobre o tabuleiro as peças - exércitos e bom- bardeiros a que têm direito (pelo número de territórios, número de CE, maiorias e totalida- des dos continentes). b) A seguir, cada jogador, na sua vez, se desejar ataca seus adversários, desloca seus exércitos

A primeira rodada consiste em 2 etapas:

se houver conveniência e recebe cartas se fizer jus a isso. (Estas etapas estão detalhadas adiante). Segunda rodada em diante:

partir da segunda rodada cada jogador na sua vez, sem esperar a colocação das peças dos ad- A versários, joga obedecendo as seguintes etapas nesta ordem:

a) Recebe novos exércitos e os coloca no tabuleiro de acordo com a sua estratégia (em territórios que já lhe pertencem);

b) Recebe bombardeiros e os coloca na sua base aérea;

d) Desloca seus exércitos se houver conveniência; e

e) Recebe cartas se fizer jus a isto. (Para receber cartas é necessário a conquista de pelo menos

c) Se desejar, ataca os adversários;

OBS. 1. A diferença entre a primeira rodada e as subseqüentes se justifica a fim de equilibrar as forças no início do jogo.

2

um território).

OBS

. 2: Cada fase do jogo está explicada detalhadamente nos itens a segui. Quando houver dúvida sobre alguma destas fases, leia novamente a seção correspon-

3
''')