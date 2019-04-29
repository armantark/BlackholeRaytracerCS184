from vector import *
from dataclasses import dataclass

@dataclass
class Ray:
    depth: int = 0

    o: Vector = Vector(0, 0 ,0)
    d: Vector = Vector(0, 0, 0)
    min_t: float = 0
    max_t: float = float('inf')

    inv_d: Vector = Vector(0,0,0)

    def at_time(self, t) -> Vector:
        return self.o + t * self.d

    #may not be necessary but I'm putting this in here for the sake of completion later if necessary
    def transform_by(self, t):
        raise NotImplementedError()


