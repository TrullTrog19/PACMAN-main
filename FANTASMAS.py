import pyxel

# Clase base para los fantasmas
class Fantasma:
    def __init__(self, mapa, frames, animation_speed=10):
        # Inicializa la posición del fantasma de manera aleatoria en el mapa
        self.ghost_x, self.ghost_y = mapa.pos_random()
        # Lista de frames para la animación
        self.frames = frames
        # Frame actual de la animación
        self.current_frame = 0
        # Dimensiones del fantasma
        self.ancho = 30
        self.alto = 30
        # Velocidad de la animación (cuanto mayor, más lenta)
        self.animation_speed = animation_speed
        # Temporizador para controlar la animación
        self.timer = 0

    def update(self):
        # Incrementa el temporizador
        self.timer += 1
        # Si el temporizador alcanza la velocidad de animación, cambia de frame
        if self.timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.timer = 0

    def draw(self):
        # Obtiene las coordenadas del frame actual
        img_x, img_y = self.frames[self.current_frame]
        # Dibuja el fantasma en la pantalla
        pyxel.blt(self.ghost_x, self.ghost_y, 2, img_x, img_y, 32, 32, 0)

# Clase para el primer tipo de fantasma
class Ghost1(Fantasma):
    def __init__(self, mapa):
        # Coordenadas de los frames para la animación
        frames = [(0, 0), (64, 0)]
        # Llama al constructor de la clase base
        super().__init__(mapa, frames)

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
