import pyxel

class Fantasma:
    def __init__(self, mapa, frames):
        self.ghost_x, self.ghost_y = mapa.pos_random()
        self.frames = frames
        self.current_frame = 0
        self.ancho = 30
        self.alto = 30

    def update(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)

    def draw(self):
        img_x, img_y = self.frames[self.current_frame]
        pyxel.blt(self.ghost_x, self.ghost_y, 2, img_x, img_y, 32, 32, 0)


class Ghost1(Fantasma):
    def __init__(self, mapa):
        frames = [(0, 0), (64, 0)]  # Provided frame coordinates
        super().__init__(mapa, frames)


class Ghost2(Fantasma):
    def __init__(self, mapa):
        frames = [(32, 0), (96, 0)]  # Provided frame coordinates
        super().__init__(mapa, frames)


class Ghost3(Fantasma):
    def __init__(self, mapa):
        frames = [(0, 32), (64, 32)]  # Provided frame coordinates
        super().__init__(mapa, frames)


class Ghost4(Fantasma):
    def __init__(self, mapa):
        frames = [(32, 32), (96, 32)]  # Provided frame coordinates
        super().__init__(mapa, frames)
