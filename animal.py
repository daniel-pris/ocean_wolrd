import pygame
from window import SCREEN_WIDTH
from window import SCREEN_HEIGHT
import random
from pygame.locals import (
    K_SPACE
)


class Animal(pygame.sprite.Sprite):
    def __init__(self):
        super(Animal, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((10, 10, 10))
        self.direction = 1
        self.speed = 3
        self.health = 20

    def move(self, pressed_keys):

        if pressed_keys[K_SPACE]:
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

            if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
                self.direction *= -1

            if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
                self.direction *= -1

            self.rect.left += self.speed * self.direction
            self.rect.top += random.choice([self.speed * self.direction, 0, 0, 0, 0])
