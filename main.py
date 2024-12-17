import pyxel
from PACMAN import AnimatedSprite
from FANTASMAS import Ghost1, Ghost2, Ghost3, Ghost4
from Mapa import Mapa


# Definimos la clase principal
class PacManApp:
    def __init__(self):
        pyxel.init(512, 512, title="Pac-Man", fps=60, quit_key=pyxel.KEY_Q)
        pyxel.load("assets/resourcesPACMAN.pyxres")
        self.pacman = AnimatedSprite(32, 32)
        self.map1 = Mapa()
        self.bolitas_comidas = 0  # Contador de bolitas comidas
        self.ghosts = [Ghost1(self.map1, self.pacman), Ghost2(self.map1), Ghost3(self.map1), Ghost4(self.map1)]
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.pacman.update(self.map1):
            self.bolitas_comidas += 1  # Incrementa el contador si se ha comido una bolita
        for ghost in self.ghosts:
            ghost.update()

    def draw(self):
        pyxel.cls(0)
        self.map1.draw()
        self.pacman.draw()
        for ghost in self.ghosts:
            ghost.draw()
        self.draw_text(5, 5, f"Bolitas comidas: {self.bolitas_comidas}", pyxel.COLOR_BLACK)

    def draw_text(self, x, y, text, color):
        # Dibuja el texto varias veces para simular un tamaño más grande
        scale = 2  # Escala del texto
        for i in range(scale):
            for j in range(scale):
                pyxel.text(x + i, y + j, text, pyxel.COLOR_WHITE)  # Fondo blanco para mayor visibilidad
        pyxel.text(x, y, text, color)  # Texto en color negro

PacManApp()
