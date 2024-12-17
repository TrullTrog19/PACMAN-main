import pyxel
from PACMAN import AnimatedSprite
from FANTASMAS import Ghost1, Ghost2, Ghost3, Ghost4, Ghost5
from Mapa import Mapa

# Definimos la clase principal
class PacManApp:
    def __init__(self):
        pyxel.init(512, 512, title="Pac-Man", fps=60, quit_key=pyxel.KEY_Q)
        pyxel.load("assets/resourcesPACMAN.pyxres")
        self.iniciar_nivel()
        pyxel.run(self.update, self.draw)

    def iniciar_nivel(self):
        self.pacman = AnimatedSprite(32, 32)
        self.map1 = Mapa()
        self.bolitas_comidas = 0  # Contador de bolitas comidas
        self.vidas = 3  # Contador de vidas
        self.ghosts = [Ghost1(self.map1, self.pacman), Ghost2(self.map1, self.pacman), Ghost3(self.map1), Ghost4(self.map1)]
        self.fruit_ghost = None  # Fantasma que aparece cuando Pac-Man se come frutas

    def update(self):
        if self.pacman.update(self.map1):
            self.bolitas_comidas += 1  # Incrementa el contador si se ha comido una bolita
        for ghost in self.ghosts:
            ghost.update()
            if self.check_collision(self.pacman, ghost):
                if ghost.huyendo:
                    ghost.ghost_x, ghost.ghost_y = self.map1.pos_random()  # Reaparece en una posición aleatoria
                    ghost.huyendo = False  # Deja de huir
                else:
                    self.vidas -= 1  # Decrementa el contador de vidas si hay colisión con un fantasma
                    if self.vidas == 0:
                        pyxel.quit()  # Termina el juego si se acaban las vidas
                    else:
                        self.iniciar_nivel()  # Reinicia el nivel si aún quedan vidas

        # Actualiza el fantasma de la fruta si existe
        if self.fruit_ghost:
            self.fruit_ghost.update()
            if self.check_collision(self.pacman, self.fruit_ghost):
                self.vidas -= 1  # Decrementa el contador de vidas si hay colisión con el fantasma de la fruta
                if self.vidas == 0:
                    pyxel.quit()  # Termina el juego si se acaban las vidas
                else:
                    self.iniciar_nivel()  # Reinicia el nivel si aún quedan vidas

        # Verifica si Pac-Man ha comido una fruta
        if self.map1.comer_fruta(self.pacman.pacman_x, self.pacman.pacman_y):
            for ghost in self.ghosts:
                ghost.__class__ = Ghost5  # Convierte el fantasma a Ghost5
                ghost.huyendo = True  # Hace que el fantasma huya de Pac-Man

    def draw(self):
        pyxel.cls(0)
        self.map1.draw()
        self.pacman.draw()
        for ghost in self.ghosts:
            ghost.draw()
        if self.fruit_ghost:
            self.fruit_ghost.draw()
        self.draw_text(5, 5, f"Bolitas comidas: {self.bolitas_comidas}", pyxel.COLOR_BLACK)
        self.draw_text(5, 20, f"Vidas: {self.vidas}", pyxel.COLOR_RED)  # Muestra el contador de vidas en la pantalla

    def draw_text(self, x, y, text, color):
        # Dibuja el texto varias veces para simular un tamaño más grande
        scale = 2  # Escala del texto
        for i in range(scale):
            for j in range(scale):
                pyxel.text(x + i, y + j, text, pyxel.COLOR_WHITE)  # Fondo blanco para mayor visibilidad
        pyxel.text(x, y, text, color)  # Texto en color negro

    def check_collision(self, pacman, ghost):
        # Verifica si hay colisión entre Pac-Man y un fantasma
        return (pacman.pacman_x < ghost.ghost_x + ghost.ancho and
                pacman.pacman_x + pacman.ancho > ghost.ghost_x and
                pacman.pacman_y < ghost.ghost_y + ghost.alto and
                pacman.pacman_y + pacman.alto > ghost.ghost_y)

    def pacman_comio_fruta(self):
        # Método para manejar cuando Pac-Man se come una fruta
        self.fruit_ghost = Ghost5(self.map1, self.pacman)  # Crea el fantasma de la fruta

PacManApp()
