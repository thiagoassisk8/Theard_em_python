# Função transferir
from base_dados import *  
import time,os
import threading

def selecionarIdConta (numero, baseDadosBanco): 
    for i in range(len(baseDadosBanco)):
        if baseDadosBanco[i].numero == numero:
            idConta = i
            break
    return idConta

contaOrigem = input('Digite a conta origem da transferencia \n')
contaDestino = input('Digite a conta destino da transferencia \n')    

def transferir():
    valor = 10
    idContaOrigem = selecionarIdConta(contaOrigem, baseDadosBanco)
    idContaDestino = selecionarIdConta(contaDestino, baseDadosBanco)

    
    if baseDadosBanco[idContaOrigem].saldo < valor:
        print('ERROOOO, o saldo da conta {} é insuficiente para realizar a transfêrencia'.format(baseDadosBanco[idContaOrigem].numero))
    else:
        #retira o valor da transfência da conta origem 
        baseDadosBanco[idContaOrigem].saldo = baseDadosBanco[idContaOrigem].saldo - valor

        #Adiciona o valor da transfêrencia na conta destino
        baseDadosBanco[idContaDestino].saldo = baseDadosBanco[idContaDestino].saldo + valor       
        print("Foram transferidos R$ {}  da conta {} para a conta {} O saldo da conta {} agora é de {} reais.".format(valor,contaOrigem,contaDestino,contaOrigem, baseDadosBanco[idContaOrigem].saldo))

print("Aguardando thread")
time.sleep(3)

for indice in range(100):
    t = threading.Thread(target=transferir)
    t.start()
    while t.isAlive():    
        print('-'*93 )
    

print ("Thread morreu")
print("Finalizando programa")


