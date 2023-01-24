import typing
import constants
import pygame
import abstract_sprite
import preload

DX = DY = 2


class ForeFinger(abstract_sprite.AbstractSprite):
    """
    Forefinger sprite. It is used in the menu.
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
        :param group: sprite group where to put the object.
        """
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect().move(*coordinates)

    def move(self, coordinates: typing.Tuple[int, int]) -> None:
        """
        Moves the sprite.

        :param coordinates: new coordinates (top left).
        """
        self.rect.x, self.rect.y = coordinates

    def shake(self, b: bool) -> None:
        """
        An animation of shaking.

        :param b: direction of motion.
        """
        if b:
            self.rect.y += 20
        else:
            self.rect.y -= 20


class MiniPlayer(abstract_sprite.AbstractSprite):
    """
    Mini player. It is used in map menu as a pointer.
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
        :param group: sprite group where to put the object.
        """
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect().move(*coordinates)

    def move(self, coordinates: typing.Tuple[int, int]) -> None:
        """
        Moves the sprite.

        :param coordinates: new coordinates (top left).
        """
        self.rect.x, self.rect.y = coordinates


class Leaf(abstract_sprite.AbstractSprite):
    """
    Sprite of one tile of leaves. It is used in map rendering.
    """

    def __init__(self, raw_coordinates: typing.Tuple[int, int], group: pygame.sprite.Group = None) -> None:
        """
        Initialization of the sprite.

        :param raw_coordinates: an initial coordinates (x and y of matrix).
        :param group: sprite group where to put the sprite.
        """
        super().__init__(group)
        self.images = [preload.load_image(filename) for filename in constants.LEAVES_IMAGE_NAMES]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.raw_x, self.raw_y = raw_coordinates
        self.t = -1

    def disappear(self, t: int) -> None:
        """
        Starts an animation of disappearance.

        :param t: start time.
        """
        if self.t == -1:
            self.t = t

    def next_stage(self, t: int) -> None:
        """
        Provides an animation. Sprite is killed when animation ends.

        :param t: current time (based on this, the image changes).
        """
        if self.t == -1:
            return
        i = int((t - self.t) / constants.LEAVES_FALL_DELTA_TIME)
        if i >= len(self.images) - 1:
            self.kill()
            return
        self.image = self.images[i]


class FallingSprite(abstract_sprite.AbstractSprite):
    """
    Sprite with property to fall.
    """
    images = []

    def __init__(self, raw_coordinates: typing.Tuple[int, int], group: pygame.sprite.Group = None) -> None:
        """
        Initialization of the sprite.

        :param raw_coordinates: an initial coordinates (x and y of matrix).
        :param group: sprite group where to put the sprite.
        """
        super().__init__(group)
        self.raw_x, self.raw_y = raw_coordinates
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.cur_i = 0
        self.t = -1
        self.t2 = 0
        self.cur_pos = 0

    def fall(self, t: int, dx: int) -> None:
        """
        Provides an animation of falling.

        :param t: current time (if fall is called for the first time initializes it),
        (based on this, the image changes).
        :param dx: direction of falling (-1 - left, 0 - down, 1 - right).
        """
        if self.t == -1:
            self.t = t
            self.t2 = t
        elif t - self.t2 > constants.OBJECTS_FALL_DELTA_TIME:
            if dx == -1:
                self.raw_x -= 1
                self.raw_y += 1
            elif dx == 1:
                self.raw_x += 1
                self.raw_y += 1
            elif dx == 0:
                self.raw_y += 1
            self.cur_pos = 0
            self.t2 = self.t = t
        elif t - self.t > constants.OBJECTS_TWITCH_DELTA_TIME:
            self.cur_pos ^= 1
            if dx == -1:
                if self.cur_pos:
                    self.rect = self.rect.move(-DX, -DY)
                else:
                    self.rect = self.rect.move(DX, DY)
            elif dx == 1:
                if self.cur_pos:
                    self.rect = self.rect.move(DX, DY)
                else:
                    self.rect = self.rect.move(-DX, -DY)
            self.t = t


class Diamond(FallingSprite):
    """
    Sprite of one diamond. It is used in map rendering.
    """

    def __init__(self, raw_coordinates: typing.Tuple[int, int], group: pygame.sprite.Group = None) -> None:
        """
        Initialization of the sprite.

        :param raw_coordinates: an initial coordinates (x and y of matrix).
        :param group: sprite group where to put the sprite.
        """
        self.images = [preload.load_image(filename) for filename in constants.PURPLE_DIAMOND_IMAGE_NAMES]
        super().__init__(raw_coordinates, group)

    def next_image(self) -> None:
        """
        Provides an animation.
        """
        self.cur_i = (self.cur_i + 1) % len(self.images)
        self.image = self.images[self.cur_i]


class Rock(FallingSprite):
    """
    Sprite of one rock. It is used in map rendering.
    """

    def __init__(self, raw_coordinates: typing.Tuple[int, int], group: pygame.sprite.Group = None) -> None:
        """
        Initialization of the sprite.

        :param raw_coordinates: an initial coordinates (x and y of matrix).
        :param group: sprite group where to put the sprite.
        """
        self.images = [preload.load_image(filename) for filename in constants.ROCKS_IMAGE_NAMES]
        self.t3 = -1
        super().__init__(raw_coordinates, group)

    def move(self, dx: int, t: int) -> bool:
        """
        Provides motion.

        :param dx: direction of motion (dx > 0 - right, dx <= 0 - left).
        :param t: current time (if move is called for the first time initializes it),
        (based on this, sprite moves).
        :return: True if move is successful else False.
        """
        if self.t3 == -1:
            self.t3 = t
        elif t - self.t3 >= constants.ROCK_MOVE_DELTA_TIME:
            self.t3 = t
            self.raw_x += 1 if dx > 0 else -1
            return True
        return False

    def next_image(self, direction: int) -> None:
        """
        Provides an animation of motion.

        :param direction: direction of motion (1 - right, -1 - left).
        """
        if direction == 1:
            self.cur_i = (self.cur_i + 1) % len(self.images)
        else:
            self.cur_i = (self.cur_i - 1) % len(self.images)
        self.image = self.images[self.cur_i]
