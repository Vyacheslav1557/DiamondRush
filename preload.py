import typing
import pygame
import PIL.Image


def scaled(filename: str, n: typing.Union[int, float]) -> PIL.Image:
    """
    Scales an image.

    :param filename: path to image.
    :param n: scaling factor.
    :return: image (PIL format).
    """
    img = PIL.Image.open(filename)
    width, height = img.size
    return img.resize((round(width * n), round(height * n)), resample=PIL.Image.NEAREST)


def converted(image: PIL.Image) -> pygame.Surface:
    """
    Converts an image.
    :param image: image (PIL format).
    :return: image (pygame format).
    """
    mode = image.mode
    size = image.size
    data = image.tobytes()
    return pygame.image.fromstring(data, size, mode)


def load_image(filename: str,
               color_key: pygame.Color = None,
               n: typing.Union[int, float] = 1,
               ) -> pygame.Surface:
    """

    :param filename: path to image.
    :param color_key: pixel which to delete.
    :param n: scaling factor.
    :return: image (pygame format).
    """
    image = scaled(filename, n) if n != 1 else PIL.Image.open(filename)
    if color_key is not None:
        image = converted(image).convert()
        image.set_colorkey(color_key)
    else:
        image = converted(image).convert_alpha()
    return image
