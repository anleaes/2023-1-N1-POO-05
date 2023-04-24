from filme import Filme


class Salas:

    def __init__(self, num_sala, poltronas, filme=None):
        self.num_sala = num_sala
        self.poltronas = poltronas
        self.filme = filme 

    def exibir_filme(self):
        if self.filme:
            print('Filme em exibição:', self.filme.titulo)
            print('Duração do filme: ', self.filme.duracao, 'minutos')
            print('Categoria do filme: ', self.filme.categoria)
            print('Classificação: ', self.filme.classificacao)
            print('Sala de exibição: ', self.num_sala)
            print('Poltronas disponiveis: ', self.poltronas)
        else:
            print('Nenhum filme em exibição.')


s = Salas(7, 50)
f = Filme('Vingadores', 120, 'Ação e aventura', '12 anos')

s.filme = f
s.exibir_filme()
