import pygame, pygame.freetype
from button import Button

class Menu:
    def __init__(self):
        
        self.play = False
        self.exit = False

        # Load font
        self.font = pygame.freetype.Font('NotoSans-Regular.ttf', 20)
        self.font_large = pygame.freetype.Font('NotoSans-Regular.ttf', 80)

        # Load images
        self.wolf = pygame.image.load('wolf.png')
        self.sheep = pygame.image.load('sheep.png')

        # Initialize buttons
        self.buttons = []
        self.buttons.append(Button('Play', self.font, pygame.Rect(570, 400, 140, 30), (255, 255, 0), (255, 255, 255), lambda: self.start_game()))
        self.buttons.append(Button('Exit', self.font, pygame.Rect(570, 440, 140, 30), (255, 255, 0), (255, 255, 255), lambda: self.exit_game()))

    def render(self, game_display):
        game_display.fill((0, 0, 20))
        game_display.blit(self.wolf, (0, 100))
        game_display.blit(self.sheep, (1024, 100))
        width = self.font_large.get_rect('WOLF & SHEEP').width
        self.font_large.render_to(game_display, (640 - width // 2, 200), 'WOLF & SHEEP', (255, 255, 0))
        for b in self.buttons:
            b.render(game_display)
         
    def on_mouse_up(self):
        x, y = pygame.mouse.get_pos()
        for b in self.buttons:
            if b.rect.collidepoint(x, y):
                b.on_click()

    def start_game(self):
        self.play = True

    def exit_game(self):
        self.exit = True
