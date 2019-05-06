# import your favorite argument parser here
from renderer.renderer import render
from renderer import Camera, World
from objects import BlackHole, Disk

# import plac
# @plac.annotation
def main():
    black_hole = BlackHole()
    disk = Disk()
    world = World(objects=[black_hole, disk])
    #ratio: 100, 67
    camera = Camera(resolution=(200, 134))
    image = render(world, camera)
    image.save('test_render_higherres.png')


if __name__ == '__main__':
    main()
