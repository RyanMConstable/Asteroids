# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, time
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from powerups import *
import os

def main_menu(in_main_menu, dt, info):
    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
    print(info)
    print("prev_score" in info)
    print("Entering main loop")
    #Create rect objects for play, quit, and the game title
    font = pygame.font.Font('freesansbold.ttf', 32)
    
    title = font.render(f"ASTEROIDS", True, "black", "grey")
    titleRect = title.get_rect()
    titleRect.center = (SCREEN_WIDTH // 2, 250)
    
    if "prev_score" in info:
        score = font.render(f"Score: {info['prev_score']}", True, "black", "grey")
        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, 350)
    
    #START AND QUIT BUTTONS
    start_img = pygame.image.load("images/start_button.png")
    start_rect = start_img.get_rect()
    start_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40)
    
    start_img_hover = pygame.image.load("images/start_button_hover.png")
    start_rect_hover = start_img.get_rect()
    start_rect_hover.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40)
    
    quit_img = pygame.image.load("images/quit_button.png")
    quit_rect = quit_img.get_rect()
    quit_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)
    
    quit_img_hover = pygame.image.load("images/quit_button_hover.png")
    quit_rect_hover = quit_img_hover.get_rect()
    quit_rect_hover.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)
    #END START AND QUIT BUTTONS
    
    #Main menu loop
    game_loop = True
    while in_main_menu:
        screen.fill("grey")
        #Print buttons to screen
        screen.blit(title, titleRect)
        if "prev_score" in info:
            screen.blit(score, scoreRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        mouse = pygame.mouse.get_pos()
        if mouse[1] < start_rect.bottom and mouse[1] > start_rect.top and mouse[0] < start_rect.right and mouse[0] > start_rect.left:
            screen.blit(start_img_hover, start_rect_hover)
            if pygame.mouse.get_pressed()[0]:
                in_main_menu = False
        else:
            screen.blit(start_img, start_rect)
            
        if mouse[1] < quit_rect.bottom and mouse[1] > quit_rect.top and mouse[0] < quit_rect.right and mouse[0] > quit_rect.left:
            screen.blit(quit_img_hover, quit_rect_hover)
            if pygame.mouse.get_pressed()[0]:
                in_main_menu = False
                game_loop = False
        else:
            screen.blit(quit_img, quit_rect)
            
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
    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
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
    powerups = pygame.sprite.Group()
    
    #Create containers for classes
    player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, bullets)
    Armor.containers = (drawable, powerups)
    
    player1 = player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    af = AsteroidField()
    
    
    #Info Game Section
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f"Score: {player1.score}", True, "white", "black")
    textRect = text.get_rect()
    textRect.top = 0
    textRect.left = 0
     
        
    #Check if in_menu set to true or false
    #GAME LOOP
    clean_board = False
    in_main_menu = True
    gaming = True
    menu_info = {}
    while gaming:
        
        #Main menu loop
        if in_main_menu:
            in_main_menu, gaming = main_menu(in_main_menu, dt, menu_info)
        
        
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
            
        for item in powerups:
            if player1.collision(item):
                if isinstance(item, Armor):
                    player1.armor += 1
                item.kill()
                
        #Check asteroid collision
        for item in asteroids:
            #Player collision with asteroid
            if player1.collision(item):
                if player1.armor == 0:
                    player1.hp -= 1
                    if player1.hp <= 0:
                        menu_info["prev_score"] = player1.score
                        end(player1.score)
                        in_main_menu = True
                        clean_board = True
                else:
                    player1.armor -= 1
                item.kill()
            
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
        
        if clean_board:
            for item in asteroids:
                item.kill()
            for bullet in bullets:
                bullet.kill()
            player1.kill()
            player1 = player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            clean_board = False
            af.kill()
            af = AsteroidField()
            
        dt = clock.tick(FPS) / 1000
        pygame.display.flip()

def end(score):
    print(f"Game over! You had a score of {score}!")

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption('Asteroids!')
    clock = pygame.time.Clock()
    dt = 0
    
    main(dt)
    pygame.display.quit()
    pygame.quit()
    quit()

