import pyxel
from PACMAN import AnimatedSprite
from FANTASMAS import Ghost1
from FANTASMAS import Ghost2
from FANTASMAS import Ghost3 
from FANTASMAS import Ghost4 
from Mapa import Mapa
#definimos la clase principal
class PacManApp:
    def __init__(self):
        pyxel.init(512, 512, title="Pac-Man", fps=60, quit_key=pyxel.KEY_Q)
        # Cargar el archivo de recursos
        pyxel.load("assets/resourcesPACMAN.pyxres")
        # Crear la instancia de AnimatedSprite para el personaje animado
        self.pacman = AnimatedSprite(32, 32)
        self.map1 = Mapa()
        #Inicializamos el fantasma
        #pyxel.load("assets/resourcesFANTASMA.pyxres")
        #self.ghost1 = Ghost1()
        #self.ghost2 = Ghost2()
        #self.ghost3 = Ghost3()
        #self.ghost4 = Ghost4()
        pyxel.run(self.update, self.draw)

    def update(self):
        # Movimiento del Pac-Man con las teclas W, A, S, D
        self.pacman.update(self.map1)

        

    def draw(self):
        pyxel.cls(0)
        self.map1.draw()
        # Dibujar el Pac-Man animado
        #pyxel.load("assets/resourcesPACMAN.pyxres")
        self.pacman.draw()

        #ahora el fantasma
        #pyxel.load("assets/resources.pyxres")
        #self.ghost1.draw()
        #self.ghost2.draw()
        #self.ghost3.draw()
        #self.ghost4.draw()

PacManApp()




#Alberto melón

