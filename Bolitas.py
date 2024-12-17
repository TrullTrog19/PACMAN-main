import pyxel

class Bolitas:
    def __init__(self, mapa, frutas):
        self.mapa = mapa
        self.frutas = frutas

    def draw(self):
        muro_size = 32
        for y in range(len(self.mapa)):
            for x in range(len(self.mapa[y])):
                celda = self.mapa[y][x]
                if celda == 0 and (x, y) not in self.frutas:
                    pyxel.blt(x*muro_size + 8, y*muro_size + 8, 1, 0, 40, 16, 16, 0)  # Dibuja la bolita en el centro de la celda

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