import pyxel

<<<<<<< HEAD
class Fantasma:
    def __init__(self, x, y, frames):
        self.ghost_x = x
        self.ghost_y = y
        self.frames = frames
        self.current_frame = 0
=======

# PARA QUE LOS FANTASMAS HEREDEN DE LA CLASE
class Fantasma:
    def __init__(self, mapa, img_x, img_y):
        self.ghost_x, self.ghost_y = mapa.pos_random()
        self.img_x = img_x
        self.img_y = img_y
        self.ancho = 30
        self.alto = 30
>>>>>>> 0ae3ba939bdd73e20d72365c0590295ffb1da3e1

    def update(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)

    def draw(self):
<<<<<<< HEAD
        img_x, img_y = self.frames[self.current_frame]
        pyxel.blt(self.ghost_x, self.ghost_y, 2, img_x, img_y, 32, 32, 0)


class Ghost1(Fantasma):
    def __init__(self):
        frames = [(0, 0), (64, 0)]  # Provided frame coordinates
        super().__init__(120, 120, frames)


class Ghost2(Fantasma):
    def __init__(self):
        frames = [(32, 0), (96, 0)]  # Provided frame coordinates
        super().__init__(220, 120, frames)


class Ghost3(Fantasma):
    def __init__(self):
        frames = [(0, 32), (64, 32)]  # Provided frame coordinates
        super().__init__(220, 60, frames)


class Ghost4(Fantasma):
    def __init__(self):
        frames = [(32, 32), (96, 32)]  # Provided frame coordinates
        super().__init__(10, 50, frames)
=======
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

>>>>>>> 0ae3ba939bdd73e20d72365c0590295ffb1da3e1
