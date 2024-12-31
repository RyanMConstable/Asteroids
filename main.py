# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    player1 = player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    updatable.add(player1)
    drawable.add(player1)
    
    keep_running = True
    while keep_running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        #player1.draw(screen)
        #player1.update(dt)
        
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        
        dt = clock.tick(60)/1000
        pygame.display.flip()
        

if __name__ == "__main__":
    main()

