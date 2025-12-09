from .shape import Vec2, Rect2

# Bullet object
# Bullet will be handled in FieldHandler object.
class Bullet():
    def __init__(self):
        self.rect: Rect2 = Rect2(0, 0, 40, 40)
        self.velocity: Vec2 = Vec2(0, 0)
