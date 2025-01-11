import pygame
import random
from asteroid import Asteroid
from constants import *
from powerups import Armor


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.score = 0
        self.boss_timer = 0

    def spawn(self, radius, position, velocity, color = "white", hp = 1):
        asteroid = Asteroid(position.x, position.y, radius, hp = hp, color = color)
        asteroid.velocity = velocity
    
    def spawnarmor(self, x, y):
        armor = Armor(x, y)
        armor.velocity = 0

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, self.score + 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            if self.boss_timer >= 50:
                self.boss_timer -= 50
                self.spawnarmor(random.randint(0, pygame.display.get_surface().get_size()[0]), random.randint(0, pygame.display.get_surface().get_size()[1]))
                self.spawn(ASTEROID_BOSS_RADIUS, position, velocity, hp=5, color="red")
            else:
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)