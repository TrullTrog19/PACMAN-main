import pyxel

class AnimatedSprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame_index = 0
        self.frame_count = 2  # Número de fotogramas en la hoja de sprites

    def change_frame(self):
        # Cambia al siguiente fotograma
        self.frame_index = (self.frame_index + 1) % self.frame_count

    def draw(self):
        # Dibuja el fotograma actual del sprite
        pyxel.blt(self.x, self.y, 0, self.frame_index * 40, 0, 36, 39, 40)