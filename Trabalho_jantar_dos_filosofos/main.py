"""
Trabalho de SO
feito por : Carlos Matheus, Joyce Simões.
"""

""" 
    IMPLEMENTAÇÃO
"""

"""
    IMPORTS
        LIBS NECESSÁRIAS PARA PROJETO
"""
import _thread as thread

import time, random

import threading

garfo = list()

#Preechendo a lista de garfos
for i in range(10):
    garfo.append(threading.Semaphore(1))

def filosofo(f):
    f = int(f) #representando os filosofos na lista de semaforos

    while True:
        #O filosofo tenta pegar o garfo da esquerda, caso esteja ocupado ele espera até que fique livre
        garfo[f].acquire()
        #O filosofo tenta pegar o garfo da Direita, caso esteja ocupado ele espera até que fique livre
        garfo[(f + 1) % 5].acquire()

        #Exibe qual filosofo esta comendo, aqui ele esta fazendo a ação de comer
        print("Filósofo {} comendo \n".format(f))
        time.sleep(random.randint(1, 5))
        garfo[f].release()# liberando o garfo da esquerda
        garfo[(f+1)%5].release() #liberando o garfo da direita.
        #apos terminar ele irá pensar e dar espaço para outro filoso comer.
        print("Filósofo {} pensando \n".format(f))
        time.sleep(random.randint(1, 10))

#criação dos filosofos
for i in range(10):
    print("Filosofo {}".format(i))
    thread.start_new_thread(filosofo, tuple([i]))

#loop do programa.
while 1:pass