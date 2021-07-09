import pygame
from menu import Menu

def main():
    pygame.init()
    game_display = pygame.display.set_mode((1280, 720))

    current_scene = Menu()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                current_scene.on_mouse_up()

        current_scene.render(game_display)

        pygame.display.flip()

main()
