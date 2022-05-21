import predator
import pygame
from random import randint
import window


class Shark(predator.Predator):
    def __init__(self):
        super(Shark, self).__init__()
        self.surf = pygame.Surface((90, 45))
        self.surf.fill((88, 134, 176))
        self.speed = 10
        self.rect = self.surf.get_rect(
            center=(
                randint(window.SCREEN_WIDTH * 0.1, window.SCREEN_WIDTH * 0.2),
                randint(50, window.SCREEN_HEIGHT - 50)
            )
        )