import pygame
from game_menu import Rectangle
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_MENU

class StatsWindow(Rectangle):
    def __init__(self, x, y, width, height, stats_list):
        super().__init__(x, y, width, height)
        self.stats_list = stats_list

    def draw(self, screen, text):

        # make background of rectangle transparent with value 150
        transparent_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 150))
        screen.blit(transparent_surface, self.position)

        stats_text = self.get_stats().split("\n")

        line_height = self.font.get_linesize()
        total_line_heigth = len(stats_text)*line_height

        y = self.rect.y + (self.rect.height - total_line_heigth) // 2

        # render text and draw text
        for line in stats_text:
            text_surface = self.font.render(line, True, COLOR_MENU)
            text_rect = text_surface.get_rect(centerx=self.rect.centerx, y=y)
            screen.blit(text_surface, text_rect)
            y += line_height

    def update(self, dt):
        pass
    
    def get_stats(self):
        text = "=============STATS=============\n"
        text += f"Final Score: {self.stats_list[4]}\n\n"
        text += f"- You hit {self.stats_list[0]} asteroids.\n"
        text += f"- You destroyed {self.stats_list[1]} small asteroids.\n"
        text += f"- You fired {self.stats_list[2]} shots in total.\n"
        text += f"- You earned {self.stats_list[3]} extra lives.\n"
        return text

def respawn_menu(screen, player_stats):

    background_respawn = pygame.image.load("img/respawn_menu.jpg").convert()

    clock = pygame.time.Clock()
    dt = 0

    button_width = 250
    button_height = 75
    start_button = Rectangle((SCREEN_WIDTH - button_width) // 2, (SCREEN_HEIGHT - button_height + 200) // 2, button_width, button_height)
    exit_button = Rectangle((SCREEN_WIDTH - button_width) // 2, (SCREEN_HEIGHT - button_height + 400) // 2, button_width, button_height)
    
    stats_width = 600
    stats_heigth = 260
    stats_window = StatsWindow((SCREEN_WIDTH - stats_width)// 2, (SCREEN_HEIGHT - stats_heigth - 200)// 2,  stats_width, stats_heigth, player_stats)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        screen.blit(background_respawn, (0,0))

        stats_window.draw(screen, "Stats")

        if start_button.update(dt):
            return True
        start_button.draw(screen, "Restart")

        if exit_button.update(dt):
            return False
        exit_button.draw(screen, "Back to Menu")

        pygame.display.flip()
        dt = clock.tick(60)/1000