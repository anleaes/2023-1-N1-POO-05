from pessoa import Pessoa


class Ingresso:

    def __init__(self, num_ingresso, num_sala, titulo_filme, preco, poltrona, pessoa=None):
        self.num_ingresso = num_ingresso
        self.num_sala = num_sala 
        self.titulo_filme = titulo_filme 
        self.preco = preco 
        self.poltrona = poltrona
        self.pessoa = pessoa

    def comprar_ingresso(self):
        if self.pessoa:
            print('Cliente: ', self.pessoa.nome)
            print('Numero do ingresso: ', self.num_ingresso)
            print('Numero da sala: ', self.num_sala)
            print('Filme em exibição: ', self.titulo_filme)
            print('Preço: ', self.preco)
            print('Poltrona: ', self.poltrona)
        else:
            print('Ingresso não comprado.')
            

i = Ingresso(1, 7, 'Vingadores', 15.00, 9)
p = Pessoa('João', '01/01/1999', 'jardim Itu 110')

i.pessoa = p 
i.comprar_ingresso()

