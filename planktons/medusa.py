import pygame
from plankton import Plankton
from random import randint
import window


class Medusa(Plankton):
    def __init__(self):
        super(Medusa, self).__init__()
        self.surf = pygame.Surface((45, 45))
        self.surf.fill((255, 99, 121))
        self.rect = self.surf.get_rect(
            center=(
                randint(window.SCREEN_WIDTH * 0.3, window.SCREEN_WIDTH * 0.7),
                randint(10, window.SCREEN_HEIGHT - 10)
            )
        )

    def reprod(self):
        return Medusa()