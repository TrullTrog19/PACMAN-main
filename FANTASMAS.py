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
        self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])
        # Temporizador para controlar la animación
        self.timer = 0
        

    def update(self):
        # Incrementa el temporizador
        self.timer += 1
        # Si el temporizador alcanza la velocidad de animación, cambia de frame
        if self.timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.timer = 0
        self.move_general()
    
    def pacman_visto(self):
        #Ver pacman
        if self.pacman:
            if self.ghost_x == self.pacman.pacman_x:
                if self.ghost_y < self.pacman.pacman_y:
                    self.direccion = "abajo"
                else:
                    self.direccion = "arriba"
                return True
            elif self.ghost_y == self.pacman.pacman_y:
                if self.ghost_x < self.pacman.pacman_x:
                    self.direccion = "derecha"
                else:
                    self.direccion = "izquierda"
                return True
        return False

    def move_general(self):
        velocidad = 3 #justa la velocidad de movimiento
        new_x = self.ghost_x
        new_y = self.ghost_y

        if self.direccion == "arriba":
            new_y -= velocidad
        elif self.direccion == "abajo":
            new_y += velocidad
        elif self.direccion == "izquierda":
            new_x -= velocidad
        elif self.direccion == "derecha":
            new_x += velocidad

        if not self.mapa.hitbox_fantasma(new_x, new_y, self.ancho, self.alto):
            self.ghost_x = new_x
            self.ghost_y = new_y
        else:
            self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])


    def draw(self):
        # Obtiene las coordenadas del frame actual
        img_x, img_y = self.frames[self.current_frame]
        pyxel.blt(self.ghost_x, self.ghost_y, 2, img_x, img_y, self.ancho, self.alto, 0)

# Clase para el primer tipo de fantasma
class Ghost1(Fantasma):
    def __init__(self, mapa, pacman):
        frames = [(0, 0), (64, 0)]
        super().__init__(mapa, frames, pacman=pacman)

    def move(self):
        velocidad = 3
        movimiento = False
        new_x = self.ghost_x
        new_y = self.ghost_y
        if self.pacman_visto():
            if self.direccion == "izquierda" or self.direccion == "derecha":
                if self.pacman.pacman_x < self.ghost_x:
                    new_x = self.ghost_x - velocidad
                    if not self.mapa.hitbox_fantasma(new_x, self.ghost_y, self.ancho, self.alto):
                        self.ghost_x = new_x
                        moved = True
                elif self.pacman.pacman_x > self.ghost_x:
                    new_x = self.ghost_x + velocidad
                    if not self.mapa.hitbox_fantasma(new_x, self.ghost_y, self.ancho, self.alto):
                        self.ghost_x = new_x
                        moved = True
            elif self.direccion == "arriba" or self.direccion == "abajo":
                if self.pacman.pacman_y < self.ghost_y:
                    new_y = self.ghost_y - velocidad
                    if not self.mapa.hitbox_fantasma(self.ghost_x, new_y, self.ancho, self.alto):
                        self.ghost_y = new_y
                        moved = True
                elif self.pacman.pacman_y > self.ghost_y:
                    new_y = self.ghost_y + velocidad
                    if not self.mapa.hitbox_fantasma(self.ghost_x, new_y, self.ancho, self.alto):
                        self.ghost_y = new_y
                        moved = True
        if not movimiento:
            self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])
            self.move_general()

# Clase para el segundo tipo de fantasma
class Ghost2(Fantasma):
    def __init__(self, mapa, pacman):
        frames = [(32, 0), (96, 0)]
        super().__init__(mapa, frames, pacman=pacman)
    
    def move(self):
        moved = False
        velocidad = 3

        if self.pacman:
            # Calcular la dirección hacia Pacman
            dir_x = self.pacman.pacman_x - self.ghost_x
            dir_y = self.pacman.pacman_y - self.ghost_y

            # Normalizar el vector de dirección
            if dir_x != 0:
                dir_x = dir_x / abs(dir_x)
            if dir_y != 0:
                dir_y = dir_y / abs(dir_y)

            # Mover el fantasma en la dirección de Pacman
            new_x = self.ghost_x + dir_x * velocidad
            new_y = self.ghost_y + dir_y * velocidad

            if not self.mapa.hitbox_fantasma(new_x, new_y, self.ancho, self.alto):
                self.ghost_x = new_x
                self.ghost_y = new_y
            else:
                # Si hay un muro en la dirección de Pacman, intentar moverse en la otra dirección
                if not self.mapa.hitbox_fantasma(new_x, self.ghost_y, self.ancho, self.alto):
                    self.ghost_x = new_x
                elif not self.mapa.hitbox_fantasma(self.ghost_x, new_y, self.ancho, self.alto):
                    self.ghost_y = new_y

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
