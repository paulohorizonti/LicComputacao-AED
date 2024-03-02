#Criar a lista
listNum = [75,93,25,17,42, "PATO", 93, 93]

#Imprimiar a lista
print(listNum)

#Adicionar um elemento a lista
listNum.append(100)
listNum.append(150)
listNum.append(95)

#listar novamente
print(listNum)

#inserrir em uma determinda posição
listNum.insert(3,43)
listNum.insert(4,'MACACO')

#listar novamente
print(listNum)

#Retonar o tamanho da lista
print('São {} elementos na lista'.format(len(listNum)))

#Remove o elemento da lista
listNum.remove(43)

#listar novamente
print(listNum)

#Retonar o tamanho da lista
print('Depois da remoção são [{}] elementos na lista'.format(len(listNum)))

#quantas vezes determinado elemento aparece
print('O elemento 93 aparece [{}] vezes na lista'.format(listNum.count(93)))

#Retonna o indece do elemento informado, erro se O ELEMENTO INFORMADO nao existir
print('O indice do elemento 25 é [{}]'.format(listNum.index(25)))

# ----- COMANDO FORA DA APOSTILA --------
#Exemplo de try catch para que quando der erro de nao encontrar o indice do numero em questao o sistema retornar um erro mais amigavel
try:
    print('O indice do elemento 25 é [{}]'.format(listNum.index(22)))
except:
    print('O ELEMENTO INFORMADO NÃO EXISTE NA LISTA')
