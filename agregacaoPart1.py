Class Conta:
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
Class Cliente:
    def __init__(self,nome,cpf,endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        
c1 = Cliente('111111111-11','Ana','rua arnaldo ')
c2 = Cliente('222222222-22','Maria','rua maria')
conta = Conta([c1,c2],24237891,2500.00)

#Composição


Class Extrato:
    def __init__(self):
        self.transacoes = []
    def imprimir(self):
        for p in self.transacoes:
            print(p[0],p[1])
           
Class Conta:
    def __init__(self,cliente,numero,saldo):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato()
        
    def depositar(self,valor):
        self.saldo += valor
        self.extrato.transacoes.append(["Deposito",valor])
        
        
    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["Saque",valor])
            return True
        
c1 = Cliente('111111111-11','ana','rua padre')
c2 = Cliente('222222222-22','maria','rua mae')
 conta = Conta([c1,c2],24237891,2500.00)
 
 conta.depositar(1000.00)
 conta.sacar(500.00)
 conta.extrato.imprimir()    
        
        
    
            
            
    
    
        
        
        
    
    


