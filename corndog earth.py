import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moon Destruction")

# Load images
moon_img = pygame.image.load('moon.jpg')  # Replace with your moon image file
earth_img = pygame.image.load('earth.jpg')  # Replace with your earth image file
dynamite_img = pygame.image.load('dynamite.jpg')  # Replace with your dynamite image file
corndog_img = pygame.image.load('../pygamestartercode-rhit-naveR/00-IntroToPython/replit_play_example/corndog.jpg')  # Replace with your corndog image file

# Game fonts
font = pygame.font.Font(None, 36)

# Player constants
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_COLOR = BLUE
PLAYER_START_X = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
PLAYER_START_Y = SCREEN_HEIGHT - PLAYER_HEIGHT - 20
PLAYER_SPEED = 5

# Dynamite constants
DYNAMITE_WIDTH = 30
DYNAMITE_HEIGHT = 30
DYNAMITE_COLOR = RED
DYNAMITE_SPEED = 10

# Corndog constants
CORNDOG_WIDTH = 40
CORNDOG_HEIGHT = 40
CORNDOG_COLOR = YELLOW

# Define a class for the Player
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)

    def move_left(self):
        self.rect.x -= PLAYER_SPEED

    def move_right(self):
        self.rect.x += PLAYER_SPEED

    def throw_dynamite(self):
        dynamite = Dynamite(self.rect.centerx - DYNAMITE_WIDTH // 2, self.rect.top)
        dynamites.append(dynamite)

    def eat_corndog(self):
        corndog = Corndog(random.randint(0, SCREEN_WIDTH - CORNDOG_WIDTH), random.randint(0, SCREEN_HEIGHT - CORNDOG_HEIGHT))
        corndogs.append(corndog)

# Define a class for Dynamite
class Dynamite:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, DYNAMITE_WIDTH, DYNAMITE_HEIGHT)

    def move(self):
        self.rect.y -= DYNAMITE_SPEED

    def draw(self, screen):
        screen.blit(dynamite_img, self.rect)

# Define a class for Corndog
class Corndog:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CORNDOG_WIDTH, CORNDOG_HEIGHT)

    def draw(self, screen):
        screen.blit(corndog_img, self.rect)

# Create player instance
player = Player(PLAYER_START_X, PLAYER_START_Y)

# Lists to store dynamites and corndogs
dynamites = []
corndogs = []

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_SPACE:
                player.throw_dynamite()
            elif event.key == pygame.K_5:
                player.eat_corndog()

    # Update dynamite positions and remove dynamites that go off screen
    for dynamite in dynamites:
        dynamite.move()
        if dynamite.rect.bottom < 0:
            dynamites.remove(dynamite)

    # Fill the screen with background color
    screen.fill(WHITE)

    # Draw moon and earth
    screen.blit(moon_img, (0, 0))
    screen.blit(earth_img, (SCREEN_WIDTH - earth_img.get_width(), 0))

    # Draw player
    player.draw(screen)

    # Draw dynamites
    for dynamite in dynamites:
        dynamite.draw(screen)

    # Draw corndogs
    for corndog in corndogs:
        corndog.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
