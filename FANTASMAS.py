import pyxel

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

