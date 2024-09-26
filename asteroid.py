from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)
    
    def update(self, dt):
        self.position = self.position + self.velocity * dt

class Shot(CircleShape):
    def __init__(self, pos, velocity, *groups):
        x, y = pos
        radius = 5
        super().__init__(x, y, radius, *groups)
        self.position = pos
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, width= 2)

    def update(self, dt):
        self.position = self.position + self.velocity * dt



    
