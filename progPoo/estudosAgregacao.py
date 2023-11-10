#Classe salário

class Salario:
    def __init__(self,base,bonus):
        self.base = base
        self.bonus = bonus
        
    def salario_anual(self):
        return(self.base*12)+self.bonus
        
#Classe Empregado 

class empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario_agregado = salario
        self.salario_agregado = salario #agregação
    def salario_total(self):
        return self.salario_agregado.salario_anual()    
        
        
        
        
salario = Salario(1000,700)
emp = empregado('Musashi',46,salario)
print(emp.salario_total)
        
                  
        