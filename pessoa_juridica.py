from pessoa import Pessoa


class Pessoa_Juridica(Pessoa):

    def __init__(self, nome, data_nascimento, endereco, cnpj):
        super().__init__(nome, data_nascimento, endereco)
        self.cnpj = cnpj
        
    
p = Pessoa_Juridica('Lucas', '10/10/2000', 'Jardim Itu 712', 99999)

print(p.nome)
print(p.data_nascimento)
print(p.endereco)
print(p.cnpj)
