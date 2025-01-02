# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Sets window name
    pygame.display.set_caption('Asteroids!')
    clock = pygame.time.Clock()
    dt = 0
    
    #Create groups that are able to be added to
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    #Create containers for classes
    player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, bullets)
    
    player1 = player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    af = AsteroidField()
    
    
    #Info Game Section
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f"Score: {player1.score}", True, "white", "black")
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    #Menu Text
    playButton = font.render("Play", True, "black", "white")
    playButtonRect = text.get_rect()
    playButtonRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    in_menu = True
    while in_menu:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if SCREEN_WIDTH/2 <= mouse[0] <= SCREEN_WIDTH/2+140 and SCREEN_HEIGHT/2 <= mouse[1] <= SCREEN_HEIGHT/2+40: 
                    in_menu = False

        screen.fill("black")
        
        if SCREEN_WIDTH/2 <= mouse[0] <= SCREEN_WIDTH/2+140 and SCREEN_HEIGHT/2 <= mouse[1] <= SCREEN_HEIGHT/2+40: 
            pygame.draw.rect(screen,"white",[SCREEN_WIDTH/2,SCREEN_HEIGHT/2,140,40])   
        else: 
            pygame.draw.rect(screen,"grey",[SCREEN_WIDTH/2,SCREEN_HEIGHT/2,140,40])
            
        screen.blit(playButton, (SCREEN_WIDTH/2+50, SCREEN_HEIGHT/2))
        
        pygame.display.flip()
                
        
    
    #GAME LOOP
    keep_running = True
    while keep_running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        screen.blit(font.render(f"Score: {player1.score}", True, "white", "black"), textRect)

        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)

        #Check asteroid collision
        for item in asteroids:
            if player1.collision(item):
                print("Game Over!")
                print(f"Score: {player1.score}")
                keep_running = False
                pygame.quit()
                quit()
                
            for bullet in bullets:
                if bullet.collision(item):
                    player1.score += 1
                    bullet.kill()
                    item.split()
                
        
        dt = clock.tick(60)/1000
        pygame.display.flip()
    #END GAME LOOP



if __name__ == "__main__":
    main()

