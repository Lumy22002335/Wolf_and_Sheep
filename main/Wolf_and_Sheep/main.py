import pygame
from menu import Menu
from game import Game

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
        current_scene.update()

        if isinstance(current_scene, Menu):
            if current_scene.play:
                current_scene = Game()

        if current_scene.exit:
            if isinstance(current_scene, Menu):
                exit()
            else:
                current_scene = Menu()

        pygame.display.flip()

main()
