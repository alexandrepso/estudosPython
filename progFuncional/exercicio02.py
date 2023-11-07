#considere a lista abaixo:

#lista = [0,1,1,2,3,5,8,13,21,34]

#implementar uma solução de programação funcional para imprimir apenas os pares.

lista = [0,1,1,2,3,5,8,13,21,34]

f_pares = list(filter(lambda x: x % 2 == 0, lista))      #minha implementação

print(f_pares)


#lista = [0,1,1,2,3,5,8,13,21,34]

#ftesteParidade = lambda x: x % 2 == 0

#print(f'teste de ftesteParidade (5) = {ftesteParidade (5)} ')

#pares = list(filter(ftesteParidade, lista))

#print(f'lista de numeros pares  = {pares}')