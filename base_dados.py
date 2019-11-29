import logging
import threading
'''
class Counter(object):  #Tentativa de Lock
    def __init__(self, start = 0):
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        logging.debug('Aguardando lock')
        self.lock.acquire()
        try:
            logging.debug('Aguardando  lock')
            self.value = self.value + 1
        finally:
            logging.debug('Aguardando lock')
            self.lock.release()
'''
class contas:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

#Usuários cadastrados no banco
baseDadosBanco = [
    contas('Thiago','4570-1',0.0),
    contas('Gabriel','2761-1',960.0),
    contas('Isabela','3450-1',1000.0)
]
