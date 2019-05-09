# import your favorite argument parser here
from renderer.renderer import render
from renderer import Camera, World
from objects import BlackHole, Disk

import numpy as np

from objects.disk import Disk

def normalize_vector(v: np.array) -> np.array:
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

# import plac
# @plac.annotation
def main():
    disk_direction = normalize_vector(np.array([-1, 20, -1]))

    world_radius = 50000

    black_hole = BlackHole(mass=1.989e30, origin=np.array([world_radius]*3))
    disk = Disk(
        origin=np.array([world_radius]*3),
        normal=disk_direction,
        inner_radius=black_hole.radius * 3,
        outer_radius=black_hole.radius * 6
    )

    # disk = Disk()

    world = World(objects=[black_hole, disk], size=np.array([world_radius*2]*3))
    camera = Camera(resolution=(450, 270), fov=(1, 0.66), position=np.array([world_radius,world_radius,0]))
    image = render(world, camera)
    image.save('test_render_higherres.png')


if __name__ == '__main__':
    main()
