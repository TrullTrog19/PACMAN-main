import pyxel
from PACMAN import AnimatedSprite
from FANTASMAS import Ghost1
from FANTASMAS import Ghost2
from FANTASMAS import Ghost3 
from FANTASMAS import Ghost4 

class PacManApp:
    def __init__(self):
        pyxel.init(512, 512, title="Pac-Man", fps=60, quit_key=pyxel.KEY_Q)
        # Cargar el archivo de recursos
        pyxel.load("assets/resourcesPACMAN.pyxres")
        self.mapa = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        # Crear la instancia de AnimatedSprite para el personaje animado
        self.pacman = AnimatedSprite(80, 60)

        #Inicializamos el fantasma
        #self.ghost1 = Ghost1()
        #self.ghost2 = Ghost2()
        #self.ghost3 = Ghost3()
        #self.ghost4 = Ghost4()
        pyxel.run(self.update, self.draw)

    def update(self):
        # Movimiento del Pac-Man con las teclas W, A, S, D
        self.pacman.update()

        

    def draw(self):
        pyxel.cls(0)
        for y in range(len(self.mapa)):
            for x in range(len(self.mapa[y])):
                muro = self.mapa[y][x]
                if muro == 1:
                    pyxel.blt(x*32,y*32, 1, 0, 0, 32, 32, 0)
                elif muro == 0:
                    pass
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

