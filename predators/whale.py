import predator
import pygame
from random import randint
import window


class Whale(predator.Predator):
    def __init__(self):
        super(Whale, self).__init__()
        self.surf = pygame.Surface((120, 60))
        self.surf.fill((97, 124, 138))
        self.speed = 4
        self.rect = self.surf.get_rect(
            center=(
                randint(window.SCREEN_WIDTH * 0.8, window.SCREEN_WIDTH * 0.9),
                randint(50, window.SCREEN_HEIGHT - 50)
            )
        )