class Pessoa:
    def __init__(self,nome,idade):     #construtor
        self.nome = nome                            #atributos
        self.idade = idade                          #operaçoes(metodos)
    def imprimir(self):
        print(self.nome,"tem",self.idade,"ano(s)")     #tipo e variavel  
    def getIdade(self):                                # clase e objeto 
        return self.idade
    def setNome(self,nome):
        self.nome = nome
        
class Profissional(Pessoa): 
    def __init__(self, nome, idade,profissao):
        super().__init__(nome,idade)
        self.profissao = profissao
    def imprimir(self):
        super().imprimir()  
        print("\t e trabalha como",self.profissao)  
               
        
p = Profissional ("Anna",16,"advogada")
p.imprimir()