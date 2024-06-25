import pygame
import os

pygame.init()

# Set up the display (window)
screen = pygame.display.set_mode((800, 600))  # Example window size
pygame.display.set_caption('Pygame Animation')

# Define some colors
WHITE = (255, 255, 255)

# Load all frames for different animations
frame_filenames_idle = ['unnamed(1).png']  # Example idle frames
frame_filenames_walk = ['hit(red) (1).png']  # Example walk frames

frames_idle = []
frames_walk = []

for filename in frame_filenames_idle:
    frame = pygame.image.load(os.path.join('assets', filename)).convert_alpha()
    frames_idle.append(frame)

for filename in frame_filenames_walk:
    frame = pygame.image.load(os.path.join('assets', filename)).convert_alpha()
    frames_walk.append(frame)

# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animation_state = 'idle'  # Initial animation state
        self.image_frames = frames_idle  # Start with idle frames
        self.current_frame = 0  # Index of the current frame
        self.image = self.image_frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Example starting position

    def update(self):
        # Update animation frame
        self.current_frame = (self.current_frame + 1) % len(self.image_frames)
        self.image = self.image_frames[self.current_frame]

    def change_animation(self, new_state):
        # Change animation frames based on new_state
        if new_state == 'idle':
            self.animation_state = 'idle'
            self.image_frames = frames_idle
        elif new_state == 'walk':
            self.animation_state = 'walk'
            self.image_frames = frames_walk
        self.current_frame = 0  # Reset frame index

# Initialize game objects
player = Player()
all_sprites = pygame.sprite.Group(player)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Change animation to 'walk' when spacebar is pressed
                player.change_animation('walk')

    # Update
    all_sprites.update()

    # Draw / Render
    screen.fill(WHITE)  # Clear screen
    all_sprites.draw(screen)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10)  # Adjust as needed for the animation speed

pygame.quit()
