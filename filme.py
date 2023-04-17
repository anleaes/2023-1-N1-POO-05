class Filme:
    
    def __init__(self, titulo, duracao, categoria):
        self.titulo = titulo
        self.duracao = duracao 
        self.categoria = categoria 
        

p = Filme('Vingadores', 120, 'herois' )

print(f"{p.titulo}, {p.duracao}, {p.categoria}")
    

