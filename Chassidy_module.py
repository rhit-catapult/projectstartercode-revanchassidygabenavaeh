import pygame
import sys

WHITE= (225, 225,225)
BLACK=(0,0,0)
class Mike:
    def __init__(self, screen: pygame.Surface, x, y, width, height):
        self.screen= screen
        self.x= x
        self.y= y
        self.width= width
        self.height=height
        self.original_image = pygame.image.load("IMG_1733-removebg-preview.png")
        self.image= pygame.transform.scale(self.original_image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)


    def draw(self):
        self.screen.blit(self.image, self.rect)

def main():
      # turn on pygame
        pygame.init()

        # create a screen
        # TODO: Change the size of the screen as you see fit!
        screen_width = 1434
        screen_height = 805
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Cool Project")

        mike_width=100
        mike_height=100
        mike_object = Mike(screen, 100,650, mike_width, mike_height)

        # let's set the framerate
        clock = pygame.time.Clock()

        running= True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # TODO: Add you events code

            # TODO: Fill the screen with whatever background color you like!
            screen.fill((60, 60, 132))

            pygame.draw.rect(screen, BLACK, (100, 505, 300, 20))
            pygame.draw.rect(screen,  BLACK, (550, 250, 300, 20))
            pygame.draw.rect(screen,  BLACK, (800, 600, 300, 20))
            pygame.draw.rect(screen,  BLACK, (1300, 450, 300, 20))
            pygame.draw.rect(screen, BLACK, (0, 775, 1500, 30))

            mike_object.draw()

            # don't forget the update, otherwise nothing will show up!
            pygame.display.update()

            clock.tick(60)

if __name__ == "__main__":
    main()
