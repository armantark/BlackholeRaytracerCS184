class Disk:
    def __init__(self, position: Vector = Vector(0.5, 0.5, 0.5),
                 rotation: Vector = Vector(0, 0, 0), radius: float = 0.75):
        self.position = position
        self.rotation = rotation
        self.radius = radius

    def hit_by_ray(self, r: Ray, last_position: Vector) -> bool:
        if (r.position - self.position).norm() <= (2.5 * self.radius):  # photon sphere
            return True

        return False

    def get_luminance(self, out_position: Vector, out_direction: Vector) -> Spectrum:
        return Spectrum(0, 0, 255)