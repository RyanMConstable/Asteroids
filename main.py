# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, time
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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    #Sets window name
    pygame.display.set_caption('Asteroids!')
    clock = pygame.time.Clock()
    dt, dt_menu = 0, 0
    
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
    textRect.center = (140,20)
    #Play button
    playButton = font.render("Play", True, "black", "white")
    playButtonRect = playButton.get_rect()
    playButtonRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    #Quit button
    quitButton = font.render("Quit", True, "black", "white")
    quitButtonRect = quitButton.get_rect()
    quitButtonRect.center = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2) - 280)
     
        
        
    #Check if in_menu set to true or false
    #GAME LOOP
    gaming = True
    while gaming:
    
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
                print("Game Over! =================================================")
                print(f"Score: {player1.score}")
                gaming = False
                break
                
            for bullet in bullets:
                if bullet.collision(item):
                    player1.score += 1
                    bullet.kill()
                    item.split()
                
        
        dt = clock.tick(60)/1000
        pygame.display.flip()



if __name__ == "__main__":
    main()
    pygame.quit()

