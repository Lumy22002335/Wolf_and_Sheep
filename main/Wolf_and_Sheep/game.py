import pygame, pygame.freetype
from button import Button

class Game:

    def __init__(self):
        self.exit = False

        # Load font
        self.font = pygame.freetype.Font('NotoSans-Regular.ttf', 24)

        # Load images
        self.wolf = pygame.image.load('wolf_small.png')
        self.sheep = pygame.image.load('sheep_small.png')

        self.button = Button('Exit', self.font, pygame.Rect(10, 680, 100, 30), (255, 255, 0), (255, 255, 255), lambda: self.exit_to_menu())

        self.grid_start = (384, 104)

        self.mouse_grid_pos = (0, 0)

        self.grid = [[0, 1, 0, 1, 0, 1, 0, 1]]
        for i in range(0, 6):
            e = []
            for j in range(0, 8):
                e.append(0)
            self.grid.append(e)
        self.grid.append([0, 0, 0, 0, 2, 0, 0, 0])

        # Set the turn to 2 (Sheep's turn)
        self.turn = 2

        # Set phase to 0 (0 = select Sheep or Wolf to move; 1 = select the tile to move to)
        self.phase = 0

        self.end_state = 0

        self.sheep_position = (4, 7)

    def valid_movement(self, source, target, type):
        if source[0] == target[0] or source[1] == target[1]:
            return False

        if target[0] < 0 or target[0] > 7:
            return False
        
        if target[1] < 0 or target[1] > 7:
            return False

        tile_dist = abs(target[0] - source[0]) + abs(target[1] - source[1])
        if tile_dist != 2:
            return False
        
        if self.grid[target[1]][target[0]] != 0:
            return False

        if type == 1:
            if source[1] > target[1]:
                return False
        return True

    def draw_grid(self, game_display):
        draw_y = self.grid_start[1]
        for y in range(0, 8):
            draw_x = self.grid_start[0]
            for x in range(0, 8):
                if self.end_state == 0:
                    mouse_hover = self.mouse_grid_pos[0] == x and self.mouse_grid_pos[1] == y
                    if self.phase == 0:
                        if self.turn == self.grid[y][x]:
                            if mouse_hover:
                                pygame.draw.rect(game_display, (0, 200, 0), (draw_x, draw_y, 64, 64), 0)
                            else:
                                pygame.draw.rect(game_display, (0, 200, 200), (draw_x, draw_y, 64, 64), 0)
                    if self.phase == 1:
                        if self.selected_tile[0] == x and self.selected_tile[1] == y:
                            pygame.draw.rect(game_display, (0, 200, 0), (draw_x, draw_y, 64, 64), 0)
                        if self.valid_movement(self.selected_tile, (x, y), self.turn):
                            if mouse_hover:
                                pygame.draw.rect(game_display, (255, 255, 0), (draw_x, draw_y, 64, 64), 0)
                            else:
                                pygame.draw.rect(game_display, (150, 50, 0), (draw_x, draw_y, 64, 64), 0)

                pygame.draw.rect(game_display, (0, 255, 0), (draw_x, draw_y, 64, 64), 2)

                if (self.grid[y][x] == 1):
                    game_display.blit(self.wolf, (draw_x, draw_y))
                elif (self.grid[y][x] == 2):
                    game_display.blit(self.sheep, (draw_x, draw_y))
                draw_x += 64
            draw_y += 64


    def render(self, game_display):
        game_display.fill((0, 0, 20))
        self.button.render(game_display)
        self.draw_grid(game_display)

        if self.end_state == 1:
            self.font.render_to(game_display, (574, 50), 'WOLF WON!', (0, 255, 255))

        if self.end_state == 2:
            self.font.render_to(game_display, (570, 50), 'SHEEP WON!', (0, 255, 255))

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.mouse_grid_pos = ((x - 384) // 64, (y - 104) // 64)

        # If the Sheep reached the top of the grid, the Sheep won
        if self.sheep_position[1] == 0:
            self.end_state = 2

        # If the Sheep has no movements the Wolf won
        has_valid_movements = False
        for i in range(0, 8):
            for j in range(0, 8):
                if self.valid_movement((self.sheep_position[0], self.sheep_position[1]), (i, j), 2):
                    has_valid_movements = True
        if not has_valid_movements:
            self.end_state = 1
        
    def on_mouse_up(self):
        x, y = pygame.mouse.get_pos()
        if self.button.rect.collidepoint(x, y):
            self.button.on_click()

        if self.end_state != 0:
            return

        if self.mouse_grid_pos[0] < 0 or self.mouse_grid_pos[0] > 7 or self.mouse_grid_pos[1] < 0 or self.mouse_grid_pos[1] > 7:
            return

        # If we're on the selecting phase, check if the player clicked on the Wolf or Sheep tile
        if self.phase == 0:
            tile_clicked = self.grid[self.mouse_grid_pos[1]][self.mouse_grid_pos[0]]
            if self.turn == tile_clicked:
                self.phase = 1
                self.selected_tile = self.mouse_grid_pos
        
        # If we're on the moving phase, check if the player clicked on a valid tile to move
        elif self.phase == 1:
            if self.valid_movement(self.selected_tile, self.mouse_grid_pos, self.turn):
                self.grid[self.mouse_grid_pos[1]][self.mouse_grid_pos[0]] = self.turn
                self.grid[self.selected_tile[1]][self.selected_tile[0]] = 0

                if self.turn == 1:
                    self.turn = 2
                else:
                    self.turn = 1
                    self.sheep_position = (self.mouse_grid_pos[0], self.mouse_grid_pos[1])
                self.phase = 0

    def exit_to_menu(self):
        self.exit = True
