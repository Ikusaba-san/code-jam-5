import pyglet

from .constants import CollisionType
from .enemy import Enemy
from .object import Object
from .player import Player
from .space import Space
from .utils import keys


class Game(pyglet.window.Window):
    def __init__(self, *, fps=120, **kwargs):
        super().__init__(caption='Penguin Snowball', **kwargs)
        self.is_over = False
        self.fps = fps

        self.player = Player(self.width / 2, self.height / 2)

        self.space = self.create_space()
        self.space.add(self.player)
        for _ in range(5):
            self.space.add(Enemy())

        # Add handlers
        self.push_handlers(self.player)
        self.push_handlers(keys)

    def create_space(self) -> Space:
        """Returns a space usable for the game"""

        space = Space()

        space.add_collision_handler(CollisionType.PLAYER,
                                    CollisionType.ENEMY,
                                    self.on_collision_player_enemy,
                                    Player.collides_with)

        space.add_collision_handler(CollisionType.ENEMY,
                                    CollisionType.SNOWBALL,
                                    Enemy.on_collision_snowball,
                                    Enemy.collides_with)

        return space

    def on_draw(self):
        self.clear()
        self.space.draw()

    def update(self, dt):
        self.space.update(dt)

    def run(self):
        """Runs the game"""

        pyglet.clock.schedule_interval(self.update, 1/self.fps)
        pyglet.app.run()

    def on_collision_player_enemy(self, player, enemy):
        """When a player collides with an enemy, end the game"""
        if not self.is_over:
            self.is_over = True
            game_over_screen = GameOverScreen(self)
            self.space.add(game_over_screen)


class GameOverScreen(Object):
    def __init__(self, window):
        self.label = pyglet.text.Label("Game Over",
                                       font_name="Times New Roman",
                                       font_size=36,
                                       x=window.width // 2,
                                       y=window.height // 2,
                                       anchor_x='center',
                                       anchor_y='center')

    def add_to_space(self, space):
        super().add_to_space(space)
        self.label.batch = space.batch