from .shape import Vec2, Rect2

class Player():
    def __init__(self):
        self.rect: Rect2 = Rect2(400, 300, 80, 80)
        self.speed: float = 320.0
