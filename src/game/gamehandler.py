import pygame, sys
from pygame._sdl2.video import Window, Renderer
import game.var as var

class GameHandler():
    @staticmethod
    def run() -> None:
        pygame.init()
        pygame.font.init()
        var.window = Window("Dodge game", (800, 600))
        var.renderer = Renderer(var.window, vsync = True)
        var.clock = pygame.time.Clock()
        GameHandler.loop()

    @staticmethod
    def loop() -> None:
        while True:
            var.clock.tick(var.FPS)
            GameHandler.handle_input()
            GameHandler.handle_scene()
            GameHandler.render()

    @staticmethod
    def handle_input() -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    @staticmethod
    def handle_scene() -> None:
        pass

    @staticmethod
    def render() -> None:
        var.renderer.draw_color = (0, 0, 0, 255)
        var.renderer.clear()
        var.renderer.present()
