#considere a lista abaixo:

# numero = [1,2,3,4,5,6,7,8,9,10]

# Implemente uma solução através de programação funcional para somar todos os elementos da lista.

numero = [1,2,3,4,5,6,7,8,9,10]
                                   # minha implementação 

numero = sum(numero)
print(numero)

##################################################################################################

from functools import reduce

f_soma = lambda x,y :x + y

numero = [1,2,3,4,5,6,7,8,9,10]

resultado = reduce(f_soma,numero)

print(resultado)


