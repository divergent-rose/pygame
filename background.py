import pygame
import random
from constants import SCREEN_WIDTH,SCREEN_HEIGHT

class Background:
    def __init__(self, num_stars=150):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.stars = []
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 24)
        
        # Create stars with different speeds for parallax effect
        for _ in range(num_stars):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            speed = random.uniform(0.5, 2)
            size = random.randint(1, 3)
            self.stars.append({'x': x, 'y': y, 'speed': speed, 'size': size})
    
    def update(self):
        """Move stars down the screen"""
        for star in self.stars:
            star['y'] += star['speed']
            star['x'] += star['speed'] * 0.5  # Slight horizontal movement for parallax effect
            # Wrap around when star goes off screen
            if star['y'] > self.height:
                star['y'] = 0
                star['x'] = random.randint(0, self.width)
            # Wrap around when star goes off screen horizontally
            if star['x'] > self.width:
                star['x'] = 0
                star['y'] = random.randint(0, self.height)
    
    def draw(self, screen):
        """Draw the background"""
        screen.fill((0, 0, 10))  # Dark space
        
        for star in self.stars:
            # Brightness based on size
            brightness = 255 if star['size'] > 1 else 200
            color = (brightness, brightness, brightness)
            pygame.draw.circle(screen, color, 
                             (int(star['x']), int(star['y'])), 
                             star['size'])
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
    
    def add_score(self, points):
        self.score += points