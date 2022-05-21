from animal import Animal
import pygame


class Plankton(Animal):
    def __init__(self):
        super(Plankton, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((12, 156, 25))



