from .shape import Vec2, Rect2

class Bullet():
    def __init__(self):
        self.rect: Rect2 = Rect2(0, 0, 40, 40)
        self.speed: float = 200.0
