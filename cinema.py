from pessoa import Pessoa


class Cinema:

    def __init__(self, nome, salas, pessoa=None):
        self.nome = nome
        self.salas = salas 
        self.pessoa = pessoa   

    def Registrar_cliente(self):
        if self.pessoa:
            print('Cliente: ', self.pessoa.nome)
            print('Data de nascimento: ', self.pessoa.data_nascimento)
            print('Endereço: ', self.pessoa.endereco)
            print('Registrado com sucesso')
        else:
            print('Cliente não registrado')


c = Cinema('Cinemax', 10)
p = Pessoa('João', '01/01/1999', 'jardim Itu 110')

c.pessoa = p 
c.Registrar_cliente()