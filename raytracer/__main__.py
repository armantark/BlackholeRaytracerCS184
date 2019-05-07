# import your favorite argument parser here
from renderer.renderer import render
from renderer import Camera, World
from objects import BlackHole, Disk

import numpy as np

from objects.disk import TestDisk

def normalize_vector(v: np.array) -> np.array:
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

# import plac
# @plac.annotation
def main():
    disk_direction = normalize_vector(np.array([-1, -1, -1]))

    black_hole = BlackHole()
    # disk = TestDisk(
    #     normal=disk_direction,
    #     inner_radius=black_hole.radius * 3,
    #     outer_radius=black_hole.radius * 6
    # )

    disk = TestDisk()

    world = World(objects=[black_hole, disk])
    #resolution = 150, 100
    camera = Camera(resolution=(150, 100))
    image = render(world, camera)
    image.save('test_render_higherres.png')


if __name__ == '__main__':
    main()
