from random import randint

from .field import Field
from .player import Player
from .bullet import Bullet
from .shape import Rect2

from .physics import Physics

import game.var as var

# A class which handles game logic
class FieldHandler():
    # Handling field by ticks.
    @staticmethod
    def handle_tick_field(field: Field) -> None:
        if field.bullet_spawn_time < 0:
            FieldHandler.spawn_bullet(field)
            field.bullet_spawn_time = field.bullet_spawn_interval
        else:
            field.bullet_spawn_time -= 1 / var.fps

        FieldHandler.handle_bullet(field)

    # Handling spawning bullets.
    # The bullets are spwaned outside of field.
    # The bullets will cross the field.
    @staticmethod
    def spawn_bullet(field: Field) -> None:
        spawn_index: int = randint(0, 3)
        bullet: Bullet = Bullet()
        if spawn_index == 0 or spawn_index == 2:
            bullet.rect.pos.x = float(randint(20, 780))
            bullet.velocity.x = 0
            if spawn_index == 0:
                bullet.rect.pos.y = -20
                bullet.velocity.y = float(randint(150, 250))
            else:
                bullet.rect.pos.y = 620
                bullet.velocity.y = float(-randint(150, 250))
        else:
            bullet.rect.pos.y = float(randint(20, 580))
            bullet.velocity.y = 0
            if spawn_index == 1:
                bullet.rect.pos.x = -20
                bullet.velocity.x = float(randint(150, 250))
            else:
                bullet.rect.pos.x = 820
                bullet.velocity.x = float(-randint(150, 250))
        field.bullet_list.append(bullet)

    # Handling bullet.
    # Cheching whether bullet is outside of field, making bullets move, checking collision between player.
    @staticmethod
    def handle_bullet(field: Field) -> None:
        for i in range(len(field.bullet_list) - 1, -1, -1):
            bullet: Bullet = field.bullet_list[i]
            if bullet.rect.pos.x > 880 or bullet.rect.pos.x < -80 or bullet.rect.pos.y > 680 or bullet.rect.pos.y < -80:
                field.bullet_list.pop(i)
            else:
                bullet.rect.pos.x += bullet.velocity.x / var.fps
                bullet.rect.pos.y += bullet.velocity.y / var.fps
                if Physics.simple_collision_check(bullet.rect, field.player.rect):
                    var.game_over = True

    # Field rendering function
    @staticmethod
    def render(field: Field) -> None:
        var.renderer.draw_color = (0, 255, 255, 255)
        var.renderer.fill_rect([field.player.rect.pos.x - field.player.rect.size.x / 2, field.player.rect.pos.y - field.player.rect.size.y / 2, field.player.rect.size.x, field.player.rect.size.y])
        var.renderer.draw_color = (255, 255, 255, 255)
        for i in range(len(field.bullet_list)):
            rect: Rect2 = field.bullet_list[i].rect
            var.renderer.fill_rect([rect.pos.x - rect.size.x / 2, rect.pos.y - rect.size.y / 2, rect.size.x, rect.size.y])

    # Moving player
    @staticmethod
    def move_player(field: Field) -> None:
        player: Player = field.player
        if var.key_pressed['left']:
            player.rect.pos.x -= player.speed / var.fps
        if var.key_pressed['right']:
            player.rect.pos.x += player.speed / var.fps
        if var.key_pressed['up']:
            player.rect.pos.y -= player.speed / var.fps
        if var.key_pressed['down']:
            player.rect.pos.y += player.speed / var.fps

    # Restarting game
    @staticmethod
    def reset_state(field: Field) -> None:
        field.bullet_list = []
        field.player.rect.pos.x = 400
        field.player.rect.pos.y = 300


