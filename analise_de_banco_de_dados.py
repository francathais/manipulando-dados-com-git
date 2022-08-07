# -*- coding: utf-8 -*-
"""Analise de banco de dados

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/francathais/23b8ee9d8d31f9330924881efa9ba481/reconquistando-o-python.ipynb

```
# Isto está formatado como código
```

#Analise de banco de dados
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pip install plotly

from google.colab import files
uploaded = files.upload()

import pandas as pd 
import io

#Chamando pelo nome o arquivo: lista  
lista = pd.read_csv(io.BytesIO(uploaded['planodesaude.csv']))
#mostrar lista 
print(lista)

#conhecendo quantidade de inhas e colunas
lista.shape

#informações
lista.info()

#descrevendo banco de dados
lista.describe()

lista['State']

lista["Kilograms"]

kilos_estado=lista[["Gender", "State", "Kilograms"]].groupby(["Gender","State"]).sum()
print(kilos_estado) #Comparando kilogramas homens e mulheres por estado

kilos_estado=lista[["Gender", "Kilograms"]].groupby("Gender").sum()
print(kilos_estado)

kilos_estado.plot(kind="bar")
#nome
plt.title("Gráfico de kilos, separado por gênero")
#eixos
plt.xlabel("Gênero")
plt.ylabel("Kilos")
#mostra
plt.show()

kilos_estado.groupby("Gender").mean()

kilinhos=lista["Kilograms"]
print(kilinhos)

print(sum(kilinhos)) #soma

print(max(kilinhos)) #maxima

print(min(kilinhos)) #minima

print(sum(kilinhos)/len(kilinhos)) #média

#plt.scatter(lista['Age'],lista['Kilograms'])
#nome
#plt.title("Gráfico de Kilogramas")
#eixos
#plt.xlabel("Kilogramas")
#plt.ylabel("Frequência")
#plt.xticks(rotation=50)
#plt.yticks(rotation=45)
#mostra
#plt.show()

"""#gráfico de frequência com título e eixos"""

#gerar
plt.hist(lista['State'])
#nome
plt.title("Habitante por estado nacional")
#eixos
plt.xlabel("Estado")
plt.ylabel("Frequência")
#mostra
plt.show()

"""#Filtrando váriavel na tabela"""

lista['Color']  #filtrando apenas Color

#gerar
plt.hist(lista['Color'])
#nome
plt.title("Frequência das cores")
#eixos
plt.xlabel("Cores")
plt.ylabel("Frequência")
#mostra
plt.show()



"""#Cores disponíveis: Green, Blue, Black, White, Orange, Purple,Silver, Red, Brown



"""

lista['Age'] #filtrando apenas Age

#gerar
plt.hist(lista['Age'])
#nome
plt.title("Frequência de idade")
#eixos
plt.xlabel("Idade")
plt.ylabel("Frequência")
#mostra
plt.show()

"""#Formas de pesquisar informação na tabela"""

lista.loc[[0]] #localizando pessoa 0

lista.loc[[0,3]] #localizando pessoa 0 e 3

lista.loc[0:3] #localizando pessoa do 0 ao 3

"""#Filtrando pessoas de São Paulo"""

lista.loc[ lista['State']=='SP'] #localizando só pessoas de SP

"""#Criando dataframe só com SP e usando loc

"""

SP=lista.loc[lista['State']=='SP'] #criando dataframe

print(SP) #mostra

# exemplo de gráfico de linha de Color, caso fosse um ados contínuos, ou seja, que não podem ser contados em números inteiros
# Código: plt.plot(lista["Color"])
# plt.show

plt.hist(lista["Age"])
#nome
plt.title("Idade")
#eixos
plt.xlabel("Idade")
plt.ylabel("Frequência")
#mostra
plt.show()

#Top>Down qual o valor mais utilizado

plt.hist(lista["Valor"])
plt.ylim(10, 30)
#plt.yscale('log')
plt.show

escolha_de_valores=lista[["Valor"]].groupby(["Valor"]).sum()
print(escolha_de_valores)

idade=lista["Age"]
print(idade)

print(sum(idade)) #soma

print(max(idade)) #maxima

print(min(idade)) #minima

print(sum(idade)/len(idade)) #média

valores=lista["Valor"]
print(valores)



"""#Valor pago por sexo"""

valor_por_sexo=lista[["Gender", "Valor"]]  #ver tabela de sexo por valor pago
print(valor_por_sexo)

valor_por_sexo=lista[["Gender", "Valor"]].groupby("Gender").sum()
#calculando diferença de valor pago por homem e mulheres, agrupando os dados female/male
print(valor_por_sexo)

valor_por_sexo.plot(kind="bar")
#nome
plt.title("Valor pago por gênero")
#eixos
plt.xlabel("Gênero")
plt.ylabel("Valor pago")
#mostra
plt.show()

valor_por_estado=lista[["Gender", "State", "Valor"]].groupby(["Gender","State"]).sum()
print(valor_por_estado) #Comparando o valor pago por homens e mulheres por estado

valor_por_estado.groupby("Gender").median()

valor_por_estado.plot(kind="bar")
#nome
plt.title("Valor pago, separado por gênero, com estado de residência")
#eixos
plt.xlabel("Gênero e Estado")
plt.ylabel("Valor pago")
#mostra
plt.show()

valor_por_estado.query('Gender=="female"')
#filtrando female de valor_por_estado

valor_por_estado1=valor_por_estado.query('Gender=="female"')
print(valor_por_estado1)

valor_por_estado1.plot(kind="bar")
#nome
plt.title("Valor pago, gênero feminino, com estado de residência")
#eixos
plt.xlabel("Gênero e Estado")
plt.ylabel("Valor pago")
#mostra
plt.show()

valor_por_estado.query('Gender=="male"')

valor_por_estado2=valor_por_estado.query('Gender=="male"')
print(valor_por_estado1)

valor_por_estado2.plot(kind="bar")
#nome
plt.title("Valor pago, gêreno masculino, com estado de residência")
#eixos
plt.xlabel("Gênero e Estado")
plt.ylabel("Valor pago")
#mostra
plt.show()

"""#Extraindo por gênero (localizando)
#Depois, criando dataframe

"""

lista.loc[ lista['Gender']=='female'] #localizando só pessoas de SP

female=lista.loc[lista['Gender']=='female'] #criando dataframe
print(female)

analise=lista[["Gender", "Valor"]] #criei dataframe
print(analise)

lista.plot

#teste lista.plot(kind='hist')

#exemplo grafico de linha: plt.plot(lista['Valor'], lista["Color"])