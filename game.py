import pygame
from settings_game import*

class Game:
    def __init__(self):
        #general 
        self.surface = pygame.Surface((game_width, game_height))
        self.display_surface = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()

        #line for copy
        self.line_surface = self.surface.copy()

        #tetromino
        self.tetromino = Tetromino("T", self.sprites)
    def draw_grid (self):
        #grid line for height
        for col in range (1, columns):
            x = col * cell_size 
            pygame.draw.line (self.surface, white_color, (x,0), (x, self.surface.get_height()), 1)
        #grid line for width
        for row in range (1, rows):
            y = row * cell_size
            pygame.draw.line (self.surface, white_color, (0,y), (self.surface.get_width(), y))
        self.line_surface.blit(self.line_surface, (0, 0))

    def run (self):
        #blit stand for block image like layering
        self.draw_grid()
        self.sprites.draw(self.surface)
        self.display_surface.blit(self.surface, (padding, padding))

class Block (pygame.sprite.Sprite): # sprite function means 
    def __init__(self, group, pos, color):
        super().__init__(group) 
        self.image = pygame.Surface((cell_size, cell_size))
        self.image.fill (color)
  
        #position
        self.pos = pygame.Vector2(pos) + pygame.Vector2(3, 5)
        x = self.pos.x * cell_size
        y = self.pos.y * cell_size
        self.rect = self.image.get_rect(topleft = (x, y))

class Tetromino:
    def __init__(self, shape, group):
        self.block_positions = tetrominos[shape]["shape"]
        self.color = tetrominos[shape]["color"]

        self.blocks = [Block(group, pos, self.color) for pos in self.block_positions]