class pessoa:
    def __init__(self, name,ender):
        self.name = name
        self.ender = ender
        
    def set_name(self, name):
        self.name = name
        
    def set_ender(self,ender):
        self.ender = ender
        
    def get_name(self):
        return self.name
        
    def get_ender(self):
        return self.ender
    
    pessoa1 = Pessoa("maria","rua arnaldo")
    pessoa2 = Pessoa("joão","rua alvinopolis")
    
    print(f'Nome: {pessoa1.get_name()}, Endereço:{pessoa1.get_ender()}')
    
    Nome: maria,  Endereço: rua arnaldo
    
    print(f'Nome: {pessoa2.get_name()}, Endereço:{pessoa2.get_ender()}')
    
    Nome: joão, Endereço: rua alvinopolis
    
    
    
    
    
    
            
        
