import pygame
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

    # Setting FPS and player movements
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    # Game Looping
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0))

        # Grouping objects for game loop 
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)







if __name__ == "__main__":
    main()
