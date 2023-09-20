#calcular o fatorial de um numero

def fatorial_interativo(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def fatorial_recursivo(n):
    if((n==0)or(n==1)):
        return 1
    return n*fatorial_recursivo(n-1)

numero = 5
print(f'O fatorial de {numero} é: {fatorial_interativo(numero)}')
print(f'O fatorial de {numero} é: {fatorial_recursivo(numero)}')
