import pygame
from settings_game import*

class Game:
    def __init__(self):
        #general 
        self.surface = pygame.Surface((game_width, game_height))
        self.display_surface = pygame.display.get_surface()

    def run (self):
        #blit stand for block image like layering
        self.display_surface.blit(self.surface, (padding, padding))