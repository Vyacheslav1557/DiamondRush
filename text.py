import pygame
import typing
import constants
import abstract_sprite
import preload

_symbol_images = {
}


class Symbol(abstract_sprite.AbstractSprite):
    """
    One symbol sprite.
    """

    def __init__(self,
                 filename: str,
                 coordinates: typing.Tuple[int, int] = (0, 0),
                 n: int = 1,
                 group: pygame.sprite.Group = None,
                 ) -> None:
        """
        Initialization of the sprite.

        :param filename: path to image.
        :param coordinates: initial coordinates (top left).
        :param n:
        :param group:
        """
        super().__init__(group)
        if (filename, n) not in _symbol_images:
            _symbol_images[(filename, n)] = preload.load_image(filename, constants.COLOR_KEY, n)
        self.image = _symbol_images[(filename, n)]
        self.rect = self.image.get_rect().move(*coordinates)


class String(abstract_sprite.AbstractSprite):
    """
    One string sprite.
    """

    def __init__(self,
                 left: int, bottom: int,
                 alphabet: dict,
                 line: str,
                 group: pygame.sprite.Group = None,
                 n: int = 1,
                 surface_size: typing.Tuple[int, int] = constants.WINDOW_SIZE,
                 indent: typing.Tuple[int, int] = (0, 0),
                 ) -> None:
        """
        Initialization of the string.

        :param left: left x border.
        :param bottom: lower border y coordinate.
        :param alphabet: alphabet.
        :param line: string which to show.
        :param group: sprite group where to put the sprite.
        :param n: scaling factor.
        :param surface_size: surface_size.
        :param indent: indent from left border and lower border.
        """
        super().__init__(group)
        self.image = pygame.Surface(surface_size, pygame.SRCALPHA).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
        self.line = line
        self.n = n
        self.alphabet = alphabet
        self.indent = indent
        self.show()

    def show(self, indent=None) -> typing.Tuple[int, int]:
        """
        Renders the string.

        :param indent: indent from left border and lower border.
        :return: new indent from left border and lower border.
        """
        if indent is None:
            indent = self.indent
        ix, iy = indent
        for char in self.line:
            sb = Symbol(self.alphabet[char], n=self.n).image
            width, height = sb.get_rect().size
            self.image.blit(sb, (ix, self.rect.height - iy - height))
            ix += width
        return ix, iy
