import math

class Vec2():
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __repr__(self):
        return f'Vec2({self.x}, {self.y})'

    def __add__(self, v: 'Vec2'):
        return Vec2(self.x + v.x, self.y + v.y)

    def __sub__(self, v: 'Vec2'):
        return Vec2(self.x - v.x, self.y - v.y)

    def __mul__(self, s: float):
        return Vec2(self.x * s, self.y * s)

    def __rmul__(self, s: float):
        return Vec2(self.x * s, self.y * s)

    def __truediv__(self, s: float):
        if s == 0:
            raise ZeroDivisionError('Division by zero!')
        return Vec2(self.x / s, self.y / s)

    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self) -> 'Vec2':
        l: float = self.length()
        return self / l

class Rect2():
    def __init__(self, x: float, y: float, w: float, h: float):
        self.pos: Vec2 = Vec2(x, y)
        self.size:Vec2 = Vec2(w, h)

    def __repr__(self):
        return f'Rect2({self.pos.x}, {self.pos.y}, {self.size.x}, {self.size.y})'
