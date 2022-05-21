import pygame
import window
import pickle
from predators.whale import Whale
from predators.shark import Shark
from predators.dolphin import Dolphin
from planktons.medusa import Medusa
from planktons.larva import Larva
from planktons.shrimp import Shrimp
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    K_SPACE,
    K_a,
    K_r,
    QUIT
)

pygame.display.set_caption('Ocean World')
pygame.init()

screen = pygame.display.set_mode([window.SCREEN_WIDTH, window.SCREEN_HEIGHT])
# Set up the clock for a decent frame rate
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
plank = pygame.sprite.Group()
predt = pygame.sprite.Group()


def add_shark():
    shark = Shark()
    shark.add(all_sprites, predt)


def add_whale():
    whale = Whale()
    whale.add(all_sprites, predt)


def add_dolphin():
    dolphin = Dolphin()
    dolphin.add(all_sprites, predt)


def add_predts():
    add_shark()
    add_dolphin()
    add_whale()


def add_medusa():
    medusa = Medusa()
    medusa.add(all_sprites, plank)


def add_larva():
    larva = Larva()
    larva.add(all_sprites, plank)


def add_shrimp():
    shrimp = Shrimp()
    shrimp.add(all_sprites, plank)


def add_planks():
    add_shrimp()
    add_larva()
    add_medusa()


data = {
    'pred': 0,
    'plan': 0,
    'all': 0
}


def reset_data():
    f = open('datafile.bin', 'wb')
    pickle.dump(data, f)
    f.close()


def save_data():
    f = open('datafile.bin', 'wb')
    data['pred'] = int(len(predt.sprites()) / 3)
    data['plan'] = int(len(plank.sprites()) / 3)
    data['all'] = len(all_sprites.sprites())
    pickle.dump(data, f)
    print(data)
    f.close()


f = open('datafile.bin', 'rb')
data_r = pickle.load(f)
print(data_r)
for i in range(data_r['pred']):
    add_predts()
for i in range(data_r['plan']):
    add_planks()
f.close()


def add_sprites():
    while True:
        try:
            ent = int(input("Enter the number of clones of the species of predator(up to 5): "))
            if ent < 0 or ent > 5:
                print("Input from 0 to 5:")
                continue
            break
        except ValueError:
            print("That's not a valid option!")

    for i in range(ent):
        add_predts()

    while True:
        try:
            ent = int(input("Enter the number of clones of the species of plankton(up to 10): "))
            if ent < 0 or ent > 10:
                print("Enter from 0 to 10:")
                continue
            break
        except ValueError:
            print("That's not a valid option!")

    for i in range(ent):
        add_planks()


print("Welcome to Ocean World!\nPress:\n[a] to add animals\n[Esc] to exit\n[Space] to do step\n[r] to reset data")

MAX_ANIMALS = 64

running = True
print("Start:")
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                save_data()
                print("You exited with saving data.")
                running = False
            if event.key == K_r:
                reset_data()
                all_sprites.empty()
                print("Data erased, all animals died!")
            if event.key == K_a:
                if len(all_sprites.sprites()) < MAX_ANIMALS :
                    add_sprites()
                else:
                    print("Too many animals! Try later...")
            if event.key == K_SPACE:
                print("A step was taken: plankton multiplied, and predators grew old...")
                if len(all_sprites.sprites()) < MAX_ANIMALS:
                    for entity in plank:
                        baby = entity.reprod()
                        baby.add(all_sprites, plank)
                for ent in predt:
                    ent.oldness()

        elif event.type == QUIT:
            save_data()
            print("See you soon!")
            running = False

    pressed_keys = pygame.key.get_pressed()

    screen.fill((192, 235, 231))

    # Draw all sprites
    for entity in all_sprites:
        entity.move(pressed_keys)
        screen.blit(entity.surf, entity.rect)

    pygame.sprite.groupcollide(plank, predt, True, False)

    # Flip the display
    pygame.display.flip()
    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

pygame.quit()