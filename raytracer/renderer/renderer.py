from PIL import Image, ImageDraw
from .world import World
from .camera import Camera
from objects import BlackHole

def render(world: World, camera: Camera) -> Image.Image:
    pass


def test_render(dimensions=(800,600)) -> Image.Image:
    black_hole = BlackHole(None, None)
    color = black_hole.get_luminance(None)

    image = Image.new('RGB', dimensions)
    draw = ImageDraw.Draw(image)

    draw.rectangle((12, 12, 80, 32), fill=(255, 255, 255))
    draw.text((18, 18), 'Test', fill=tuple(color))

    return image
