import pygame

class Button:
    def __init__(self, text, font, rect, normal_color, highlight_color, on_click):
        self.text = text
        self.font = font
        self.rect = rect
        self.normal_color = normal_color
        self.highlight_color = highlight_color
        self.on_click = on_click
        self.current_color = normal_color


    def render(self, game_display):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.current_color = self.highlight_color
        else:
            self.current_color = self.normal_color
        pygame.draw.rect(game_display, self.current_color, self.rect, 2)
        text = self.font.get_rect(self.text)
        text_position = (self.rect.center[0] - text.width * 0.5, self.rect.center[1] - text.height * 0.5)
        self.font.render_to(game_display, text_position, self.text, self.current_color)
