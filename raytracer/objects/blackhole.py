from utils import Vector, Ray, Spectrum

G = 6.674e-11
C = 2.9979e8

class BlackHole:
    def __init__(self, position: Vector = Vector(0.5, 0.5, 0.5), mass: float = 3e+25):
        # 3e+25 kg -> schwarzschield radius approx. 5cm
        self.position = position
        self.mass = mass
        self.radius = 2 * G * mass / (C ** 2)

    def hit_by_ray(self, r: Ray, last_position: Vector) -> bool:
        pass
        # if (r.position - self.position).

    def get_luminance(self, out_direction: Vector) -> Spectrum:
        return Spectrum(255, 0, 0)
