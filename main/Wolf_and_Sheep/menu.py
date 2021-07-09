import pygame, pygame.freetype

class Menu:
    def __init__(self):
    
        # Load font
        self.font = pygame.freetype.Font('NotoSans-Regular.ttf', 30)
        self.font_large = pygame.freetype.Font('NotoSans-Regular.ttf', 80)

        # Load images
        self.wolf = pygame.image.load('wolf.png')
        self.sheep = pygame.image.load('sheep.png')

    def render(self, game_display):
        game_display.fill((0, 0, 20))