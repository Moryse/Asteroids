import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys


def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()
    field = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (projectiles, updatable, drawable)
    AsteroidField.containers = (updatable,)

    clock = pygame.time.Clock()
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        pygame.display.flip()
        screen.fill("black")


        for updatable_object in updatable:
            updatable_object.update(dt)

        for asteroid in projectiles:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit(0)
            
        
        for drawable_object in drawable:
            drawable_object.draw(screen)
            
            


        
    
        
        
        

        
        
    pygame.tick(60)

if __name__ == "__main__":
    main()
    