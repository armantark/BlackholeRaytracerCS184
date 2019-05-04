# import your favorite argument parser here
from renderer.renderer import render
from renderer import Camera, World
from objects import BlackHole

# import plac
# @plac.annotation
def main():
    black_hole = BlackHole()
    world = World(objects=[black_hole])
    camera = Camera()
    image = render(world, camera)
    image.save('test_render.png')


if __name__ == '__main__':
    main()
