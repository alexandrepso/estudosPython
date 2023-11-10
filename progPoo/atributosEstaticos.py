class Pessoa:
    _contador = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa._contador += 1
        
    def imprimir(self):
        print(self.nome, " Tem ",self.idade,"ano(s)")
        
    @property
    def contador(self):
        return type(self) ._contador
    
    p1 = Pessoa("Carlos",18)
    print(p1.contador)
    print(Pessoa._contador)
    
Class NomeCompleto:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    @classmethod    
    def fromString(cls,texto):
            nome,sobrenome = map(str,texto.split(''))
            objeto = cls(nome,sobrenome)
            return objeto
    registro1 = NomeCompleto.fromString("Luiz Braga")
    
Class NomeCompleto:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    @classmethod
    def fromString(cls,texto):
        nome,sobrenome = map(str,texto.split(''))
        objeto = cls(nome,sobrenome)
        return objeto
    @staticmethod
    def isValid(texto):
        nomes = texto.split('')
        return len(nomes) > 1
    
    
        
        