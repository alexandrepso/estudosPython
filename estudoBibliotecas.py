import numpy as np 

def entrada_dados():
    coeficiente = quantidade = eval(input("Digite o valor coeficiente"))
    return coeficiente

def calcular_delta(a,b,c):
    delta=b*b-4*a*c
    return delta

    #f(x)=ax^2+bx+c 
    a=entrada_dados()
    b=entrada_dados()
    c=entrada_dados()
    
    delta=calcular_delta(a,b,c)
    
    resultado=calcular_raizes(a,b,c,delta)
    return resultado
    
    

def calcular_raizes(a,b,c,delta):
    if(delta<0):
        resultado='a equação não possui raizes no numeros reais'
    elif(delta==0):
        x=-b/(2*a)
        resultado=f'a equação possui apenas raiz: {x}'
    else:
        x1=(-b-np.sqrt(delta))/(2*a)
        x2=(-b+np.sqrt(delta))/(2*a)
        resultado=f'a equação possui duas raizes: {x1} e {x2}'
        
    return resultado                                  
        
        
        
        
        