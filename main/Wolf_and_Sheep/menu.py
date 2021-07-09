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
        game_display.blit(self.wolf, (0, 100))
        game_display.blit(self.sheep, (1024, 100))
        width = self.font_large.get_rect('WOLF & SHEEP').width
        self.font_large.render_to(game_display, (640 - width // 2, 200), 'WOLF & SHEEP', (255, 255, 0))
