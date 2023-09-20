'''soma de todos elementos pares'''

def ehPar(n):
    r = (n%2==0) #funcão para verificar se é par
    return r

def soma_par(lst):
    soma=0
    for num in  lst:
        if(ehPar(num)):
            soma=soma+num
    return soma

lista = [10,2,5,7,6,3]
soma=soma_par(lista)
print(f'O somatório dos elementos paresda lista é: {soma}')