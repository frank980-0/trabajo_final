from typing import Any

palos = 'oro' 'basto' 'espada' 'copa'
valores = '1' '2' '3' '4' '5' '6' '7' '10' 'caballo' 'rey'
puntaje_cartas = {
                (1,'espada'): 14, (1,'basto'): 13,
                (7,'espada'): 12, (7,'oro'): 11,
                (3,None): 10, (2, None): 9,
                (1,'copa'): 8, (1,'oro'): 8,
                (1, None): 7, (11, None): 6,(10, None): 5,
                (7,'basto'): 4, (7,'copa'): 4,
                (6 ,None): 3, (5, None):2, (4, None):1,
}
class carta:
    
    def __init__(self, palo: Any, valor):
        self.palo = palo
        self.valor = valor
        self.puntajes_TRUCO = self.obtener_puntajes_truco()
        self.puntajes_envido = self.obtener_puntajes_envido()
        
    def obtener_puntajes_truco (self):
        return puntaje_cartas.get((self.valor, self.palo), puntaje_cartas.get((self.valor,None), 0))
    
    def obtener_puntajes_envido (self):
        if self.valor >= 10:
            return 0
        return self.valor 
    @staticmethod
    def calcular_envido(mano):
        # Agrupar las cartas por palo
        palos = {}
        for carta in mano:
            if carta.palo not in palos:
                palos[carta.palo] = []
            palos[carta.palo].append(carta)
        
        max_envido = 0
        for palo, cartas in palos.items():
            if len(cartas) > 1:
                # Ordenar las cartas del mismo palo por su valor
                cartas_ordenadas = sorted(cartas, key=lambda c: int(c.valor) if c.valor.isdigit() else 0)
                # El Envido es la suma de las dos cartas más altas del mismo palo
                envido = int(cartas_ordenadas[-1].valor) + int(cartas_ordenadas[-2].valor)
                max_envido = max(max_envido, envido)
        
        return max_envido
            

    def __str__(self) -> str:
        return f"{self.valor} de {self.palo} (truco: {self.puntajes_TRUCO}, envido: {self.puntajes_envido})"
    
    

