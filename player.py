import pygame
from constants import *
from circleshape import CircleShape
from asteroid import Shot

PLAYER_SHOOT_COOLDOWN = 0.3


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_timer = max(self.shot_timer - dt, 0)
        self.rotation = self.rotation % 360
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        rotated_vector = pygame.Vector2(0, 1)
        rotated_vector = rotated_vector.rotate(self.rotation)
        rotated_vector = rotated_vector * PLAYER_SHOOT_SPEED
        if self.shot_timer <= 0:
            shot = Shot(self.position, rotated_vector)
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
            return shot
        return None
