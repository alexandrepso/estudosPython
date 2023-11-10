# Implementar uma solução em python, através do uso de thread , que faça:

# 1 - Inicie execução de 2 threads 
# 2 - coloque a 1 e 2 threads para esperar , respectivamente 3 e 2 segundos ;
# 3 - Informe a ordem da execução das threads


from time import sleep
from threading import Thread

def tarefa(tempo_espera,nome_tarefa):
    print(f'Iniciando a tarefa {nome_tarefa}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa, {nome_tarefa}')
    
t1 = Thread(target=tarefa, args=(3, 'A'))
t2 = Thread(target=tarefa, args=(2, 'B'))
t1.start()
t2.start()
t1.join() # esperar até completar a execução thread 1
t2.join() # esperar até completar a execução thread 2
print('A execução foi concluida')
    