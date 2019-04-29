from dataclasses import dataclass
from math import sqrt

@dataclass
class Vector:
    x: double = 0
    y: double = 0
    z: double = 0

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __rsub__(self, other):
        raise RuntimeError("wut")

    def __mul__(self, other: float):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float):
        return self.__mul__(1.0/other)

    def norm(self):
        return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def normalize(self):
        norm = self.norm()
        self.x /= norm
        self.y /= norm
        self.z /= norm

    def dot(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

