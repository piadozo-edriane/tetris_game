import pygame
#components


class Main:
    # game size
    columns = 10
    rows = 20
    cell_size = 40
    game_width, game_height = columns * cell_size, rows * cell_size
    # side bar size
    side_bar_width = 200
    preview_height_fraction = 0.7
    score_height_fraction = 1 - preview_height_fraction
    # window
    padding = 20
    window_width = game_width + side_bar_width + padding * 3
    window_height = game_height + padding * 2

    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((Main.window_width, Main.window_height))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        #components
        #self.game = component_game.Game.run()

    def run (self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # Background color
            self.display_surface.fill((135, 115, 114))
            self.game.run()
            # Updating the game
            pygame.display.update()
            self.clock.tick()
    
if __name__ == "__main__":
    main = Main()
    main.run()