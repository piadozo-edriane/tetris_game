import pygame
from settings_game import*
#component
from game import Game
from score_board import Score
from preview_area import Preview


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        #components
        self.game = Game()
        self.score = Score()
        self.preview = Preview()

    def run (self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # Background color
            self.display_surface.fill((135, 115, 114))
            #components
            self.game.run()
            self.score.run()
            self.preview.run()
            # Updating the game
            pygame.display.update()
            self.clock.tick()
    
if __name__ == "__main__":
    main = Main()
    main.run()