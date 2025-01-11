from circleshape import *
from constants import *

class Armor(CircleShape):
    def __init__(self, x, y, color = "blue"):
        super().__init__(x, y, 5)
        self.color = color
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)
        
        
        
class FastBullet(CircleShape):
    def __init__(self, x, y, color = "green"):
        super().__init__(x, y, 5)
        self.color = color
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)