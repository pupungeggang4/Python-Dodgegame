from .bullet import Bullet
from .player import Player

# Structure of field
# Field will be handled in FieldHandler class
class Field():
    def __init__(self):
        self.player: Player = Player()
        self.bullet_list: list[Bullet] = []
        self.bullet_spawn_time: float = 1.5
        self.bullet_spawn_interval: float = 1.5
