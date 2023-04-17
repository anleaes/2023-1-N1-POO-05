from filme import Filme


class Salas:

    def __init__(self, num_sala, poltrona, filme):
        self.num_sala = num_sala
        self.poltrona = poltrona 
        self.filme = filme


p = Salas(7, 9, 'Vingadores' )

print(f'{p.num_sala}, {p.poltrona}, {p.filme}')
        
    