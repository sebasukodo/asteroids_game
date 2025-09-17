import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    fields = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill([0,0,0])

        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)

        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                asteroid.kill()
                player.lives -= 1
                if player.lives <= 0:
                    print("Game over!")
                    print(f"You destroyed {player.kill_count} asteroids while hitting {player.hit_count}")
                    sys.exit()

            for shot in shots:
                if asteroid.check_collisions(shot):
                    dead = asteroid.split()
                    shot.kill()
                    player.hit_count += 1

                    if dead:
                        player.kill_count += 1

        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
