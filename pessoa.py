class Pessoa:

    def __init__(self, nome, data_nascimento, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco 

      
p = Pessoa('Lucas', '01/01/1999', 'Jardim Itu 155')

print(f'Nome: {p.nome}, data de nascimento: {p.data_nascimento}, endereço: {p.endereco}')
