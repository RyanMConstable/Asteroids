from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        if self.position[0] > SCREEN_WIDTH or self.position[0] < 0:
            self.kill()
        if self.position[1] > SCREEN_HEIGHT or self.position[1] < 0:
            self.kill()