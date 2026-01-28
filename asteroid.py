from circleshape import CircleShape
import constants
from logger import log_state, log_event
import pygame
import random
import math

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
         # ADD THE LUMPY SHAPE CODE HERE
        self.shape_points = []
        num_points = random.randint(8, 12)

        #random colors for each asteroid
        self.color = (random.randint(100,255), random.randint(100,255), random.randint(100,255))

        for i in range(num_points):
            angle = (360 / num_points) * i
            # Random variation in radius for lumpiness (70% to 130% of radius)
            lumpy_radius = self.radius * random.uniform(0.7, 1.3)
            
            x_offset = lumpy_radius * math.cos(math.radians(angle))
            y_offset = lumpy_radius * math.sin(math.radians(angle))
            self.shape_points.append((x_offset, y_offset))
        

    def draw(self, screen):
        # UPDATE YOUR DRAW METHOD HERE
        points = [(self.position.x + x, self.position.y + y) 
                  for x, y in self.shape_points]
        #pygame.draw.circle(screen, "purple", self.position, self.radius, constants.LINE_WIDTH)
        pygame.draw.polygon(screen, self.color, points, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill() #this removes the original asteroid. 

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