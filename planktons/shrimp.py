import pygame
import self as self

from plankton import Plankton
from random import randint
import window


class Shrimp(Plankton):
    def __init__(self):
        super(Shrimp, self).__init__()
        self.surf = pygame.Surface((15, 25))
        self.surf.fill((71, 154, 55))
        self.rect = self.surf.get_rect(
            center=(
                randint(window.SCREEN_WIDTH * 0.3, window.SCREEN_WIDTH * 0.7),
                randint(10, window.SCREEN_HEIGHT - 10)
            )
        )

    def reprod(self):
        return Shrimp()
