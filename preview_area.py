from settings_game import*

class Preview:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface((side_bar_width, game_height * preview_height_fraction))
        self.rect = self.surface.get_rect(topright = (window_width - padding, padding))

    def run (self):
        self.display_surface.blit(self.surface, self.rect)