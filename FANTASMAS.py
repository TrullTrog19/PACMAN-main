import pyxel
import random

# Clase base para los fantasmas
class Fantasma:
    def __init__(self, mapa, frames, animation_speed=10, pacman=None):
        # Inicializa la posición del fantasma de manera aleatoria en el mapa
        self.ghost_x, self.ghost_y = mapa.pos_random()
        self.mapa = mapa
        self.pacman = pacman 
        # Lista de frames para la animación
        self.frames = frames
        # Frame actual de la animación
        self.current_frame = 0
        # Dimensiones del fantasma
        self.ancho = 30
        self.alto = 30
        self.animation_speed = animation_speed
        # Temporizador para controlar la animación
        self.timer = 0
        self.huyendo = False  # Indica si el fantasma está huyendo de Pac-Man

    def update(self):
        self.timer += 1
        if self.timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.timer = 0
        self.move()

    def move(self):
        pass  # Método para ser sobrescrito por las subclases

    def draw(self):
        img_x, img_y = self.frames[self.current_frame]
        pyxel.blt(self.ghost_x, self.ghost_y, 2, img_x, img_y, self.ancho, self.alto, 0)

# Clase para el primer tipo de fantasma
class Ghost1(Fantasma):
    def __init__(self, mapa, pacman):
        frames = [(0, 0), (64, 0)]
        super().__init__(mapa, frames, pacman=pacman)

    def move(self):
        velocidad = 2
        new_x = self.ghost_x
        new_y = self.ghost_y

        if self.huyendo:
            if self.pacman.pacman_x < self.ghost_x:
                new_x += velocidad
            elif self.pacman.pacman_x > self.ghost_x:
                new_x -= velocidad
            
            if self.pacman.pacman_y < self.ghost_y:
                new_y += velocidad
            elif self.pacman.pacman_y > self.ghost_y:
                new_y -= velocidad
        else:
            if self.pacman.pacman_x < self.ghost_x:
                new_x -= velocidad
            elif self.pacman.pacman_x > self.ghost_x:
                new_x += velocidad
            
            if self.pacman.pacman_y < self.ghost_y:
                new_y -= velocidad
            elif self.pacman.pacman_y > self.ghost_y:
                new_y += velocidad
        
        if not self.mapa.hitbox_fantasma(new_x, new_y, self.ancho, self.alto):
            self.ghost_x = new_x
            self.ghost_y = new_y
        else:
            self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])

# Clase para el segundo tipo de fantasma
class Ghost2(Fantasma):
    def __init__(self, mapa):
        frames = [(32, 0), (96, 0)]
        super().__init__(mapa, frames)

# Clase para el tercer tipo de fantasma
class Ghost3(Fantasma):
    def __init__(self, mapa):
        frames = [(0, 32), (64, 32)]
        super().__init__(mapa, frames)

# Clase para el cuarto tipo de fantasma
class Ghost4(Fantasma):
    def __init__(self, mapa):
        frames = [(32, 32), (96, 32)]
        super().__init__(mapa, frames)

# Clase para el quinto tipo de fantasma (solo aparece cuando Pac-Man se come frutas)
class Ghost5(Fantasma):
    def __init__(self, mapa, pacman):
        frames = [(0, 64), (64, 64)]
        super().__init__(mapa, frames, pacman=pacman)

    def move(self):
        velocidad = 2
        new_x = self.ghost_x
        new_y = self.ghost_y

        if self.pacman.pacman_x < self.ghost_x:
            new_x += velocidad
        elif self.pacman.pacman_x > self.ghost_x:
            new_x -= velocidad
        
        if self.pacman.pacman_y < self.ghost_y:
            new_y += velocidad
        elif self.pacman.pacman_y > self.ghost_y:
            new_y -= velocidad
        
        if not self.mapa.hitbox_fantasma(new_x, new_y, self.ancho, self.alto):
            self.ghost_x = new_x
            self.ghost_y = new_y
        else:
            self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])
