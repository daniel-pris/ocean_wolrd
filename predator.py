import animal
import pygame


class Predator(animal.Animal):
    def __init__(self):
        super(Predator, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((128, 102, 255))
        self.speed = 5

    def oldness(self):
        self.health -= 1
        self.speed -= 1
        if self.health <= 0:
            self.kill()

