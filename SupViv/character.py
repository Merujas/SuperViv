import pygame
import constants
import os
from world import *
from game_resources import *
from sprites import load_sprites_from_folder

# Mecánicas de Personajes
class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.inventory = {"wood": 0, "stone": 0, "meat": 0} # Inventario inicial
        self.direction = "down"  # Dirección inicial del personaje
        self.current_frame = 0  # Frame actual de la animación    
        self.animation_timer = 0 # Temporizador para la animación
        self.animation_delay = 0.1  # Retraso entre frames (en segundos)
        sprite_folder = os.path.join("SupViv", "assets", "character", "sprites", "Walk") # Carpeta de sprites
        self.sprites = load_sprites_from_folder(sprite_folder) # Cargar sprites desde la carpeta
        self.image = self.sprites[self.direction][self.current_frame]  # Sprite actual

    def get_mask(self):
        # Devuelve la máscara del personaje
        return pygame.mask.from_surface(self.image)
    def update_animation(self, dt):
    # Verifica si hay sprites para la dirección actual
        if not self.sprites[self.direction]:
            print(f"Advertencia: No hay sprites cargados para la dirección '{self.direction}'")
            return

    # Actualiza el frame de la animación según el tiempo transcurrido
        self.animation_timer += dt
        if self.animation_timer >= self.animation_delay:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.sprites[self.direction])
            self.image = self.sprites[self.direction][self.current_frame]

    def draw(self, screen):
        # Dibujar el sprite actual
        screen.blit(self.image, (self.x, self.y))

    # Verificar colisión
    def check_collision(self, obj, new_x, new_y):
        # Calcula el desplazamiento entre el jugador y el objeto
        offset_x = int(obj.x - new_x)
        offset_y = int(obj.y - new_y)

        # Verifica si las máscaras se superponen
        return self.get_mask().overlap(obj.get_mask(), (offset_x, offset_y)) is not None

    def move(self, dx, dy, world):
        # Actualiza la dirección según el movimiento
        if dx < 0:
            self.direction = "left"
        elif dx > 0:
            self.direction = "right"
        elif dy < 0:
            self.direction = "up"
        elif dy > 0:
            self.direction = "down"
        # Calcula las nuevas coordenadas para el eje x
        new_x = self.x + dx * self.speed
        can_move_x = True  # Bandera para indicar si el movimiento en x es válido

        # Verifica colisiones en el eje x
        for tree in world.trees:
            if self.check_collision(tree, new_x, self.y):  # Solo verifica el eje x
                can_move_x = False
                break

        for tree in world.trees2:
            if self.check_collision(tree, new_x, self.y):  # Solo verifica el eje x
                can_move_x = False
                break

        # Actualiza la posición en x si no hay colisión
        if can_move_x:
            self.x = new_x

        # Calcula las nuevas coordenadas para el eje y
        new_y = self.y + dy * self.speed
        can_move_y = True  # Bandera para indicar si el movimiento en y es válido

        # Verifica colisiones en el eje y
        for tree in world.trees:
            if self.check_collision(tree, self.x, new_y):  # Solo verifica el eje y
                can_move_y = False
                break

        for tree in world.trees2:
            if self.check_collision(tree, self.x, new_y):  # Solo verifica el eje y
                can_move_y = False
                break

        # Actualiza la posición en y si no hay colisión
        if can_move_y:
            self.y = new_y
        
        if dx != 0 or dy != 0:
            self.update_animation(0.1)

        # Limita la posición dentro de los límites de la pantalla
        self.x = max(0, min(self.x, constants.width - self.sprites["down"][0].get_width()))
        self.y = max(0, min(self.y, constants.height - self.sprites["down"][0].get_height()))

    def update(self):
        # Obtener teclas presionadas
        keys = pygame.key.get_pressed()

        # Determinar la dirección del movimiento
        if keys[pygame.K_UP]:
            self.direction = "up"
            self.move(0, -1, World)
        elif keys[pygame.K_DOWN]:
            self.direction = "down"
            self.move(0, 1, World)
        elif keys[pygame.K_LEFT]:
            self.direction = "left"
            self.move(-1, 0, World)
        elif keys[pygame.K_RIGHT]:
            self.direction = "right"
            self.move(1, 0, World)
        elif keys[pygame, pygame.K_UP] and keys[pygame.K_LEFT]:
            self.direction = "up_left"
            self.move(-1, -1, World)
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            self.direction = "up_right"
            self.move(1, -1, World)
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.direction = "down_left"
            self.move(-1, 1, World)
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self.direction = "down_right"
            self.move(1, 1, World)
        else:
            self.direction = "down"
            self.move(0, 0, World)
        
