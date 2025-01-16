# Python Insights - Analisando Dados com Python
# Case - Cancelamento de Clientes
# Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.

# Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.

# 1. Importar a Base de Dados
# 2. Resolver problemas de dados não existentes
# 3. Tratamento de Dados
# 4. Criação de Gráficos dos Cancelamentos
# 5. Mostrar soluções para os Problemas

# 1. Importar a Base de Dados
import pandas as pd

# Importando o CSV para a variável tabela
tabela = pd.read_csv("cancelamentos.csv")

print(tabela)

# 2. Resolver problemas de dados não existentes "nan"

# .info() -> Exibir informações sobre a variável que armazena o CSV.
print(tabela.info())

# Na situação atual, e necessário entender se podemos excluir aqueles que estão
# faltando dados, pois caso o número seja pequeno, será algo irrelevante.

# .dropna() -> Irá remover as linhas nas quais estão faltando dados "nan".
tabela = tabela.dropna()

print(tabela.info())

# 3. Tratamento de Dados

print(tabela)

# Nesse ponto é necessário analisar quais os dados serão relevantes para a nossa
# análise, pois isso irá ocupar menos espaço, além de evitar dados
# desnecessários.

# .Drop() -> remover linhas ou colunas de uma tabela de dados
tabela = tabela.drop(columns=["CustomerID"])

# Nessa situação, o CustomerID é algo desnecessário, já que é apenas um número 
# de identificação de usuário, e não algo que possa impactar nos cancelamentos. 

print(tabela)

# 4. Criação de Gráficos dos Cancelamentos

# .value_counts() -> Realiza contagem de elementos presente em uma parte da 
# lista que o usuário passar.
# normalize=True -> Retornar em forma percentual.
print(tabela["cancelou"].value_counts(normalize=True))

# Até aqui seria possível realizar a análise desse dados, mas fazendo gráfico
# fica mais fácil sua visualização.

# Biblioteca responsável por gerar gráficos no python.
import plotly.express as px

# .bar() -> Criar Gráfico de Barras.
# data_frame -> Tabela a ser passado.
# x -> Qual parte será utilizado "no caso duracao_contrato".
# text_auto -> Exibir o rótulo dos dados.
grafico = px.histogram(data_frame=tabela, x="duracao_contrato", color="cancelou", text_auto=True)

# .show() -> Realizar exibição do gráfico.
grafico.show()
# Percebesse que agora é uma forma de visualizar melhor os dados.

for columns in tabela.columns:
  grafico = px.histogram(data_frame=tabela, x=columns, color="cancelou", text_auto=True)
  grafico.show()

  # Atráves de um laço for, foi capaz de gerar gráficos de todas as colunas,
  # o que irá facilitar a análise e entender o porque está havendo muitos
  # cancelamentos.

# 5. Mostrar soluções para os Problemas

# Agora é pensar o por que está havendo tantos cancelamentos.

# 1. Dias de interação -> Acima do dia 15 as assinaturas foram canceladas.

# 2. Gastos Totais -> Abaixo de R$ 497 em gasto total, teve todas as assinaturas
# canceladas.

# 3. Duração de Contratos -> Contratos mensais tiveram todas as assinaturas
# canceladas.

# 4. Atraso -> Acima do dia 20 nos atrasos do pagamento, todas as assinaturas
# canceladas.

# 5. Ligações -> Acima de 3 Ligações, tiveram um aumento exagerado na taxa de 
# cancelamento.

# 6. Sexo -> O sexo feminino tem mais cancelamentos do que assinantes.

# 7. Idade -> Acima de 50 anos, todas as assinaturas canceladas.


# Como visto, muitas das coisas que impactaram o cancelamento não tem oque fazer,
# como idade, gasto totais, mas outras coisas sim, como: 

# 1. Dias de interação -> Notificar o usuário, e trazer ele de volta para 
# interagir.

# 3. Duração de Contratos -> Dar descontos em assinaturas com maior duração.

# 4. Atraso -> Ligar para as pessoas que estão atrasos a partir do dia 15 por
# exemplo.

# 5. Ligações -> Listar as pessoas que mais ligaram ao callsenter, e colocar elas
# em urgencia.

# 5. Mostrar soluções para os Problemas

# Para isso iremos filtrar esse dados, assim fazendo uma simulação na quantidade
# de cancelamentos antes e depois.

# Metódo de filtragem, na qual passamos a condição dentro do colchetes
# Nesse caso iremos remover os valores que mostram a taxa de cancelamento,
# simulando o resultado caso convertemos esse cancelamentos em assinatura
tabela = tabela[tabela["frequencia_uso"]<=15]
tabela = tabela[tabela["ligacoes_callcenter"]<=3]
tabela = tabela[tabela["dias_atraso"]<= 15]
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]

print(tabela["cancelou"].value_counts(normalize=True))

# Percebesse que o valor inicial era de aproximadamente 57% de cancelamentos, e
# que após as soluções caiu para aproximadamente 18%