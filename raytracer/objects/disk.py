from utils import Spectrum, Ray
from math import cos, sin, radians
import numpy as np

BASENORMAL = np.array([0,1,0])

class Disk:

    def __init__(self, position: np.array = np.array([0.5, 0.5, 0.5]),
                 rotation: np.array = np.array([180, 0, 0]), radius: float = 0.1):
        self.position = position
        self.rotation = rotation
        self.radius = radius
        self.radius2 = radius ** 2
        x = radians(rotation[0])
        y = radians(rotation[1])
        z = radians(rotation[2])
        # this is the result of multiplying rotation matrices by x, y, and z axes together
        self.rotation_matrix_for_normal = np.matrix([[cos(y) * cos(z), cos(z) * sin(x) * sin(y) - cos(x) * sin(z),
                                                 cos(x) * cos(z) * sin(y) + sin(x) * sin(z)],

                                                 [cos(y) * sin(z), cos(x) * cos(z) + sin(x) * sin(y) * sin(z),
                                                 cos(x) * sin(y) * sin(z) - cos(z) * sin(x)],

                                                 [-sin(y), cos(y) * sin(x), cos(x) * cos(y)]])
        self.planenormal: np.array = self.rotation_matrix_for_normal * BASENORMAL.reshape(3,1)

    def intersectPlane(self, n: np.array, p0: np.array, l0: np.array, l: np.array, t: float):
        denom = np.dot(n.reshape(1,3), l.reshape(3,1))
        if denom > 1e-6:
            p0l0 = p0 - l0
            t = np.dot(p0l0,n) / denom
            return t >= 0
        return False

    def hit_by_ray(self, r: Ray, last_position: np.array) -> bool:
        t = 0
        # need to figure out what n is, it is the perpendicular vector to the plane
        if self.intersectPlane(n=self.planenormal / np.linalg.norm(self.planenormal), p0=self.position / np.linalg.norm(self.position),
                               l0=r.position / np.linalg.norm(r.position), l=r.velocity / np.linalg.norm(r.velocity), t=t):
            p: np.array = r.position + r.velocity * t
            v: np.array = p - self.position
            d2 = np.dot(v, v)
            return d2 <= self.radius2
        return False

    def get_luminance(self, out_position: np.array, out_direction: np.array) -> Spectrum:
        return Spectrum(0, 0, 255)
