import pygame
import pygame.mixer
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_BG_VOLUME
from game_menu import game_menu
from respawn_menu import respawn_menu
from game_run import run_game

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("セバスコード's Asteroid Game") 

    # adding background music
    pygame.mixer.music.load("sounds/menu_bg.ogg")
    pygame.mixer.music.set_volume(GAME_BG_VOLUME)
    pygame.mixer.music.play(-1)

    running = True
    while running:
        # Main Menu Screen

        exit_game = game_menu(screen)
        if not exit_game:
            break

        respawn = True
        while respawn:
            # run game
            player_stats = run_game(screen)

            # respawn game
            respawn = respawn_menu(screen, player_stats)

        # mouse input after pressing back to menu causes game to exit without delay
        pygame.time.delay(150)

    pygame.mixer.music.stop()
    sys.exit()

if __name__ == "__main__":
    main()
