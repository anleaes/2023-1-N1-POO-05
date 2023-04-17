class Ingresso:

    def __init__(self, num_ingresso, num_sala, titulo_filme, preco, num_poltrona):
        self.num_ingresso = num_ingresso
        self.num_sala = num_sala 
        self.titulo_filme = titulo_filme 
        self.preco = preco 
        self.num_poltrona = num_poltrona 
        

p = Ingresso(1, 7, 'Vingadores', 15.00, 9)

print(f'{p.num_ingresso}, {p.num_sala}, {p.titulo_filme}, {p.preco}, {p.num_poltrona}')