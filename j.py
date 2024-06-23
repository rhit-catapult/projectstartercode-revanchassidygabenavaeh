import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Mike:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("IMG_1733-removebg-preview.png")
        self.rect = self.image.get_rect()  # Corrected this line
        self.rect.topleft = (self.x, self.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)

def main():
    # Initialize pygame
    pygame.init()

    # Create a screen
    screen_width = 1434
    screen_height = 805
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Cool Project")

    mike_object = Mike(screen, 100, 100)  # Pass screen object correctly

    # Set the framerate
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the screen with a background color
        screen.fill((60, 60, 132))

        pygame.draw.rect(screen, BLACK, (100, 505, 300, 20))
        pygame.draw.rect(screen, BLACK, (550, 250, 300, 20))
        pygame.draw.rect(screen, BLACK, (800, 600, 300, 20))
        pygame.draw.rect(screen, BLACK, (1300, 450, 300, 20))
        pygame.draw.rect(screen, BLACK, (0, 775, 1500, 30))

        mike_object.draw()

        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
