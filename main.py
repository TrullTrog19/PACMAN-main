import pyxel
from PACMAN import AnimatedSprite
from FANTASMAS import Ghost1
from FANTASMAS import Ghost2
from FANTASMAS import Ghost3 
from FANTASMAS import Ghost4 

class PacManApp:
    def __init__(self):
        pyxel.init(1024, 512, title="Pac-Man", fps=60, quit_key=pyxel.KEY_Q)
        self.pacman_x = 80
        self.pacman_y = 60

        # Cargar el archivo de recursos
        #pyxel.load("assets/resourcesPACMAN.pyxres")
        
        # Crear la instancia de AnimatedSprite para el personaje animado
        self.pacman = AnimatedSprite(self.pacman_x, self.pacman_y)
        #Inicializamos el fantasma
        self.ghost1 = Ghost1()
        self.ghost2 = Ghost2()
        self.ghost3 = Ghost3()
        self.ghost4 = Ghost4()
        pyxel.run(self.update, self.draw)

    def update(self):
        # Movimiento del Pac-Man con las teclas W, A, S, D
        movimiento = False  # Variable para verificar si hubo movimiento

        if pyxel.btn(pyxel.KEY_W):  # Detecta si se presionó la tecla
            self.pacman_y -= 5
            
        if pyxel.btn(pyxel.KEY_S):
            self.pacman_y += 5
            
        if pyxel.btn(pyxel.KEY_A):
            self.pacman_x -= 5

        if pyxel.btn(pyxel.KEY_D):
            self.pacman_x += 5
            
        if pyxel.btnp(pyxel.KEY_F):
            self.pacman_x += 0
            movimiento = True
        
        # Actualizar la posición del pacman animado
        self.pacman.x = self.pacman_x
        self.pacman.y = self.pacman_y

        # Cambiar el fotograma solo si hubo movimiento
        if movimiento:
            self.pacman.change_frame()
        

    def draw(self):
        pyxel.cls(0)
        
        # Dibujar el Pac-Man animado
        pyxel.load("assets/resourcesPACMAN.pyxres")
        self.pacman.draw()
        #ahora el fantasma
        pyxel.load("assets/resources.pyxres")
        self.ghost1.draw()
        self.ghost2.draw()
        self.ghost3.draw()
        self.ghost4.draw()

PacManApp()






