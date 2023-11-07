#considere a lista abaixo:

#lista_numeros = [9.56783,7.57568,3.009914,6.2321]
#lista_precisao = [2,2,3,3]

#Implemetar uma solução atraves de programação funcional para arrendondar os 
# valores da lista de números na mesma ordem da lista precisão.

lista_numeros = [9.56783,7.57568,3.009914,6.2321]

lista_precisao = [2,2,3,3]

arredondamento = lambda x,y:round(x,y)

resultado = list(map(arredondamento,lista_numeros,lista_precisao))

print(resultado)