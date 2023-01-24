import pygame
import typing
import constants
import preload


class Protagonist(pygame.sprite.Sprite):
    """
    Player sprite.
    """

    def __init__(self, coordinates: typing.Tuple[int, int], group: pygame.sprite.Group = None) -> None:
        """
        Initialization of the sprite.

        :param coordinates: an initial coordinates (top left).
        :param group: sprite group where to put the object.
        """
        super().__init__(group)
        n = 80 / 26
        self.hit_images = [preload.load_image(filename, None, n)
                           for filename in constants.HIT_IMAGE_NAMES]
        self.drag_images = [preload.load_image(filename, None, n)
                            for filename in constants.DRAG_IMAGE_NAMES]
        self.moving_images = [preload.load_image(filename, None, n)
                              for filename in constants.MOVING_IMAGE_NAMES]
        self.staying_images = [preload.load_image(filename, None, n)
                               for filename in constants.STAYING_IMAGE_NAMES]
        self.shot_images = [preload.load_image(filename, None, n)
                            for filename in constants.SHOT_IMAGE_NAMES]
        self.climbing_up_images = [preload.load_image(filename, None, n)
                                   for filename in constants.CLIMBING_UP_IMAGE_NAMES]
        self.climbing_right_images = [preload.load_image(filename, None, n)
                                      for filename in constants.CLIMBING_RIGHT_IMAGE_NAMES]
        self.dying_under_rock_images = [preload.load_image(filename, None, n)
                                        for filename in constants.DYING_UNDER_ROCK_IMAGE_NAMES]
        self.status = 0
        self.image = self.staying_images[0]
        self.rect = self.image.get_rect().move(*coordinates)
        self.m = 0
        self.cl = 0
        self.cl_side = 0
        self.st = 0
        self.d = 0
        self.d2 = 0

    def set_m(self, direction: int) -> None:
        """
        Provides an animation of walking.

        :param direction: direction of motion (1 - right, -1 - left).
        """
        if direction == 1:
            self.image = self.moving_images[self.m]
        else:
            self.image = pygame.transform.flip(self.moving_images[self.m], True, False)
        self.m = (self.m + 1) % len(self.moving_images)

    def set_cl(self) -> None:
        """
        Provides an animation of climbing.
        """
        self.image = self.climbing_up_images[self.cl]
        self.cl = (self.cl + 1) % len(self.climbing_up_images)

    def set_cl_right(self) -> None:
        """
        Provides an animation of climbing right.
        """
        self.image = self.climbing_right_images[self.cl_side]
        self.cl_side = (self.cl_side + 1) % len(self.climbing_right_images)

    def set_cl_left(self) -> None:
        """
        Provides an animation of climbing left.
        """
        self.image = pygame.transform.flip(self.climbing_right_images[self.cl_side], True, False)
        self.cl_side = (self.cl_side + 1) % len(self.climbing_right_images)

    def set_stay(self) -> None:
        """
        Provides an animation of staying.
        """
        self.image = pygame.Surface(constants.TILE_SIZE, pygame.SRCALPHA).convert_alpha()
        img = self.staying_images[self.st]
        self.image.blit(img, (0, constants.TILE_HEIGHT - img.get_height()))
        self.st = (self.st + 1) % len(self.staying_images)

    def set_drag(self, direction: int) -> None:
        """
        Provides an animation of dragging a rock.

        :param direction: direction of motion (1 - right, -1 - left).
        """
        self.image = pygame.Surface(constants.TILE_SIZE, pygame.SRCALPHA).convert_alpha()
        if direction == 1:
            img = self.drag_images[self.d]
        else:
            img = pygame.transform.flip(self.drag_images[self.d], True, False)
        self.image.blit(img, (0, constants.TILE_HEIGHT - img.get_height()))
        self.d = (self.d + 1) % len(self.drag_images)

    def die_under_rock(self):
        """
        Provides an animation of dying under rock.
        """
        self.image = pygame.Surface(constants.TILE_SIZE, pygame.SRCALPHA).convert_alpha()
        img = self.dying_under_rock_images[self.d2]
        self.image.blit(img,
                        (constants.TILE_WIDTH // 2 - img.get_width() // 2,
                         constants.TILE_HEIGHT - img.get_height())
                        )
        self.d2 = (self.d2 + 1) % len(self.dying_under_rock_images)
