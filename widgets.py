import text
import typing
import pygame
import constants


class PushButton(text.String):
    """
    Push button sprite.
    """

    def __init__(self,
                 left: int, bottom: int,
                 alphabet: dict,
                 line: str,
                 group: pygame.sprite.Group = None,
                 n: int = 1,
                 surface_size: typing.Tuple[int, int] = constants.WINDOW_SIZE,
                 color: pygame.Color = None,
                 indent: typing.Tuple[int, int] = (0, 0),
                 *extra: pygame.Surface
                 ) -> None:
        """
        Initialization of the push button.

        :param left: left x border.
        :param bottom: lower border y coordinate.
        :param alphabet: alphabet.
        :param line: string which to show.
        :param group: sprite group where to put the sprite.
        :param n: scaling factor.
        :param surface_size: surface_size.
        :param indent: indent from left border and lower border.
        :param extra: some other images.
        """
        self.extra = extra
        super().__init__(left, bottom, alphabet, line, group, n, surface_size, indent)
        self.color = color

    def show(self, indent=None) -> None:
        """
        Renders the string.

        :param indent: indent from left border and lower border.
        """
        ix, iy = super().show(indent)
        for img in self.extra:
            width, height = img.get_rect().size
            self.image.blit(img, (ix, self.rect.height - iy - height))
            ix += width

    def press(self) -> None:
        """
        Presses the push button.
        """
        self.image.fill(self.color)
        self.show()

    def release(self) -> None:
        """
        Releases the push button.
        """
        self.image.fill(constants.TRANSPARENT_COLOR)
        self.show()
