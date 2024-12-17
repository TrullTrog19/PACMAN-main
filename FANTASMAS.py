import pyxel

# PARA QUE LOS FANTASMAS HEREDEN DE LA CLASE
class Fantasma:
    def __init__(self, x, y, img_x, img_y):
        self.ghost_x = x
        self.ghost_y = y
        self.img_x = img_x
        self.img_y = img_y

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.ghost_x, self.ghost_y, 2, self.img_x, self.img_y, 32, 32, 0)


class Ghost1(Fantasma):
    def __init__(self):
        super().__init__(120, 120, 0, 0)


class Ghost2(Fantasma):
    def __init__(self):
        super().__init__(220, 120, 32, 0)


class Ghost3(Fantasma):
    def __init__(self):
        super().__init__(220, 60, 0, 32)


class Ghost4(Fantasma):
    def __init__(self):
        super().__init__(10, 50, 32, 32)

