import pyxel

class AnimatedSprite:
    def __init__(self, x, y):
        self.pacman_x = x
        self.pacman_y = y
        self.movement = ""
        self.pacman_imagen = "pacman_derecha"
        self.frame_index = 0
        self.frame_count = 2  # Número de fotogramas en la hoja de sprites
        

    def change_frame(self):
        # Cambia al siguiente fotograma
        self.frame_index = (self.frame_index + 1) % self.frame_count

    def update(self):
        movimiento = False  # Variable para verificar si hubo movimient
        if pyxel.btn(pyxel.KEY_W):  # Detecta si se presionó la tecla
            self.movement = "pacman_arriba"
            self.pacman_y -= 5
        if pyxel.btn(pyxel.KEY_S):
            self.movement = "pacman_abajo"
            self.pacman_y += 5
        if pyxel.btn(pyxel.KEY_A):
            self.movement = "pacman_izquierda"
            self.pacman_x -= 5
            self.pacman_imagen = "pacman_izquierda"
        if pyxel.btn(pyxel.KEY_D):
            self.movement = "pacman_derecha"
            self.pacman_x += 5
            self.pacman_imagen = "pacman_derecha"
        if pyxel.btnp(pyxel.KEY_F):
            self.pacman_x += 0
            movimiento = True

        # Actualizar la posición del pacman animado
        #self.pacman.x = self.pacman_x
        #self.pacman.y = self.pacman_y
        # Cambiar el fotograma solo si hubo movimiento
        if movimiento:
            self.pacman_imagen = "pacman_f"
            self.change_frame()

    def draw(self):
        # Dibuja el fotograma actual del sprite
        #pyxel.blt(self.x, self.y, 0, self.frame_index * 40, 0, 36, 39, 40)
        if self.pacman_imagen == "pacman_f":
            pyxel.blt(self.pacman_x, self.pacman_y, 0, self.frame_index * 40, 0, 36, 39, 40)
        elif self.pacman_imagen == "pacman_derecha":
            pyxel.blt(self.pacman_x, self.pacman_y, 0, 0, 0, 36, 39, 0)
        elif self.pacman_imagen == "pacman_izquierda":
            pyxel.blt(self.pacman_x, self.pacman_y, 0, 0, 48, 32, 32, 0)
        #AQUÍ HAY QUE HACER DOS IF, UNO PARA CUANDO LA F ESTÉ PULSADA, Y OTRO PARA CUANDO NO, Y HACER DOS MOVIMIENTOS DISTINTOS


