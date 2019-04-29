# import your favorite argument parser here
from renderer.renderer import test_render

if __name__ == '__main__':
    print('Hello, World!')
    test_image = test_render()
    test_image.save('test_render.png')
