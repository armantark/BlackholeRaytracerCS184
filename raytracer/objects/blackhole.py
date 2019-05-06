from utils import Ray, Spectrum
import numpy as np

G = 6.674e-11
C = 2.9979e8

class BlackHole:
    def __init__(self, position: np.array = np.array([0.5, 0.5, 0.5]), mass: float = 1e+25):
        # 3e+25 kg -> schwarzschield radius approx. 5cm
        self.position = position
        self.mass = mass
        self.radius = 2 * G * mass / (C ** 2)

    def hit_by_ray(self, r: Ray, last_position: np.array) -> bool:
        if np.linalg.norm(r.position - self.position) <= (2.5 * self.radius):  # photon sphere
            return True

        return False

    def get_luminance(self, out_position: np.array, out_direction: np.array) -> Spectrum:
        return Spectrum(255, 0, 0)
