from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)
    
    def update(self, dt):
        self.position = self.position + self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        split_asteroid = self.radius - ASTEROID_MIN_RADIUS
        new_position = self.position
        new_asteroid1 = Asteroid(new_position.x, new_position.y, split_asteroid)
        new_asteroid2 = Asteroid(new_position.x, new_position.y, split_asteroid)
        new_asteroid1.velocity = new_velocity_1 * 1.2
        new_asteroid2.velocity = new_velocity_2 * 1.2

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



    
