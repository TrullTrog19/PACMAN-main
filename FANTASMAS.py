import pyxel
#PARA QUE LOS FANTASMAS HEREDEN DE LA CLASE
class Fantasma():
    def __init__(self):
        pass



class Ghost1:
    def __init__(self):
        self.ghost_x = 120
        self.ghost_y = 120
        
    def update(self):
        pass
    def draw(self):
        
        pyxel.blt(self.ghost_x, self.ghost_y, 2, 0, 0, 32, 32, 0)

class Ghost2:
    def __init__(self):
        self.ghost_x = 220
        self.ghost_y = 120
        
    def update(self):
        pass
    def draw(self):
        
        pyxel.blt(self.ghost_x, self.ghost_y, 2, 32, 0, 32, 32, 0)


class Ghost3:
    def __init__(self):
        self.ghost_x = 220
        self.ghost_y = 60
        
    def update(self):
        pass
    def draw(self):
        
        pyxel.blt(self.ghost_x, self.ghost_y, 2, 0, 32, 32, 32, 0)

class Ghost4:
    def __init__(self):
        self.ghost_x = 10
        self.ghost_y = 50
        
    def update(self):
        pass
    def draw(self):
        
        pyxel.blt(self.ghost_x, self.ghost_y, 2, 32, 32, 32, 32, 0)

#ESTO ES PARA CAMBIAR DE FRAME
#class AnimatedSpriteFAN:
 #   def __init__(self, x, y):
#        self.x = x
#        self.y = y
#        self.frame_index = 0
#        self.frame_count = 2  # Número de fotogramas en la hoja de sprites

#    def change_frame(self):
        # Cambia al siguiente fotograma
#        self.frame_index = (self.frame_index + 1) % self.frame_count

#    def draw(self):
        # Dibuja el fotograma actual del sprite
#        pyxel.blt(self.x, self.y, 2, self.frame_index * 16, 0, 16, 16, 0)