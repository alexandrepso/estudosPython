# Implementar uma solução em python, através do uso de threads, que faça:

# 1 - inicie a execução de 2 threads;
# 2 - a primeira threads deve calcular o cubo de um número;
# 3 - a segunda thread deve calcular o quadrado de um numero ;
# 4 - coloque a 1 e 2 thread para esperar , 3 e 2 segundos respectivamente ;
# 5 - informe a ordem da execução das threads;

from time import sleep
from threading import Thread

def calcular_cubo(num, tempo_espera):
    print(f'\nCubo: {num * num * num}')
    sleep(tempo_espera)
    print('Conclusão da função calcular_cubo')
    
def calcular_quadrado(num, tempo_espera):
    print(f'\nQuadrado: {num * num}')
    sleep(tempo_espera)
    print('Conclusão da função calcular_quadrado')
    
t1 = Thread(target=calcular_quadrado, args=(5,3))
t2 = Thread(target=calcular_cubo, args=(5,2))
t1.start()
t2.start()
t1.join() # esperar até a conclusão da thread 1
t2.join() # esperar até a conclusão da thread 2
print('A execução foi concluida')