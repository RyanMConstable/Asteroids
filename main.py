# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, time
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main_menu(in_main_menu, dt):
    #Create rect objects for play, quit, and the game title
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f"Exit", True, "black", "white")
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)
    
    play = font.render(f"Play", True, "black", "white")
    playRect = text.get_rect()
    playRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40)
    
    #Main menu loop
    game_loop = True
    while in_main_menu:
        screen.fill("grey")
        #Print buttons to screen
        screen.blit(text, textRect)
        screen.blit(play, playRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Find button pressed
        mouse = pygame.mouse.get_pos()
        if mouse[1] < playRect.bottom and mouse[1] > playRect.top and mouse[0] < playRect.right and mouse[0] > playRect.left and pygame.mouse.get_pressed()[0]:
            in_main_menu = False
        if mouse[1] < textRect.bottom and mouse[1] > textRect.top and mouse[0] < textRect.right and mouse[0] > textRect.left and pygame.mouse.get_pressed()[0]:
            in_main_menu = False
            game_loop = False
            
        #Check keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            in_main_menu = False
        if keys[pygame.K_ESCAPE]:
            in_main_menu = False
            game_loop = False
        
        #Update time and flip the screen
        dt = clock.tick(FPS) / 1000
        pygame.display.flip()
    return in_main_menu, game_loop

def main(dt):
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #pygame.FULLSCREEN
    #Sets window name
    
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
        
        #Main menu loop
        if in_main_menu:
            in_main_menu, gaming = main_menu(in_main_menu, dt)
            
        
        
        #This is the main menu of the game
        screen.fill("black")
            
        #Check the keys to see if the user wants to end the game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            end(player1.score)
            return
        #Check for specific events like exiting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
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
                    item.hp -= 1
                    if item.hp == 0:
                        item.split()
                
        
        dt = clock.tick(FPS) / 1000
        pygame.display.flip()

def end(score):
    print(f"Game over! You had a score of {score}!")

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Asteroids!')
    clock = pygame.time.Clock()
    dt = 0
    
    main(dt)
    pygame.display.quit()
    pygame.quit()
    quit()

