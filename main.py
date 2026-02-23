import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drw in drawable:
            drw.draw(screen)
        delta_time = clock.tick(60)
        dt = delta_time / 1000
        updatable.update(dt=dt)
        for obj in asteroids:
            for shot in shots:
                if shot.collides_with(obj):
                    log_event("asteroid_shot")
                    shot.kill()
                    obj.split()
            if player.collides_with(obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()


if __name__ == '__main__':
    main()
