from circleshape import CircleShape
import constants
from logger import log_state, log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "purple", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= constants.ASTEROID_MIN_RADIUS: #this is a small asteroid... it will just delete it. 
            return []
        else:
            new_radius = self.radius / 2
            log_event("asteroid_split")
            #this is creating two new asteroids with correct radius 

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            #create the two new velocities by rotating the original velocity vector
            angle = random.uniform(20,50)
            asteroid1.velocity = self.velocity.rotate(angle) *1.2
            asteroid2.velocity = self.velocity.rotate(-angle) *1.2

            return [asteroid1, asteroid2]