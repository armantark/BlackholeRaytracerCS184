from utils import Vector, Ray

class Camera:
    def __init__(self, position=Vector(0.5, 0.5, 0), fov=(0.5, 0.33), resolution=(800, 600)):
        self.position = position
        self.fov = fov
        self.resolution = resolution

    def cast_ray(self, pixel):
        ray_direction = Vector(
            (pixel[0] / self.resolution[0] - 0.5) * self.fov[0],
            (pixel[1] / self.resolution[1] - 0.5) * self.fov[1],
            1
        )

        ray = Ray(origin=self.position, direction=ray_direction.unit())
        return ray
