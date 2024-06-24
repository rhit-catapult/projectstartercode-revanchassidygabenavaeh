import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move Character with Arrow Keys")

# Load images
player_img = pygame.image.load('Mike.png')  # Replace 'player.png' with your image file
stick_man = player_img.get_rect()
stick_man.center = (screen_width // 2, screen_height // 2)


CHAR_WIDTH, CHAR_HEIGHT = 40, 60
CHAR_COLOR = (50, 50, 200)
CHAR_INITIAL_X = screen_width // 2 - CHAR_WIDTH // 2
CHAR_INITIAL_Y = screen_height - CHAR_HEIGHT - 50
CHAR_JUMP_SPEED = 10
GRAVITY = 0.6


class Character:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, screen_width // 2, screen_height // 2)
        self.vel_y = 0  # velocity in the y direction

    def jump(self):
        self.vel_y = -CHAR_JUMP_SPEED

    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y



character = Character(CHAR_INITIAL_X, CHAR_INITIAL_Y)
# Set initial movement variables
player_speed = 5
player_dx = 0
player_dy = 0

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_dx = -player_speed
            elif event.key == pygame.K_RIGHT:
                player_dx = player_speed
            elif event.key == pygame.K_UP:
                player_dy = -player_speed
            elif event.key == pygame.K_DOWN:
                player_dy = player_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_dy = 0

    character = Character(CHAR_INITIAL_X, CHAR_INITIAL_Y)
    # Update player position
    stick_man.x += player_dx
    stick_man.y += player_dy

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                character.jump()

    # Apply gravity
    character.apply_gravity()

    # Boundary checking (optional)
    if stick_man.left < 0:
        stick_man.left = 0
    elif stick_man.right > screen_width:
        stick_man.right = screen_width
    if stick_man.top < 0:
        stick_man.top = 0
    elif stick_man.bottom > screen_height:
        stick_man.bottom = screen_height

    # Fill the screen with background color
    screen.fill(white)

    # Draw player on the screen
    screen.blit(player_img, stick_man)


    def draw(self, screen):
        pygame.draw.rect(screen, CHAR_COLOR, self.rect)


    #character.draw(screen)
    # Update the display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
