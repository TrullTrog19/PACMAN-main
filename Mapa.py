import pyxel
import random

class Mapa:
    def __init__(self):
        self.mapa = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.frutas = [(1, 1), (1, 14), (14, 1), (14, 14)]  # Posiciones de las frutas

    def pos_random(self):
        while True:
            x = random.randint(1, len(self.mapa[0])-2)
            y = random.randint(1, len(self.mapa)-2)
            if self.mapa[y][x] == 0:
                return x*32, y*32
    
    def draw(self):
        muro_size = 32
        for y in range(len(self.mapa)):
            for x in range(len(self.mapa[y])):
                celda = self.mapa[y][x]
                if celda == 1:
                    pyxel.blt(x*muro_size, y*muro_size, 1, 0, 0, muro_size, muro_size, 0)
                elif celda == 0 and (x, y) not in self.frutas:
                    pyxel.blt(x*muro_size + 8, y*muro_size + 8, 0, 0, 40, 16, 16, 0)  # Dibuja la bolita en el centro de la celda
        for fruta in self.frutas:
            pyxel.blt(fruta[0]*32 + 8, fruta[1]*32 + 8, 1, 0, 48, 56, 16, 0)  # Dibuja la fruta en las esquinas

    def es_muro(self, x, y):
        columna = x // 32
        fila = y // 32
        if 0 <= fila < len(self.mapa) and 0 <= columna < len(self.mapa[0]):
            return self.mapa[fila][columna] == 1
        return False
    
    def es_bolita(self, x, y):
        columna = x // 32
        fila = y // 32
        if 0 <= fila < len(self.mapa) and 0 <= columna < len(self.mapa[0]):
            return self.mapa[fila][columna] == 0
        return False
    
    def comer_bolita(self, x, y):
        columna = (x + 16) // 32  # Ajusta la posición para el centro de Pac-Man
        fila = (y + 16) // 32  # Ajusta la posición para el centro de Pac-Man
        if 0 <= fila < len(self.mapa) and 0 <= columna < len(self.mapa[0]):
            if self.mapa[fila][columna] == 0:
                self.mapa[fila][columna] = -1  # Marca la bolita como comida
                return True
        return False
    
    def comer_fruta(self, x, y):
        columna = (x + 16) // 32  # Ajusta la posición para el centro de Pac-Man
        fila = (y + 16) // 32  # Ajusta la posición para el centro de Pac-Man
        if (columna, fila) in self.frutas:
            self.frutas.remove((columna, fila))  # Elimina la fruta del mapa
            return True
        return False
