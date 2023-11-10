from datetime import date

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
# um metodo de classe para criar um objeto pessoa atraves do ano de nascimento.       
    @classmethod     
    def apartirAnoNascimento(cls,nome,ano):   
     return cls(nome, date.today().year - ano)
 # metodo estatico : verifica de é maior de idade
    @staticmethod
    def ehMaiorIdade(idade):
        return idade >= 18
    
pessoa1 = Pessoa('maria',26)
pessoa2 = Pessoa('anna',2007)
print(pessoa1.idade)
print(pessoa2.idade)
# imprimi o resultado.
print(Pessoa.ehMaiorIdade(17)) 
    
        