from pygame._sdl2.video import Window, Renderer
from pygame import Clock
from .shape import Vec2, Rect2
from .field import Field

window: Window = None
renderer: Renderer = None
clock: Clock = None
fps: float = 60
key_pressed: dict[str, bool] = {'left': false, 'right': false, 'up': false, 'down': false}
field: Field = None

