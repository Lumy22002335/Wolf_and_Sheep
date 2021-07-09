import pygame
from menu import Menu

def main():
    pygame.init()
    game_display = pygame.display.set_mode((1280, 720))

    current_scene = Menu()


    while True:
        current_scene.render(game_display)

        pygame.display.flip()

main()
