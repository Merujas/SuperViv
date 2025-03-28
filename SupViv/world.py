import pygame
import constants
import random
import os
from game_resources import Tree
from game_resources import Stones
from game_resources import Meet
from game_resources import Tree2
from game_resources import Grass
#Caracteristicas del mundo
class World:
    def __init__(self, width, height):
        self.width = width  #Ancho
        self.height = height #Alto
        self.grass = pygame.image.load(os.path.join("SupViv", "assets", "objects", "Grass.png")).convert_alpha()
        self.grass = pygame.transform.scale(self.grass, (constants.Grass, constants.Grass))
        self.trees = [Tree(random.randint(0, width-30),
                           random.randint(0, height-30)) for _ in range(10)] #Arboles
        self.trees2 = [Tree2(random.randint(0, width-30),
                            random.randint(0, height-30)) for _ in range(10)] #Arboles2
        self.stones = [Stones(random.randint(0, width-20),
                             random.randint(0, height-20)) for _ in range(10)] #Piedras
        self.meet = [Meet(random.randint(0, width-10),
                          random.randint(0, height-10)) for _ in range(10)] #Carne

#Dibuja el mundo
    def draw(self, screen):
        for y in range(0, self.height, constants.Grass):
            for x in range(0, self.width, constants.Grass):
                screen.blit(self.grass, (x, y))

        for stone in self.stones:
            stone.draw(screen)
        for tree in self.trees:
            tree.draw(screen)
        for tree2 in self.trees2:
            tree2.draw(screen)
        for meat in self.meet:
            meat.draw(screen)
  


       
        

#Mueve el mundo


