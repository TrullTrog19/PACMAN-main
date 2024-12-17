import pyxel


# PARA QUE LOS FANTASMAS HEREDEN DE LA CLASE
class Fantasma:
    def __init__(self, mapa, img_x, img_y):
        self.ghost_x, self.ghost_y = mapa.pos_random()
        self.img_x = img_x
        self.img_y = img_y
        self.ancho = 30
        self.alto = 30

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.ghost_x, self.ghost_y, 2, self.img_x, self.img_y, self.ancho, self.alto, 0)


class Ghost1(Fantasma):
    def __init__(self, mapa):
        super().__init__(mapa, 0, 0)


class Ghost2(Fantasma):
    def __init__(self, mapa):
        super().__init__(mapa, 32, 0)


class Ghost3(Fantasma):
    def __init__(self, mapa):
        super().__init__(mapa, 0, 32)


class Ghost4(Fantasma):
    def __init__(self, mapa):
        super().__init__(mapa, 32, 32)

