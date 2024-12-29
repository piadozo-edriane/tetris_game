
from random import choice
from settings_game import*
from timers import Timer

class Game:
    def __init__(self):
        #general 
        self.surface = pygame.Surface((game_width, game_height))
        self.display_surface = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()

        #line for copy
        self.line_surface = self.surface.copy()
        self.line_surface.fill ((0,255,0))
        self.line_surface.set_colorkey((0,255,0))
        self.line_surface.set_alpha(120)
        #tetromino
        #import a choice into a random module and create the dictionary tetrominos into list and iterate the keys
        self.tetromino = Tetromino(choice(list(tetrominos.keys())), self.sprites)

        #timer
        self.timers = {
            "vertical move": Timer(update_start_speed, True, self.move_down)
        }
        self.timers ["vertical move"].activate()

    def timer_update (self):
        for timer in self.timers.values():
            timer.update()

    def move_down (self):
        self.tetromino.move_down()

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
        #update 
        self.timer_update()
        self.sprites.update()
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
        self.pos = pygame.Vector2(pos) + block_offset
        x = self.pos.x * cell_size
        y = self.pos.y * cell_size
        self.rect = self.image.get_rect(topleft = (x, y))
    def update (self):
        self.rect = self.image.get_rect(topleft = self.pos * cell_size)
    
    def update (self):
        self.rect = self.image.get_rect(topleft = self.pos * cell_size)

class Tetromino:
    def __init__(self, shape, group):
        self.block_positions = tetrominos[shape]["shape"]
        self.color = tetrominos[shape]["color"]

        self.blocks = [Block(group, pos, self.color) for pos in self.block_positions]
    def move_down(self):
        for block in self.blocks:
            block.pos.y += 1