# Implementar uma solução em python, através do uso de Thread, que faça:

# a - Inicie a execução de uma Thread
# b- coloque a thread para esperar 2 seguntos
# c- informe o início e o fim da execução da Thread

from time import sleep
from threading import Thread

def tarefa (tempo_espera, mensagem):
    print(f'\nIniciando a tarefa {mensagem}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {mensagem}')
Thread = Thread(target=tarefa, args=(2, 'Thread em execução'))    
Thread.start()
print('\nAguardando pela execução da thread...')
Thread.join
print('A execução foi concluida!')


    