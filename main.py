import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable,updatable)

    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatee in updatable:
            updatee.update(dt)

        for asteroid in asteroids:
            asteroid.update(dt)
            if asteroid.collision_check(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()


        screen.fill((0,0,0))

        for drawee in drawable:
            drawee.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
