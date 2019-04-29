from utils import Vector, Ray, Spectrum

class BlackHole:
    def __init__(self, position: Vector, mass: float):
        self.position = position
        self.mass = mass

    def hit_by_ray(self, r: Ray) -> bool:
        return False

    def get_luminance(self, out_direction: Vector) -> Spectrum:
        return Spectrum(255, 0, 0)
