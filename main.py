import pygame
import sys
from logger import log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_state
from player import *

def main():
    # Initiating game program
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Grouping templates
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Setting FPS and player movements
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)
    field = AsteroidField()
    player = Player(x, y)

    # Game Looping
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Grouping objects for game loop
        updatable.update(dt)

       # Collision check
        for asteroid in asteroids:
            collision = player.collides_with(asteroid)
            if collision == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for bullet in shots:
                hit = bullet.collides_with(asteroid)
                if hit:
                    log_event("asteroid_shot")
                    asteroid.split()
                    bullet.kill()

	# Clearing screen and draw black
        pygame.Surface.fill(screen, (0,0,0))
        for obj in drawable:
            obj.draw(screen)


        # FPS and game display
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)





if __name__ == "__main__":
    main()
