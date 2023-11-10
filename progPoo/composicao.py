import datetime
from Extrato import Extrato


class Extrato:
    def __init__(self):
        self.transacoes = []
        
    def extrado(self,numeroconta):
        print(f"Extrato : {numeroconta}\n")
        for p in self.transacoes:
                print(f”{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3].strftime(‘%d/%b/%y)}”)
                
class Conta:
    def __init__(self, cliente, conta, saldo):
        self.cliente = cliente
        self.conta = conta
        self.saldo = saldo 
        self.sata abertura = datetime.satetime.today()
        self.extrato = Extrato()
        
    def depositar(self,valor):
        self.saldo += valor
        self.extrato.trasacoes.append(["DEPOSITO", valor, "Data",datetime.datetime.today ()])

    def sacar(self,valor):
        if self.saldo < valor:
           return False
        else:
             self.saldo -= valor
             self.extrato.trasacoes.append(["SAQUE", valor, "Data",datetime.datetime.today ()]) 
             return True
             
    def tranferirValor(self,contadestino,valor):
        if self.saldo < valor:
           return "Não  existe saldo suficiente"
        else:
        
             contadestino.depositar(valor)
             self.saldo -= valor
             self.extrato.trasacoes.append(["TRANSFERENCIA", valor, "Data",datetime.datetime.today ()])
             return "Tranferencia Realizada"
            
                              
        
        
        
         