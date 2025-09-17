import pygame
from game_menu import Button
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def respawn_menu(screen, player_stats):
    clock = pygame.time.Clock()
    dt = 0

    start_button_width = 300
    start_button_height = 100
    start_button = Button((SCREEN_WIDTH - start_button_width)/2, (SCREEN_HEIGHT - start_button_height)/2, start_button_width, start_button_height)

    exit_button = Button((SCREEN_WIDTH - start_button_width)/2, (SCREEN_HEIGHT - start_button_height + 250)/2, start_button_width, start_button_height)    

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        screen.fill([0,0,0])

        if start_button.update(dt):
            return True
        start_button.draw(screen, "Restart")

        if exit_button.update(dt):
            return False
        exit_button.draw(screen, "Back to Menu")

        pygame.display.flip()
        dt = clock.tick(60)/1000