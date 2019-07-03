# Contains classes for collision functionality
from .utils import circles_collide


class ColliderMixin:
    collision_leniency = 0.85

    def collides_with(self, other):
        """
        Called to determine if this collider collides with another
        """
        return circles_collide(self.x,
                               self.y,
                               self.width * self.collision_leniency,
                               other.x,
                               other.y,
                               other.width * self.collision_leniency)

    def on_collision(self, other):
        """
        A callback intended to be overriden, called when two colliders collide
        """
        pass  # Defaults to doing nothing
