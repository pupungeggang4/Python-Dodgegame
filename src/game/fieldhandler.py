from .field import Field
from .player import Player
from .bullet import Bullet
import game.var as var

class FieldHandler():
    @staticmethod
    def handle_tick_field(field: Field):
        if field.bullet_spawn_time < 0:
            FieldHandler.spawn_bullet(field)
            field.bullet_spawn_time = field.bullet_spawn_interval
        else:
            field.bullet_spawn_time -= 1 / var.FPS
