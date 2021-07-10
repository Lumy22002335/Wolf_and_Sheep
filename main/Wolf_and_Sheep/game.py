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

        self.grid = [[0, 1, 0, 1, 0, 1, 0, 1]]
        for i in range(0, 6):
            e = []
            for j in range(0, 8):
                e.append(0)
            self.grid.append(e)
        self.grid.append([0, 0, 0, 0, 2, 0, 0, 0])

    def draw_grid(self, game_display):
        draw_y = self.grid_start[1]
        for y in range(0, 8):
            draw_x = self.grid_start[0]
            for x in range(0, 8):
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

    def on_mouse_up(self):
        x, y = pygame.mouse.get_pos()
        if self.button.rect.collidepoint(x, y):
            self.button.on_click()

    def exit_to_menu(self):
        self.exit = True
