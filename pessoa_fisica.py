from pessoa import Pessoa


class Pessoa_Fisica:

    def __init__ (self, nome, data_nascimento, endereco, cpf):
        super().__init__(nome, data_nascimento, endereco)
        self.cpf = cpf 