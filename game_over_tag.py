import pygame
import sys
import button_start

def main():
    pygame.init()
    pygame.display.set_caption("Testing the Game Over Screen")
    screen = pygame.display.set_mode((1640, 650))
    run_game_over_loop(screen, True)


def run_game_over_loop(screen, did_player1_win):
    clock = pygame.time.Clock()

    #lose_sound = pygame.mixer.Sound("sounds/lose.wav")
    #lose_sound.play()


    if  did_player1_win:
        game_over_image = pygame.image.load("RedPlayerWins.png")
    else:
        game_over_image = pygame.image.load("BluePlayerWins.png")


    replay_button = button_start.TextButton(screen, screen.get_width() / 2, screen.get_height() - 150, "Play Again?")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if replay_button.is_clicked_by(event.pos):
                    print("You clicked the button.  You will now leave this screen.")
                    return
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))

        screen.blit(game_over_image, (screen.get_width() / 2 - game_over_image.get_width() / 2, 150))
        replay_button.draw()

        pygame.display.update()


if __name__ == "__main__":
    main()
