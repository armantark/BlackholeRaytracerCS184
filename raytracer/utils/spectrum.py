from dataclasses import dataclass


@dataclass
class Spectrum:
    r: float = 0
    g: float = 0
    b: float = 0

    def __add__(self, other):
        return Spectrum(self.r + other.r, self.g + other.g, self.b + other.b)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Spectrum(self.r - other.r, self.g - other.g, self.b - other.b)

    def __rsub__(self, other):
        raise RuntimeError("???")

    def __mul__(self, other):
        return Spectrum(self.r * other.r, self.g * other.g, self.b * other.b)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return Spectrum(self.r / other.r, self.g / other.g, self.b / other.b)

    def illum(self) -> float:
        return 0.2126 * self.r + 0.7152 * self.g + 0.0722 * self.b

    def __iter__(self):
        return iter((self.r, self.g, self.b))
