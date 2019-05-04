from vector import *
from dataclasses import dataclass

@dataclass
class Ray:
    depth: int = 0

    position: Vector = Vector(0, 0 ,0)
    velocity = Vector(0, 0 ,0)
    delta_t = 0.0001

    def simulate(self, gravity_objects = []):
        total_force = 0
        for object in gravity_objects:
            pass
        accleration = 0  # implement later
        new_position = self.position + self.velocity * self.delta_t

        for object in gravity_objects:
            if object.


        self.velocity = (new_position - self.position) / self.delta_t;
        self.position = new_position


    # min_t: float = 0
    # max_t: float = float('inf')

    # inv_d: Vector = Vector(0,0,0)

    # def at_time(self, t) -> Vector:
    #     return self.o + t * self.d

    #may not be necessary but I'm putting this in here for the sake of completion later if necessary
    def transform_by(self, t):
        raise NotImplementedError()


