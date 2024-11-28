import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        newAsteroid = random.uniform(20, 50)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        
        velocityA = self.velocity.rotate(newAsteroid)
        velocityB = self.velocity.rotate(-newAsteroid)

        asteroidA = Asteroid(self.position.x, self.position.y, newRadius)
        asteroidA.velocity = velocityA * 1.2
        
        asteroidB = Asteroid(self.position.x, self.position.y, newRadius)
        asteroidB.velocity = velocityB * 1.2


        
        

