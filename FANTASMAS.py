import pyxel
import random

class Fantasma:
    def __init__(self, mapa, frames):
        self.mapa = mapa
        self.ghost_x, self.ghost_y = mapa.pos_random()
        self.frames = frames
        self.current_frame = 0
        self.ancho = 30
        self.alto = 30
        self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])

    def move(self):
        new_x = self.ghost_x
        new_y = self.ghost_y

        if self.direccion == "arriba":
            new_y -= 2
        if self.direccion == "abajo":
            new_y += 2
        if self.direccion == "izquierda":
            new_x -= 2
        if self.direccion == "derecha":
            new_x += 2

        if not self.mapa.hitbox_fantasma(new_x, new_y, self.ancho, self.alto):
            self.ghost_x = new_x
            self.ghost_y = new_y
        else:
            self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])

    def update(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.move()

    def draw(self):
        img_x, img_y = self.frames[self.current_frame]
        pyxel.blt(self.ghost_x, self.ghost_y, 2, img_x, img_y, self.ancho, self.alto, 0)


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
