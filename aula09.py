'''determinar se um numero é primo ou não'''



def eh_primo(n):
    if(n<2):
        return false
    i=n//2
    while(i>1):
        if(n%i==0):
            return false
        i=i-1
    return true




def imprimir_resultado(numero,resultado):
    mensagem= f'O numero {numero} Não é primo'
    if(resultado):
        mensagem= f' o número {numero} É primo'
    return mensagem

numero = 7
resultado=eh_primo(numero)
msg=imprimir_resultado(numero,resultado)
print(msg)
