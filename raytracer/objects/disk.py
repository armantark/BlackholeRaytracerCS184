from utils import Spectrum, Ray
from math import cos, sin, radians
import numpy as np

BASENORMAL = np.array([0, 1, 1])

class TestDisk:
    def __init__(
        self,
        origin: np.array =  np.array([0.5, 0.5, 0.5]),
        normal: np.array = np.array([0, 1, 0]),
        inner_radius: float = 0,
        outer_radius: float = 0.1
    ):
        self.origin = origin
        self.normal = normal
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.mass = 0


    def _intersects_plane(self, r: Ray, last_position: np.array) -> bool:
        relative_direction = np.dot(r.position - self.origin, self.normal)
        relative_last_direction = np.dot(last_position - self.origin, self.normal)

        if relative_direction == 0:
            return True

        if relative_direction > 0:
            return relative_last_direction < 0

        # relative_direction < 0:
        return relative_last_direction > 0

    def hit_by_ray(self, r: Ray, last_position: np.array) -> bool:
        if self._intersects_plane(r, last_position):
            distance = np.linalg.norm(r.position - self.origin)
            return self.inner_radius <= distance <= self.outer_radius

    def get_luminance(self, out_position: np.array, out_direction: np.array) -> Spectrum:
        inner_spectrum = Spectrum(0, 0, 255)
        outer_spectrum = Spectrum(0, 0, 128)

        distance = np.linalg.norm(out_position - self.origin)
        ratio = (distance - self.inner_radius) / (self.outer_radius - self.inner_radius)

        spectrum = (1 - ratio) * inner_spectrum + ratio * outer_spectrum
        spectrum.r = int(spectrum.r)
        spectrum.g = int(spectrum.g)
        spectrum.b = int(spectrum.b)
        return spectrum

class Disk:
    pass

# class Disk:
#     def __init__(self, position: np.array = np.array([0.5, 0.5, 0.5]),
#                  rotation: np.array = np.array([0, 0, 0]), radius: float = 0.1):
#         self.position = position
#         self.rotation = rotation
#         self.radius = radius
#         self.radius2 = radius ** 2
#         x = radians(rotation[0])
#         y = radians(rotation[1])
#         z = radians(rotation[2])
#         # this is the result of multiplying rotation matrices by x, y, and z axes together

#         Rx = np.array([
#             [1.0, 0.0, 0.0],
#             [0.0, np.cos(rx), -np.sin(rx)],
#             [0.0, np.sin(rx), np.cos(rx)]])

#         Ry = np.array([
#             [np.cos(ry), 0.0, np.sin(ry)],
#             [0.0, 1.0, 0.0],
#             [-np.sin(ry), 0.0, np.cos(ry)]])

#         Rz = np.array([
#             [np.cos(rz), -np.sin(rz), 0.0],
#             [np.sin(rz), np.cos(rz), 0.0],
#             [0.0, 0.0, 1.0]])

#         self.rotation_matrix_for_normal = np.matmul(np.matmul(Rz, Ry), Rx)



#         # self.rotation_matrix_for_normal = np.matrix([[cos(y) * cos(z), cos(z) * sin(x) * sin(y) - cos(x) * sin(z),
#         #                                          cos(x) * cos(z) * sin(y) + sin(x) * sin(z)],
#         #
#         #                                          [cos(y) * sin(z), cos(x) * cos(z) + sin(x) * sin(y) * sin(z),
#         #                                          cos(x) * sin(y) * sin(z) - cos(z) * sin(x)],
#         #
#         #                                          [-sin(y), cos(y) * sin(x), cos(x) * cos(y)]])
#         self.planenormal: np.array = self.rotation_matrix_for_normal * BASENORMAL.reshape(3,1)

#     def intersectPlane(self, n: np.array, p0: np.array, l0: np.array, l: np.array, t: float):
#         denom = np.dot(n.reshape(1,3), l.reshape(3,1))
#         if denom > 1e-6:
#             p0l0 = p0 - l0
#             t = np.dot(p0l0,n) / denom
#             return t >= 0
#         return False

#     def hit_by_ray(self, r: Ray, last_position: np.array) -> bool:
#         t = 0
#         # need to figure out what n is, it is the perpendicular vector to the plane
#         # return self.intersectPlane(n=self.planenormal / np.linalg.norm(self.planenormal), p0=self.position / np.linalg.norm(self.position),
#         #                            l0=r.position / np.linalg.norm(r.position), l=r.velocity / np.linalg.norm(r.velocity), t=t)
#         if self.intersectPlane(n=self.planenormal / np.linalg.norm(self.planenormal), p0=self.position / np.linalg.norm(self.position),
#                                l0=r.position / np.linalg.norm(r.position), l=r.velocity / np.linalg.norm(r.velocity), t=t):
#             p: np.array = r.position + r.velocity * t
#             v: np.array = p - self.position
#             d2 = np.dot(v, v)
#             return d2 <= self.radius2
#         return False

#     def get_luminance(self, out_position: np.array, out_direction: np.array) -> Spectrum:
#         return Spectrum(0, 0, 255)
