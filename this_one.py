import pygame
import sys
import random
import time

class Stick_Man:
    def __init__(self, screen: pygame.Surface, x, y, image_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.speed_x = 5
        self.speed_y = 0
        self.init_velocity = -20
        self.original_image = pygame.image.load(image_filename)
        self.image = pygame.transform.scale(self.original_image, (self.width, self.height))
        self.acceleration_y = 2

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1434, 805))
    stick_man1 = Stick_Man(screen, 100, 650, "Standing(Middle).png")
    # let's set the framerate
    clock = pygame.time.Clock()
    platforms=[]
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code
        pressed_keys = pygame.key.get_pressed()

        if stick_man1.x > 1134:
            stick_man1.x = 1134
        if stick_man1.x < 0:
            stick_man1.x = 0
        if pressed_keys[pygame.K_d]:
            stick_man1.x += 5
        if pressed_keys[pygame.K_a]:
            stick_man1.x -= 5
        if stick_man1.y >= 688:
            stick_man1.y = 688
            stick_man1.speed_y = 0
            if pressed_keys[pygame.K_w]:
                stick_man1.speed_y = stick_man1.init_velocity
                stick_man1.y += stick_man1.speed_y
        else:
            stick_man1.y += stick_man1.speed_y
            stick_man1.speed_y += stick_man1.acceleration_y
        # TODO: Fill the screen with whatever background color you like!
        screen.fill((0, 0, 0))

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        stick_man1.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()