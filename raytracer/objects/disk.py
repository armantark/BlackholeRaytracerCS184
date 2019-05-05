from utils import Vector, Spectrum, Ray


class Disk:
    def __init__(self, position: Vector = Vector(0.5, 0.5, 0.5),
                 rotation: Vector = Vector(0, 0, 0), radius: float = 0.75):
        self.position = position
        self.rotation = rotation
        self.radius = radius
        self.radius2 = radius ** 2
        self.planenormal: Vector = '???'

    def intersectPlane(self, n: Vector, p0: Vector, l0: Vector, l: Vector, t: float):
        denom = n.dot(l)
        if denom > 1e-6:
            p0l0 = p0 - l0
            t = p0l0.dot(n) / denom
            return t >= 0
        return False

    def hit_by_ray(self, r: Ray, last_position: Vector) -> bool:
        t = 0
        #need to figure out what n is, it is the perpendicular vector to the plane
        if self.intersectPlane(n=self.planenormal.unit(), p0=self.position.unit(),
                               l0=r.position.unit(), l=r.velocity.unit(), t=t):
            p: Vector = r.position + r.velocity * t
            v: Vector = p - self.position
            d2 = v.dot(v)
            return d2 <= self.radius2

    def get_luminance(self, out_position: Vector, out_direction: Vector) -> Spectrum:
        return Spectrum(0, 0, 255)