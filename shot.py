from circleshape import CircleShape
import constants
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.velocity = pygame.Vector2(direction) * constants.PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt