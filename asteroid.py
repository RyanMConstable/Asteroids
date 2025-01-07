from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, hp = 1, color = "white"):
        super().__init__(x, y, radius)
        self.hp = hp
        self.color = color
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        if self.position[0] > SCREEN_WIDTH + 200 or self.position[0] < - 200:
            self.kill()
        if self.position[1] > SCREEN_HEIGHT + 200 or self.position[0] < - 200:
            self.kill()
            
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS).velocity = self.velocity.rotate(angle) * 1.2
        Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS).velocity = self.velocity.rotate(-angle) * 1.2
        