#HERANÇA

class ContaEspecial(Conta):
    def __init__(self,clientes,numero,saldo,limites):
        Conta.__init__(self,clientes,numero,saldo)
        self.limite = limite
    def sacar(self,valor):
        if(self.saldo + self.limite < valor):
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["saque",valor])
            return True
        
        
#HERANÇA MULTIPLA

class ContaRemuneradaPoupaca(Conta,Poupanca):
    def __init__(self,cliente,numero,saldo,taxaremuneracao):
        Conta.__init__(self,clientes,numero,saldo)
        Poupanca.__init__(self,taxaremuneracao)
        self.taxaremuneracao = taxaremuneracao
    def remuneraConta(self):
        self.saldo += self.saldo * self.taxaremuneracao/30
        
cx = ContaRemuneradaPoupanca([c1,c2],98939123,1500.00,0.03)
cx.remuneraConta()
print(cx.saldo)
        
        
#POLIMORFISMO

class ContaCliente:
    def __init__(self,numero,IOF,IR,valorinvestido,taxarendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento
    def CalculoRendimento(self):
        pass
    
class ContaComum(ContaCliente):
    def __init__(self,numero,IOF,valorinvestido,taxarendimento):
        super().__init__(numero,IOF,IR,valorinvestido,taxarendimento)
    def CalculoRendimento(self):
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)   
        
        
class ContaRemunerada(ContaCliente):
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        super().__init__(numero, IOF, IR, valorinvestido, taxarendimento)
    def CalculoRendimento(self):
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)
        self.valorinvestido -= self.valorinvestido * self.IOF
        
        
#EXEÇÕES

try:
    print(x)
except:
print("variavel indefinida.")


class ExecaoCustomizada(exeption):
    pass
x = -1
if x <0:
    raise Exception("Valor negado")
x = "Hello"
if not type(x) is int:
    raise TypeError("Use apenas inteiros")


    