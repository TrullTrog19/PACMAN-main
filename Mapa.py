import pyxel

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


        
    def draw(self):
        for y in range(len(self.mapa)):
            for x in range(len(self.mapa[y])):
                muro = self.mapa[y][x]
                if muro == 1:
                    pyxel.blt(x*32,y*32, 1, 0, 0, 32, 32, 0)
                elif muro == 0:
                    pass
    
    #def hitbox(self, x, y):
    #    columna = x // 32
    #    fila = y // 32
    #    if 0 <= fila < len(self.mapa) and 0 <= columna < len(self.mapa[0]):
    #        return self.mapa[fila][columna] == 1
    #    return False
    
    def hitbox2(self, x, y ,ancho, alto):
        margen_inf = 3
        for i in range(y // 32, (y + alto - 1-margen_inf) // 32 + 1):  # Filas afectadas, desde la esquina izq hasta la derecha
            for j in range(x // 32, (x + ancho - 1) // 32 + 1):  # Columnas afectadas, desde la esquina izq hasta la derecha
                if 0 <= i < len(self.mapa) and 0 <= j < len(self.mapa[0]):  # Límite del mapa
                    if self.mapa[i][j] == 1:  # Si hay un muro
                        return True
