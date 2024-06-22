import pygame
import sys
import random
import time

class Stick_Man:
    def __init__(self, screen: pygame.Surface, x, y, image_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5
        self.image = pygame.image.load(image_filename)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1434, 805))
    stickyman_image = Stick_Man(screen, 400, 600, "another_cloud.png")

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_d]:
            stickyman_image.x += 2
        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        stickyman_image.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()