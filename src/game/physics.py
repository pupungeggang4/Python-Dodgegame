import math
from .shape import Vec2, Rect2

class Physics():
    @staticmethod
    def distance(v1: Vec2, v2: Vec2):
        return math.sqrt((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)

    @staticmethod
    def vec_inside_rect(v: Vec2, r: Rect2) -> bool:
        return v.x > r.pos.x - r.size.x / 2 and v.x < r.pos.x + r.size.x / 2 and v.y > r.pos.y - r.size.y / 2 and v.y < r.pos.y + r.size.y / 2

    @staticmethod
    def simple_collision_check(r1: Rect2, r2: Rect2):
        r1_radius: float = (r1.size.x + r1.size.y) / 4
        r2_radius: float = (r2.size.x + r2.size.y) / 4
        distance: float = Physics.distance(r1.pos, r2.pos)
        return distance < r1_radius + r2_radius
