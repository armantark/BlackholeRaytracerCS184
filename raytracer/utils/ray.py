from utils import *
from dataclasses import dataclass
import numpy as np

@dataclass
class Ray:
    depth: int = 0

    position: np.array = np.array([0,0,0])
    velocity: np.array = np.array([1,0,0])
    delta_t = 0.01

    def simulate_to_end(self, gravity_objects = []):

        while np.linalg.norm(self.position - np.array([0.5, 0.5, 0.5])) < 1:  # replace with better code for detecting exiting the worldbox
            # print(self.position.x, self.position.y, self.position.z)
            total_force = 0

            for object in gravity_objects:
                pass

            accleration = 0  # implement later
            new_position = self.position + self.velocity * self.delta_t

            last_position = self.position

            self.velocity = (new_position - self.position) / self.delta_t
            self.position = new_position

            for object in gravity_objects:
                if object.hit_by_ray(self, last_position):
                    hit_position = self.position  # not accurate: e.g. move to surface of sphere
                    hit_direction = self.velocity / np.linalg.norm(self.velocity)

                    luminance = object.get_luminance(hit_position, hit_direction)  # maybe divide by distance travelled or sth?
                    return luminance

            # if (self.position - Vector(0.5, 0.5, 0.5)).norm() > 1: # replace with better code for detecting exiting the worldbox
            #     return Spectrum()  # texture mapping?

        return Spectrum()



    # min_t: float = 0
    # max_t: float = float('inf')

    # inv_d: Vector = Vector(0,0,0)

    # def at_time(self, t) -> Vector:
    #     return self.o + t * self.d

    #may not be necessary but I'm putting this in here for the sake of completion later if necessary
    def transform_by(self, t):
        raise NotImplementedError()
