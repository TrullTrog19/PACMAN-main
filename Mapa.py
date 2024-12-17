import pyxel
import random

class Mapa:
    def __init__(self):
        self.mapa = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 1],
            [1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1],
            [1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1],
            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

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
                elif celda == 2:
                    pyxel.blt(x*muro_size, y*muro_size, 1, 0, 40, 16, 16, 0)

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
            return self.mapa[fila][columna] == 2
        return False
    
    def hitbox_pacman(self, x, y, ancho, alto):
        margen_inf = 2
        margen_colision = 2
        for i in range((y + margen_inf) // 32, (y + alto - 1 - margen_inf) // 32 + 1):  # Filas afectadas, desde la esquina izq hasta la derecha
            for j in range((x + margen_colision) // 32, (x + ancho - 1 - margen_colision) // 32 + 1):  # Columnas afectadas, desde la esquina izq hasta la derecha
                if 0 <= i < len(self.mapa) and 0 <= j < len(self.mapa[0]):  # Límite del mapa
                    if self.mapa[i][j] == 1:  # Si hay un muro
                        return True
    def hitbox_fantasma(self, x, y, ancho, alto):
        margen_inf = 1
        margen_colision = 1
        for i in range((y + margen_inf) // 32, (y + alto - 1 - margen_inf) // 32 + 1):
            for j in range((x + margen_colision) // 32 , (x + ancho - 1 - margen_colision) // 32 + 1): 
                if 0 <= i < len(self.mapa) and 0 <= j < len(self.mapa[0]):
                    if self.mapa[i][j] == 1:
                        return True
