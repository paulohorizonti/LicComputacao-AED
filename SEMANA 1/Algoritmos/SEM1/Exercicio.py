#Exercícios semana 1 - AED - 3 PERIODODO - LICENCIATURA EM COMPUTAÇÃO - UFT - ARAGUAÍNA - TO
# Autor: PAULO ROBERTO NOGUEIRA


#lista de frutas
fruits = ['ORANGE','APPLE','PEAR','BANANA', 'KIWI','APPLE', 'BANANA']

#mostra a lista
print(fruits)
#Contar quantas vezes determinado elemento aparece
fruits.count('APPLE')

#Contar quantas vezes determinado elemento aparece
fruits.count('TANGERINE')

#Verifica o indice da baanana
fruits.index('BANANA')

#tenta encontar o indice a partir do indice 4, inclundo o 4
fruits.index('BANANA',4)

#lista o indice da banana a partir do indice 4
print(fruits.index('BANANA',4))

#Adiciona ao fim da lista
fruits.append('GRAPE')

#Insere no indice 2 o melon
fruits.insert(2,'MELON')

#mostra a lista
print(fruits)