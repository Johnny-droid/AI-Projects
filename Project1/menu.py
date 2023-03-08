# Class Menu using pygame

import pygame

class Menu:
    
    def draw(self, screen):
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()
        
        # Display the letters menu
        font = pygame.font.SysFont("comicsansms", 100)
        text = font.render("Menu", True, (255, 255, 255))
        screen.blit(text, (screen_width / 2 - 90, screen_height / 2 - 100))

