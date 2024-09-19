import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        pygame.display.flip()
        screen.fill("black")


        for updatable_object in updatable:
            updatable_object.update(dt)
        
        for drawable_object in drawable:
            drawable_object.draw(screen)
            
            


        
    
        
        
        

        
        
    pygame.tick(60)

if __name__ == "__main__":
    main()
    