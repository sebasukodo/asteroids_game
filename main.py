import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game_menu import menu
from game_run import run_game

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("セバスコード's Asteroid Game") 

    while True:
        # Main Menu Screen
        menu(screen)

        # Game Screen
        run_game(screen)


if __name__ == "__main__":
    main()
