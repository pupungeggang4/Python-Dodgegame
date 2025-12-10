from pygame._sdl2.video import Window, Renderer
from pygame.time import Clock
from pygame.font import Font
from .shape import Vec2, Rect2
from .field import Field

class GameVar():
    # Font
    font: Font = None

    # Game components
    window: Window = None
    renderer: Renderer = None
    clock: Clock = None
    fps: float = 60

    # Game states
    key_pressed: dict[str, bool] = {'left': False, 'right': False, 'up': False, 'down': False}
    field: Field = None
    game_over: bool = False
    elapsed_time: float = 0
    score: int = 0
