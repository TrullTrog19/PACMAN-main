import pyxel
from PACMAN import AnimatedSprite
from FANTASMAS import Ghost1, Ghost2, Ghost3, Ghost4
from Mapa import Mapa

class PacManApp:
    def __init__(self):
        pyxel.init(512, 512, title="Pac-Man", fps=60, quit_key=pyxel.KEY_Q)
        pyxel.load("assets/resourcesPACMAN.pyxres")
        self.pacman = AnimatedSprite(32, 32)
        self.map1 = Mapa()
        self.ghosts = [Ghost1(), Ghost2(), Ghost3(), Ghost4()]
        pyxel.run(self.update, self.draw)

    def update(self):
        self.pacman.update(self.map1)
        for ghost in self.ghosts:
            ghost.update()

    def draw(self):
        pyxel.cls(0)
        self.map1.draw()
        self.pacman.draw()
        for ghost in self.ghosts:
            ghost.draw()

PacManApp()
