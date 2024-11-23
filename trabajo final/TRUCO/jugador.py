import random
class jugador: 
    def __init__(self, nombre,tipo,):
        self.nombre = nombre
        self.tipo = tipo
        self.puntos = 0
        self.mano = []
    
    def jugar (self):

        if self.tipo == 'aleatorio':
            return random.choice(self.mano)
        elif self.tipo == 'inteligente':
            return 