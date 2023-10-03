class ClassSomaMultiplica:
    def __init__(self, a,b):
        self.a = a
        self.b = b
        
    def soma(self):
        return self.a+self.b;
    
    def multiplica(self):
        return self.a*self.b;
    
class Derivada(ClassSomaMultiplica):
    def subtrair(self):
        return self.a-self.b;    
    
    def dividir(self):
        return self.a/self.b;
    
d = Derivada(10,20)
print(f'A soma de 10 e 20 é: {d.soma()}')
print(issubclass(Derivada,ClassSomaMultiplica))    


# ExEMPLO DE SOBRECARGA

def somar (x,y,z = 0):
    return x+y+z

print(somar (20,30)) 
print(somar (20,30,50))


# EXEMPLO DE POLIMORFISMO

class Argentina():
    def capital(self):
        print("Boenos Aires é a capital da Argentina.")
    def lingua_oficial(self):
        print("A lingua oficial da Argentina é Espanhol.")
        
class Brasil():
    def capital(self):
        print("Brasília é a capital do Brasil.")
    def lingua_oficial(self):
        print("A lingua oficial do Brasil é Português.")
            
            
obj_arg = Argentina()
obj_bra = Brasil()
for país in (obj_bra, obj_bra):
    país.capital()
    país.lingua_oficial()
    
    
    
class Veiculo:
    def rodar(self):
        print(" Reduz o consumo de combustivel.")    
        
class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().rodar()
        print("Esse veiculo utiliza eletricidade.")
        
veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()


#EXEMPLO SOBRE EXEÇÃO   

x = 10
if x > 5:
    raise Exception('x não pode ser maior do que 5. O valor de x foi de: {}.'.format(x))

        
    
    
                
            


