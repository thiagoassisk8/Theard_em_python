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