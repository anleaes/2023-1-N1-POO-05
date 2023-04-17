from pessoa import Pessoa


class Pessoa_Juridica:

    def __init__ (self, nome, data_nascimento, endereco, cnpj):
        super().__init__(nome, data_nascimento, endereco)
        self.cnpj = cnpj
        
    

    
