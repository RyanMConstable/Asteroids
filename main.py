# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, time
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from menu import main_menu

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
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
    textRect.center = (80,20)
     
        
    #Check if in_menu set to true or false
    #GAME LOOP
    in_main_menu = True
    gaming = True
    while gaming:
        #This is the main menu of the game
        while in_main_menu:
            in_main_menu = main_menu()
        #Check the keys to see if the user wants to end the game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            end(player1.score)
            return
        #Check for specific events like exiting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        screen.blit(font.render(f"Score: {player1.score}", True, "white", "black"), textRect)

        #Update and draw all items in the updatable and drawable groups
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)

        #Check asteroid collision
        for item in asteroids:
            #Player collision with asteroid
            if player1.collision(item):
                end(player1.score)
                return
            
            #Check for every bullet to see if any hit an asteroid
            for bullet in bullets:
                if bullet.collision(item):
                    player1.score += 1
                    af.score += 1
                    af.boss_timer += 1
                    bullet.kill()
                    item.split()
                
        
        dt = clock.tick(60)/1000
        pygame.display.flip()

def end(score):
    print(f"Game over! You had a score of {score}!")

if __name__ == "__main__":
    main()
    pygame.display.quit()
    pygame.quit()
    quit()

