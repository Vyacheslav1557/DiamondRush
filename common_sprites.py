import constants
import pygame
import typing
import abstract_sprite


class Tile(abstract_sprite.AbstractSprite):
    """
    An sprite called tile. Is used as parts of background.
    """

    def __init__(self,
                 image: pygame.Surface,
                 raw_coordinates: typing.Tuple[int, int],
                 group: pygame.sprite.Group = None,
                 ) -> None:
        """
        Initialization of the sprite.

        :param image: the image which represents the sprite.
        :param raw_coordinates: an initial coordinates (x and y of matrix).
        :param group: sprite group where to put the sprite.
        """
        super().__init__(group)
        self.image = image
        self.raw_x, self.raw_y = raw_coordinates
        self.rect = self.image.get_rect().move(constants.TILE_WIDTH * self.raw_x,
                                               constants.TILE_HEIGHT * self.raw_y)


class PrimarySprite(abstract_sprite.AbstractSprite):
    """
    An sprite with an image.
    """

    def __init__(self,
                 image: pygame.Surface,
                 coordinates: typing.Tuple[int, int],
                 group: pygame.sprite.Group = None,
                 ) -> None:
        """
        Initialization of the sprite.

        :param image: the image which represents the sprite.
        :param coordinates: an initial coordinates (top left).
        :param group: sprite group where to put the sprite.
        """
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect().move(*coordinates)
