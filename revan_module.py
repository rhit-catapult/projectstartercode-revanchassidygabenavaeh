import pygame
import sys
import random
import time


class StickMan:
    def __init__(self, screen, x, y, image_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("Mike.png")
        # self.speed_x
        # self.speed_y

def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1434, 805))

    stick_man = StickMan(screen, 200, 150, "Mike.png", )

    player_img = pygame.image.load("Mike.png")
    player_rect = player_img.get_rect()
    player_rect.center = (1000 // 2, 805 // 2)

    pygame.surface.Surface(1434, 805)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code



       # pygame.draw.stick_man(screen, (self.x, self.y)





    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
             stick_man.x = stick_man.x + 10
    if pressed_keys[pygame.K_LEFT]:
             stick_man.x = stick_man.x - 10
    if pressed_keys[pygame.K_UP]:
             stick_man.y = stick_man.y - 5
         if pressed_keys[pygame.K_DOWN]:
             stick_man.y = stick_man.y + 5




        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

if __name__ == "__main__":
    main()
