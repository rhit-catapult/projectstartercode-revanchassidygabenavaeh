import pygame
import sys
import random
class Stickman():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.velo_y = -50
        self.ace_y = 2
        self.speed_y = 0

    def draw(self):
        pygame.draw.circle(self.screen,(0,0,0), (self.x,self.y),40)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            self.x += 3
        if pressed_keys[pygame.K_LEFT]:
            self.x -= 3
        if pressed_keys[pygame.K_UP]:
            self.speed_y = self.velo_y
            if self.y >= 688:
                self.y = 688
                self.speed_y = 0
            else:
                self.y += self.speed_y
                self.speed_y += self.ace_y






def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("stickman2")
    screen = pygame.display.set_mode((1434, 805))
    test_man = Stickman(screen, screen.get_width()/2, screen.get_height()/2) # creating stickman outside of loop so its stored

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code


        screen.fill((255, 255, 255))

        # TODO: Add your project code

        test_man.draw()
        test_man.move()





        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

if __name__ == "__main__":
  main()
