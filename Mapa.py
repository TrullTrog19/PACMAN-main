import pyxel
import random
from Bolitas import Bolitas

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
        self.bolitas = Bolitas(self.mapa, self.frutas)

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
        self.bolitas.draw()
        for fruta in self.frutas:
            pyxel.blt(fruta[0]*32 + 8, fruta[1]*32 + 8, 1, 48, 56, 16, 16, 0)  # Dibuja la fruta en las esquinas con el sprite adecuado

    def hitbox_pacman(self, x, y, ancho, alto):
        margen_inf = 2
        margen_colision = 2
        for i in range(int((y + margen_inf) // 32), int((y + alto - 1 - margen_inf) // 32) + 1):  # Filas afectadas
            for j in range(int((x + margen_colision) // 32), int((x + ancho - 1 - margen_colision) // 32) + 1):  # Columnas afectadas
                if 0 <= i < len(self.mapa) and 0 <= j < len(self.mapa[0]):  # Límite del mapa
                    if self.mapa[i][j] == 1:  # Si hay un muro
                        return True
        return False

    def hitbox_fantasma(self, x, y, ancho, alto):
        margen_inf = 1
        margen_colision = 1
        for i in range(int((y + margen_inf) // 32), int((y + alto - 1 - margen_inf) // 32) + 1):  # Filas afectadas
            for j in range(int((x + margen_colision) // 32), int((x + ancho - 1 - margen_colision) // 32) + 1):  # Columnas afectadas
                if 0 <= i < len(self.mapa) and 0 <= j < len(self.mapa[0]):  # Límite del mapa
                    if self.mapa[i][j] == 1:  # Si hay un muro
                        return True
        return False
    
    def es_muro(self, x, y):
        columna = x // 32
        fila = y // 32
        if 0 <= fila < len(self.mapa) and 0 <= columna < len(self.mapa[0]):
            return self.mapa[fila][columna] == 1
        return False
    
    def es_bolita(self, x, y):
        return self.bolitas.es_bolita(x, y)
    
    def comer_bolita(self, x, y):
        return self.bolitas.comer_bolita(x, y)
    
    def comer_fruta(self, x, y):
        columna = (x + 16) // 32  # Ajusta la posición para el centro de Pac-Man
        fila = (y + 16) // 32  # Ajusta la posición para el centro de Pac-Man
        if (columna, fila) in self.frutas:
            self.frutas.remove((columna, fila))  # Elimina la fruta del mapa
            return True
        return False
