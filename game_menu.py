import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_MENU

class Rectangle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.position = pygame.Vector2(x, y)
        self.width = width
        self.height = height
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def draw(self, screen, text):

        # make background of rectangle transparent with value 150
        transparent_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 150)) 
        screen.blit(transparent_surface, self.position)

        pygame.draw.rect(screen, COLOR_MENU, self.rect, 2)

        #render text
        text_surface = self.font.render(text, True, COLOR_MENU)
        text_rect = text_surface.get_rect(center=self.rect.center)

        # draw text
        screen.blit(text_surface, text_rect)

    def update(self, dt):
        mouse_click = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if mouse_click[0] and self.in_area(mouse_pos): 
            return True
        return False

    def in_area(self, point):
        return self.rect.collidepoint(point)

def game_menu(screen):

    background_menu = pygame.image.load("img/main_menu.jpg").convert()

    clock = pygame.time.Clock()
    dt = 0

    start_button_width = 300
    start_button_height = 100
    start_button = Rectangle((SCREEN_WIDTH - start_button_width)/2, (SCREEN_HEIGHT - start_button_height)/2, start_button_width, start_button_height)

    exit_button = Rectangle((SCREEN_WIDTH - start_button_width)/2, (SCREEN_HEIGHT - start_button_height + 250)/2, start_button_width, start_button_height)    

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        screen.blit(background_menu, (0,0))

        if start_button.update(dt):
            return True
        start_button.draw(screen, "Start Game")

        if exit_button.update(dt):
            return False
        exit_button.draw(screen, "Exit Game")

        pygame.display.flip()
        dt = clock.tick(60)/1000