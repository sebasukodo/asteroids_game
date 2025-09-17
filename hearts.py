import pygame
import pygame.gfxdraw
from circleshape import CircleShape
from constants import HEART_RADIUS

class Heart(CircleShape):
    def __init__(self, x, y, id):
        super().__init__(x, y, HEART_RADIUS)
        self.heart_exists = False
        self.id = id

    def draw(self, screen):
        if self.heart_exists:
            pygame.gfxdraw.filled_circle(screen,int(self.position[0]), int(self.position[1]), self.radius, [255,0,0])
        else:
            pygame.draw.circle(screen, [255,255,255], self.position, self.radius, 2)

    def update(self, dt):
        pass

    def update_hearts(self, player_lives):
        self.heart_exists = self.id <= player_lives
            