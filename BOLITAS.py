import pyxel

class Bolita:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pyxel.blt(self.x, self.y, 1, 0, 40, 16, 16, 0)  # Dibuja la bolita en las coordenadas (0, 40) del sprite sheet

class BolitasManager:
    def __init__(self, mapa):
        self.bolitas = []
        self.mapa = mapa
        self.generar_bolitas()

    def generar_bolitas(self):
        for y in range(0, pyxel.height, 32):  # Asumiendo que cada celda del mapa es de 32x32 píxeles
            for x in range(0, pyxel.width, 32):
                if self.mapa.es_bolita(x, y):  # Verifica si la posición es una bolita
                    self.bolitas.append(Bolita(x, y))

    def draw(self):
        for bolita in self.bolitas:
            bolita.draw()