class Veiculo:
    
    def __init__(self, nome, velocidade_max,quilometro_livro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_livro    
        
    def toStr(self):
        print(f'nome = {self.nome}')
        print(f'velocidade_max = {self.velocidade_max}')    
        print(f'Quilometros percorridos por litro = {self.quilometro_litro}')
        
        
modelo_carro = Veiculo("fusca",180,10)
modelo_carro.toStr()        

#exercicio 01 criar fila "onibus" que herdara todas as variáb=veis e metodos da classe veiculo.

class Onibus(Veiculo):
    pass
onibus_escolar = Onibus("Scania",120,8)
onibus_escolar.toStr()
    

#modificar classe filha "Onibus"  de modo que forneça a quantidade de assentos, alem disso o valor deste parametro deve ser 70.

class Veiculo:
    
    def __init__(self, nome, velocidade_max,quilometro_livro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_livro   
        
    def capacidade_assentos(self, capacidade):
        print(f' A capacidade máxima de assentos do veiculo {self.nome} é {capacidade}')
        
    def toStr(self):
        print(f'nome = {self.nome}')
        print(f'velocidade_max = {self.velocidade_max}')
        print(f'Quilometros percorridos por litro = {self.quilometro_litro}')
        
class Onibus(Veiculo):
    def capacidade_assentos(self, capacidade=70):
        return super().capacidade_assentos(capacidade=70)      
    
onibus_escolar = Onibus("scania",120,8)
onibus_escolar.toStr()
onibus_escolar.capacidade_assentos()    
        
             
        


        
    
 