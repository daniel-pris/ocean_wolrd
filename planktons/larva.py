import pygame
from plankton import Plankton
from random import randint
import window


class Larva(Plankton):
    def __init__(self):
        super(Larva, self).__init__()
        self.surf = pygame.Surface((25, 25), 3)
        self.surf.fill((150, 156, 25))
        self.rect = self.surf.get_rect(
            center=(
                randint(window.SCREEN_WIDTH * 0.3, window.SCREEN_WIDTH * 0.7),
                randint(10, window.SCREEN_HEIGHT - 10)
            )
        )

    def reprod(self):
        return Larva()