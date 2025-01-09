import pygame

#Returns true if you want to stay in menu
def main_menu(screen):
    stay_in_menu = True
    while stay_in_menu:
        #Draw the screen grey
        screen.fill("grey")
        
        #Get list of keys, if the key is escape return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return True
        
        #Flip the screen
        pygame.display.flip()
    return False