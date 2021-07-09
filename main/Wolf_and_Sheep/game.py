import pygame, pygame.freetype

class Game:

    def __init__(self):
        self.exit = False

        # Load font
        self.font = pygame.freetype.Font('NotoSans-Regular.ttf', 20)

        # Load images
        self.wolf = pygame.image.load('wolf_small.png')
        self.sheep = pygame.image.load('sheep_small.png')

    def render(self, game_display):
        game_display.fill((255, 255, 255))
