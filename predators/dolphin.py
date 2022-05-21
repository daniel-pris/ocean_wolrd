import predator
import pygame
from random import randint
import window


class Dolphin(predator.Predator):
    def __init__(self):
        super(Dolphin, self).__init__()
        self.surf = pygame.Surface((80, 40))
        self.surf.fill((175, 80, 225))
        self.rect = self.surf.get_rect(
            center=(
                randint(window.SCREEN_WIDTH * 0.3, window.SCREEN_WIDTH * 0.4),
                randint(50, window.SCREEN_HEIGHT - 50)
            )
        )
