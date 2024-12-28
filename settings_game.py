import pygame
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
#Game behavior
update_start_speed = 20
move_wait_time = 200
rotate_wait_time = 200 
block_offset = pygame.Vector2(columns // 2, - 1)
#colors
white_color = (255, 255, 255)

#Shapes

tetrominos = {
    "T": {"shape": [(0, 0), (-1, 0), (1, 0), (0,-1)], "color":(3, 115, 252)},
    "O": {"shape": [(0, 0), (0, -1), (1, 0), (1,-1)], "color":(57, 252, 3)},
    "J": {"shape": [(0, 0), (0, -1), (0, 1), (-1,1)], "color":(93, 77, 135)},
    "L": {"shape": [(0, 0), (0, -1), (0, 1), (1, 1)], "color": (122, 59, 16)},
    "I": {"shape": [(0, 0), (0, 1), (0, -2), (0, 1)], "color": (128, 104, 20)},
    "S": {"shape": [(0, 0), (-1, 0), (0, -1), (1,-1)], "color": (13, 94, 59)},
    "Z": {"shape": [(0, 0), (1, 0), (0, -1), (-1,-1)], "color": (173, 52, 111)}
}