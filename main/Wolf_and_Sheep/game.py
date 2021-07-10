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


    def render(self, game_display):
        game_display.fill((0, 0, 20))
        self.button.render(game_display)

    def on_mouse_up(self):
        x, y = pygame.mouse.get_pos()
        if self.button.rect.collidepoint(x, y):
            self.button.on_click()

    def exit_to_menu(self):
        self.exit = True
