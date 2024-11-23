from cartas import*
import random
class mazo:
    def __init__(self):
        self.cartas = [carta(valor, palo) for palo in carta.palos for valor in carta.valores]
        random.shuffle(self.cartas)
    
    def repartir (self):
        return [{self.cartas.pop()}, {self.cartas.pop()}, {self.cartas.pop()}]