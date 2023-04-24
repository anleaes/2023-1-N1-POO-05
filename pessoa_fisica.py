from pessoa import Pessoa


class Pessoa_Fisica(Pessoa):

    def __init__(self, nome, data_nascimento, endereco, cpf):
        super().__init__(nome, data_nascimento, endereco)
        self.cpf = cpf


p = Pessoa_Fisica('João', '01/01/1999', 'jardim Itu 110', 121222)

print(p.nome)
print(p.data_nascimento)
print(p.endereco)
print(p.cpf)