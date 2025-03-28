

import pygame  
import sys
import pygameAssets
import constants
from character import Character
from world import World
pygame.init()


screen = pygame.display.set_mode((constants.width, constants.height))

pygame.display.set_caption("SupViv")

# def main():

def main():
    clock = pygame.time.Clock()
    world = World(constants.width, constants.height)
    character = Character(constants.width // 2, constants.height // 2)

    while True:
        dt = clock.tick(60) / 1000.0  # Tiempo transcurrido en segundos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.move(-1, 0, world)
        if keys[pygame.K_RIGHT]:
            character.move(1, 0, world)
        if keys[pygame.K_UP]:
            character.move(0, -1, world)
        if keys[pygame.K_DOWN]:
            character.move(0, 1, world)

        # Actualiza la animación del personaje
        character.update_animation(dt)

        # Dibuja el mundo y el personaje
        screen.fill(constants.green)
        world.draw(screen)
        character.draw(screen)
        pygame.display.flip() 
        
if __name__ == "__main__":
    main()