import pygame

#Returns true if you want to stay in menu
def main_menu(screen):
    stay_in_menu = True
    while stay_in_menu:
        screen.fill("grey")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return True
        pygame.display.flip()
    return False