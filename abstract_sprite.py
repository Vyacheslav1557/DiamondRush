import pygame
import typing


class AbstractSprite(pygame.sprite.Sprite):
    """
    Sprite base class.
    """

    def __init__(self,
                 group: typing.Union[None, pygame.sprite.Group] = None,
                 ) -> None:
        """
        Initialization of the object.

        :param group: sprite group where to put the object.
        """
        if group is not None:
            super().__init__(group)
        else:
            super().__init__()
