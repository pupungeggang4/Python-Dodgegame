import pygame, sys

from pygame._sdl2.video import Window, Renderer, Texture
from pygame import Surface, Rect
from pygame.font import Font

from .gamevar import GameVar

from .field import Field
from .fieldhandler import FieldHandler

# A class which controlls window, renderer and overall game flow.
class GameHandler():
    # Initalize game and calling loop.
    def run(self, var: GameVar) -> None:
        pygame.init()
        pygame.font.init()
        var.font = Font("font/neodgm.ttf", 32)
        var.window = Window("Dodge game", (800, 600))
        var.renderer = Renderer(var.window, vsync = True)
        var.clock = pygame.time.Clock()
        var.field = Field()
        self.loop(var)

    # Loop
    def loop(self, var: GameVar) -> None:
        while True:
            var.clock.tick(var.fps)
            self.handle_input(var)
            self.handle_scene(var)
            self.render(var)

    # Handling input
    def handle_input(self, var: GameVar) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key: int = event.key
                if key == pygame.K_LEFT:
                    var.key_pressed['left'] = True
                if key == pygame.K_RIGHT:
                    var.key_pressed['right'] = True
                if key == pygame.K_UP:
                    var.key_pressed['up'] = True
                if key == pygame.K_DOWN:
                    var.key_pressed['down'] = True

                if var.game_over == True:
                    if key == pygame.K_RETURN:
                        var.game_over = False
                        FieldHandler.reset_state(var.field, var)
                        var.elapsed_time = 0
                        var.score = 0

            if event.type == pygame.KEYUP:
                key: int = event.key
                if key == pygame.K_LEFT:
                    var.key_pressed['left'] = False
                if key == pygame.K_RIGHT:
                    var.key_pressed['right'] = False
                if key == pygame.K_UP:
                    var.key_pressed['up'] = False
                if key == pygame.K_DOWN:
                    var.key_pressed['down'] = False
    
    # Handling scene
    def handle_scene(self, var: GameVar) -> None:
        if var.game_over == False:
            FieldHandler.handle_tick_field(var.field, var)
            FieldHandler.move_player(var.field, var)
            var.elapsed_time += 1 / var.fps
            var.score = int(var.elapsed_time)

    # Rendering
    def render(self, var: GameVar) -> None:
        var.renderer.draw_color = (0, 0, 0, 255)
        var.renderer.clear()
        FieldHandler.render(var.field, var)
        text_surface: Surface = None
        if var.game_over == False:
            text_surface: Surface = var.font.render(f'Score: {var.score}', False, (255, 255, 0, 255))
        else:
            text_surface: Surface = var.font.render(f'Game Over! Press Enter to Restart.', False, (255, 255, 0, 255))
        text_texture: Texture = Texture.from_surface(var.renderer, text_surface)
        rect: Rect = text_texture.get_rect()
        text_texture.draw(None, (20, 20, rect.width, rect.height))
        var.renderer.present()
