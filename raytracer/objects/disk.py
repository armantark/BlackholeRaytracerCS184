from utils import Vector, Spectrum, Ray, Matrix
from math import cos, sin, radians


class Disk:

    def __init__(self, position: Vector = Vector(0.5, 0.5, 0.5),
                 rotation: Vector = Vector(radians(90), 0, 0), radius: float = 0.25):
        self.position = position
        self.rotation = rotation
        self.radius = radius
        self.radius2 = radius ** 2
        x = radians(rotation.x)
        y = radians(rotation.y)
        z = radians(rotation.z)
        # this is the result of multiplying rotation matrices by x, y, and z axes together
        self.rotation_matrix_for_normal = Matrix(cos(y) * cos(z), cos(z) * sin(x) * sin(y) - cos(x) * sin(z),
                                                 cos(x) * cos(z) * sin(y) + sin(x) * sin(z),

                                                 cos(y) * sin(z), cos(x) * cos(z) + sin(x) * sin(y) * sin(z),
                                                 cos(x) * sin(y) * sin(z) - cos(z) * sin(x),

                                                 -sin(y), cos(y) * sin(x), cos(x) * cos(y))
        self.planenormal: Vector = self.rotation_matrix_for_normal * Vector(0, 1, 0)

    def intersectPlane(self, n: Vector, p0: Vector, l0: Vector, l: Vector, t: float):
        denom = n.dot(l)
        if denom > 1e-6:
            p0l0 = p0 - l0
            t = p0l0.dot(n) / denom
            return t >= 0
        return False

    def hit_by_ray(self, r: Ray, last_position: Vector) -> bool:
        t = 0
        # need to figure out what n is, it is the perpendicular vector to the plane
        if self.intersectPlane(n=self.planenormal.unit(), p0=self.position.unit(),
                               l0=r.position.unit(), l=r.velocity.unit(), t=t):
            p: Vector = r.position + r.velocity * t
            v: Vector = p - self.position
            d2 = v.dot(v)
            return d2 <= self.radius2
        return False

    def get_luminance(self, out_position: Vector, out_direction: Vector) -> Spectrum:
        return Spectrum(0, 0, 255)
