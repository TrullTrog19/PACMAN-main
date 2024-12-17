import pyxel
from Mapa import Mapa

#IMPLEMENTAR COLISIONES ESTOY EN ELLO
class AnimatedSprite:
    def __init__(self, x, y):
        self.pacman_x = x
        self.pacman_y = y
        self.ancho = 32
        self.alto = 32
        #self.movement = ""
        self.pacman_imagen = "pacman_derecha"
        self.frame_index = 0
        self.frame_count = 2  # Número de fotogramas en la hoja de sprites
        self.movimiento = False
        

    def change_frame(self):
        # Cambia al siguiente fotograma
        self.frame_index = (self.frame_index + 1) % self.frame_count

    def move(self, direccion, mapa):
        new_x = self.pacman_x
        new_y = self.pacman_y
        if direccion == "pacman_arriba":
            new_y -= 5
            self.pacman_imagen = "pacman_arriba"
            self.movimiento = True
        if direccion == "pacman_abajo":
            new_y += 5
            self.pacman_imagen = "pacman_abajo"
            self.movimiento = True
        if direccion == "pacman_izquierda":
            new_x -= 5
            self.pacman_imagen = "pacman_izquierda"
            self.movimiento = True
        if direccion == "pacman_derecha":
            new_x += 5
            self.pacman_imagen = "pacman_derecha"
            self.movimiento = True
        if not self.movimiento:
            self.pacman_imagen = "pacman_estático"

        if not mapa.hitbox_pacman(new_x, new_y, self.ancho, self.alto):
            self.pacman_x = new_x
            self.pacman_y = new_y

    def update(self, mapa):
        # Variable para verificar si hubo movimient
        self.movimiento = False
        if pyxel.btn(pyxel.KEY_W):  # Detecta si se presionó la tecla
            self.move("pacman_arriba", mapa)
        if pyxel.btn(pyxel.KEY_S):
            self.move("pacman_abajo", mapa)
        if pyxel.btn(pyxel.KEY_A):
            self.move("pacman_izquierda", mapa)
        if pyxel.btn(pyxel.KEY_D):
            self.move("pacman_derecha", mapa)
        if not self.movimiento:
            self.pacman_imagen = "pacman_estático"

        # Verifica si Pac-Man ha comido una bolita
        if mapa.comer_bolita(self.pacman_x, self.pacman_y):
            return True  # Indica que se ha comido una bolita
        return False

    def draw(self):
        # Dibuja el fotograma actual del sprite
        #pyxel.blt(self.x, self.y, 0, self.frame_index * 40, 0, 36, 39, 40)
        #if self.pacman_imagen == "pacman_f":
        #    pyxel.blt(self.pacman_x, self.pacman_y, 0, self.frame_index * 40, 0, 36, 39, 40)
        if self.movimiento == False:
            if self.pacman_imagen == "pacman_estático":
                #pyxel.blt(self.pacman_x, self.pacman_y, 0, 0, 0, 32, 40, 0)
                pyxel.blt(self.pacman_x, self.pacman_y, 0, 0, 0, 30, 30, 0)
        else:
            if self.pacman_imagen == "pacman_derecha":
                pyxel.blt(self.pacman_x, self.pacman_y, 0, 0, 32, 30, 30, 0)
            elif self.pacman_imagen == "pacman_izquierda":
                pyxel.blt(self.pacman_x, self.pacman_y, 0, 32, 32, 30, 30, 0)
            elif self.pacman_imagen == "pacman_arriba":
                pyxel.blt(self.pacman_x, self.pacman_y, 0, 0, 0, 30, 30, 0)
            elif self.pacman_imagen == "pacman_abajo":
                pyxel.blt(self.pacman_x, self.pacman_y, 0, 0, 0, 30, 30, 0)
