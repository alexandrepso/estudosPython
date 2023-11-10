class Cliente:
    def __init__(self,cpf,nome,endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        
        
class Conta:
    def __init__(self,cliente,numero,saldo):   
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        
    def depositar(self,valor):
        self.saldo += valor
        
    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
        
    def transfereValor(self,contaDestino,valor):
        if self.saldo < valor:
            return (" Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return (" Tranferencia Realizada")
        
    def gerarsaldo(self):
        print(f"numero:{self.numero}\n saldo: {self.saldo}") 
        
        
from contas import Conta
from clientes import Cliente

c1 = Cliente1 = Cliente(123,"joão","rua 01")
c2 = Cliente2 = Cliente(456,"maria","rua 02")
conta1 = Conta([Cliente1,Cliente2],1,0)
conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()



"""Atenção!
Na linha número 5, é instanciado um objeto conta1 com dois clientes agregados:
cliente1 e cliente2. Esses dois objetos são passados como parâmetros.

Qual é o resultado dessa execução? Qual será o valor final na conta?

Sugestão: altere o programa do código anterior a fim de criar mais uma conta para dois clientes diferentes. Como desafio, tente, por meio do objeto conta, imprimir o nome e o endereço dos clientes associados às contas."""
               
        
        
    
        