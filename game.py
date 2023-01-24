import pygame
import pytmx
import constants
import preload
import text
import window_stages
import typing
import protagonist
import advanced_sprites
import common_sprites
import widgets
import saving_stat

raw_x, raw_y = -1000, -1000
CENTER = 400, 400
dt = 5
KDT = 200
ST_KD = 200
DKD = 4000
IDKD = 100
DYINGDT = 2000
DYINGADT = 600
DYINGHALLERTDT = 600

all_sprites = None
player_group = None
diamonds = None
rocks = None
leaves = None
unlocked = False


def init_groups() -> None:
    """
    Initialization of groups. Clears them if they already exist.
    """
    global all_sprites, player_group, diamonds, rocks, leaves, unlocked
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.GroupSingle()
    diamonds = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    leaves = pygame.sprite.Group()
    unlocked = False


def is_rock(rx: int, ry: int) -> typing.Union[None, pygame.sprite.Sprite]:
    """
    Checks if rock exists at such x and y.

    :param rx: x of matrix.
    :param ry: y of matrix.
    :return: sprite itself if such rock exists.
    """
    for sp in rocks:
        if sp.raw_x == rx and sp.raw_y == ry:
            return sp
    return None


def is_diamond(rx: int, ry: int) -> typing.Union[None, pygame.sprite.Sprite]:
    """
    Checks if diamond exists at such x and y.

    :param rx: x of matrix.
    :param ry: y of matrix.
    :return: sprite itself if such diamond exists.
    """
    for sp in diamonds:
        if sp.raw_x == rx and sp.raw_y == ry:
            return sp
    return None


def is_rock_or_diamond(rx: int, ry: int) -> typing.Union[None, pygame.sprite.Sprite]:
    """
    Checks if diamond or rock exists at such x and y.

    :param rx: x of matrix.
    :param ry: y of matrix.
    :return: sprite itself if such rock or diamond exists.
    """
    sp1 = is_rock(rx, ry)
    if sp1:
        return sp1
    sp2 = is_diamond(rx, ry)
    if sp2:
        return sp2
    return None


class Map:
    """
    Provides using a tiled map.
    """

    def __init__(self, filename: str) -> None:
        """
        Initialization of map.

        :param filename: path to map.
        """
        self.map = pytmx.load_pygame(filename)
        self.height = self.map.height
        self.width = self.map.width
        self.tile_width = self.map.tilewidth
        self.tile_height = self.map.tileheight
        self.init_extra()

    def get_player_initial_coordinates(self) -> typing.Tuple[int, int]:
        """
        Finds player initial coordinates using map.

        :return: x and y of matrix.
        """
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 4)
                if image is not None:
                    return x, y

    def init_extra(self) -> None:
        """
        Fills extra groups.
        """
        for y in range(self.height):
            for x in range(self.width):
                if self.map.get_tile_gid(x, y, 6) != 0:
                    advanced_sprites.Diamond((x, y), diamonds)
                if self.map.get_tile_gid(x, y, 7) != 0:
                    advanced_sprites.Leaf((x, y), leaves)
                if self.map.get_tile_gid(x, y, 8) != 0:
                    advanced_sprites.Rock((x, y), rocks)

    def theoretical_move(self, dx: int, dy: int) -> bool:
        """
        Checks if it is allowed to move.

        :param dx: projection of translation on the x-axis.
        :param dy: projection of translation on the y-axis.
        :return: True if it is allowed to move. Else false.
        """
        if not 0 <= raw_x + dx < self.width or not 0 <= raw_y + dy < self.height:
            return False
        if self.map.get_tile_gid(raw_x + dx, raw_y + dy, 1):
            return False
        for sp in rocks:
            if sp.raw_x == raw_x + dx and sp.raw_y == raw_y + dy:
                return False
        if self.map.get_tile_gid(raw_x + dx, raw_y + dy, 10) != 0 and not unlocked:
            return False
        return True

    def is_fully_empty(self, rx: int, ry: int, except_player: bool = False) -> bool:
        """
        Checks if such tile at rx and ry is empty.

        :param rx: x of matrix.
        :param ry: y of matrix.
        :param except_player: if is necessary to take account of the player position.
        :return: True if is fully empty. Else false.
        """
        if not 0 <= rx < self.width or not 0 <= ry < self.height:
            return False
        for i in range(1, 11):
            if i == 4 or i == 6 or i == 7 or i == 8 or i == 9:
                continue
            if self.map.get_tile_gid(rx, ry, i) != 0:
                return False
        for sp in leaves:
            if sp.raw_x == rx and sp.raw_y == ry and sp.t == -1:
                return False
        if is_rock_or_diamond(rx, ry):
            return False
        if not except_player and raw_x == rx and raw_y == ry:
            return False
        return True

    def is_exit(self, rx: int, ry: int) -> bool:
        """
        Checks if there is an exit at such rx and ry.

        :param rx: x of matrix.
        :param ry: y of matrix.
        :return: True if it is.
        """
        return self.map.get_tile_gid(rx, ry, 5) != 0


class Sight(pygame.Surface):
    """
    More common to call it camera. Specifies the position of the screen.
    """

    def __init__(self, game_map: Map) -> None:
        """
        Initialization of camera.

        :param game_map: map which to render.
        """
        self.game_map = game_map
        self.x0, self.y0 = 0, 0
        super().__init__((self.game_map.width * self.game_map.tile_width,
                          self.game_map.height * self.game_map.tile_height))

    def render(self, screen: pygame.Surface, *indexes: int) -> None:
        """
        Rendering the map.

        :param screen: surface of rendering.
        :param indexes: indexes of layers.
        """
        for i in indexes:
            rx, ry = self.x0, self.y0
            if i == 6:
                for sprite in diamonds:
                    x, y = sprite.raw_x, sprite.raw_y
                    x2, y2 = sprite.rect.topleft
                    screen.blit(sprite.image, (rx + x * self.game_map.tile_width + x2,
                                               ry + y * self.game_map.tile_height + y2))
            elif i == 7:
                for sprite in leaves:
                    x, y = sprite.raw_x, sprite.raw_y
                    screen.blit(sprite.image, (rx + x * self.game_map.tile_width,
                                               ry + y * self.game_map.tile_height))
            elif i == 8:
                for sprite in rocks:
                    x, y = sprite.raw_x, sprite.raw_y
                    x2, y2 = sprite.rect.topleft
                    screen.blit(sprite.image, (rx + x * self.game_map.tile_width + x2,
                                               ry + y * self.game_map.tile_height + y2))
            else:
                for y in range(self.game_map.height):
                    for x in range(self.game_map.width):
                        image = self.game_map.map.get_tile_image(x, y, i)
                        if image is not None:
                            if i == 10:
                                if unlocked:
                                    image = preload.load_image(constants.UNLOCKED_LOCK_IMAGE_NAME)
                            screen.blit(image, (rx + x * self.game_map.tile_width,
                                                ry + y * self.game_map.tile_height))

    def move(self) -> None:
        """
        Calculates the position of the screen.
        """
        player_group.sprite.rect.x = CENTER[0]
        player_group.sprite.rect.y = CENTER[1]
        self.x0 = -raw_x * constants.TILE_WIDTH + CENTER[0]
        self.y0 = -raw_y * constants.TILE_HEIGHT + CENTER[1]

        if raw_x * constants.TILE_WIDTH < CENTER[0]:
            player_group.sprite.rect.x = raw_x * constants.TILE_WIDTH
            self.x0 = 0
        elif raw_x * constants.TILE_WIDTH > (self.game_map.width - 1) * constants.TILE_WIDTH - CENTER[0]:
            player_group.sprite.rect.x = constants.WINDOW_WIDTH - (self.game_map.width - raw_x) * constants.TILE_WIDTH
            self.x0 = -self.game_map.width * constants.TILE_WIDTH + constants.WINDOW_WIDTH

        if raw_y * constants.TILE_WIDTH < CENTER[1]:
            player_group.sprite.rect.y = raw_y * constants.TILE_HEIGHT
            self.y0 = 0
        elif raw_y * constants.TILE_HEIGHT > (self.game_map.height - 1) * constants.TILE_HEIGHT - CENTER[1]:
            player_group.sprite.rect.y = constants.WINDOW_HEIGHT - (
                    self.game_map.height - raw_y) * constants.TILE_HEIGHT
            self.y0 = -self.game_map.height * constants.TILE_HEIGHT + constants.WINDOW_HEIGHT


class Game(window_stages.BasicWindow):
    def __init__(self) -> None:
        super(Game, self).__init__()

    def run_final_window(self, att: int, i: int) -> int:
        """
        Runs final window.

        :param att: amount of attempts.
        :param i: map index.
        :return: status (see window).
        """
        text_group = pygame.sprite.Group()
        text.String(220, 200, constants.GOLDEN_ALPHABET, "COMPLETE!", text_group, 3, (400, 80))

        self.available_levels = max(self.available_levels, min(self.available_levels + 1, 3))
        if self.available_levels == 3:
            self.info[0] = 0
        else:
            self.info[0] = 1
        self.amount_of_diamonds += self.max_amount_of_diamonds_per_map[i]
        saving_stat.save_stat(self.lives, self.amount_of_diamonds, self.available_levels)
        res = widgets.PushButton(0, 0, constants.GOLDEN_ALPHABET,
                                 f"{self.max_amount_of_diamonds_per_map[i]}/{self.max_amount_of_diamonds_per_map[i]}",
                                 None,
                                 3, (400, 50), None, (0, 0),
                                 preload.load_image(constants.MAP_DIAMOND,
                                                    None, 2.6)).image
        text.String(280, 500, constants.GOLDEN_ALPHABET, f"{att} retries",
                    text_group, 3, (400, 50))
        con = widgets.PushButton(280, 700, constants.GOLDEN_ALPHABET,
                                 "continue",
                                 text_group,
                                 3, (400, 50), None, (0, 0))

        while True:
            self.screen.fill(constants.BLACK_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if con.rect.collidepoint(*event.pos):
                            return 7
            text_group.draw(self.screen)
            self.screen.blit(res, (300, 300))
            pygame.display.flip()

    def pause(self) -> int:
        """
        Pauses th game and shows pause menu.
        :return: status (see window).
        """
        amount_of_options = 4
        screenshot = self.screen.copy()
        main_group = pygame.sprite.Group()
        buttons_group = pygame.sprite.Group()
        indent = 20
        upper = constants.WINDOW_HEIGHT - constants.TILE_HEIGHT * (amount_of_options + 1) - indent
        lower = constants.WINDOW_HEIGHT - 4 - indent
        sp1 = common_sprites.PrimarySprite(
            pygame.surface.Surface((constants.WINDOW_WIDTH,
                                    constants.TILE_HEIGHT * amount_of_options),
                                   pygame.SRCALPHA).convert_alpha(),
            (0, upper), main_group
        )
        sp1.image.fill(constants.BLACK_COLOR)

        sp2 = common_sprites.PrimarySprite(
            pygame.surface.Surface((constants.WINDOW_WIDTH, 4), pygame.SRCALPHA).convert_alpha(),
            (0, upper), main_group
        )
        sp2.image.fill(constants.WHITE_COLOR)
        sp3 = common_sprites.PrimarySprite(
            pygame.surface.Surface((constants.WINDOW_WIDTH, 4), pygame.SRCALPHA).convert_alpha(),
            (0, lower - constants.TILE_HEIGHT), main_group
        )
        sp3.image.fill(constants.WHITE_COLOR)

        indent = 10
        n = 5
        surface_size = (constants.WINDOW_WIDTH, constants.TILE_HEIGHT - 5)
        col = constants.MENU_LIGHT_ORANGE_COLOR
        btn5 = widgets.PushButton(0, lower - constants.TILE_HEIGHT * 4, constants.GOLDEN_ALPHABET,
                                  "RESUME", None, n, surface_size, col, (180, indent))
        btn4 = widgets.PushButton(0, lower - constants.TILE_HEIGHT * 3, constants.GOLDEN_ALPHABET,
                                  "RESTART", None, n, surface_size, col, (170, indent))
        btn1 = widgets.PushButton(0, lower - constants.TILE_HEIGHT * 2, constants.GOLDEN_ALPHABET,
                                  "GO TO MAP", None, n, surface_size, col, (140, indent))
        btn0 = widgets.PushButton(0, lower - constants.TILE_HEIGHT, constants.GOLDEN_ALPHABET,
                                  "MAIN MENU", None, n, surface_size, col, (100, indent))
        buttons_group.add(btn0, btn1, btn4, btn4, btn5)
        main_group.add(buttons_group)
        mean = [6, 7, 11, -1]
        cur = amount_of_options - 1
        while True:
            self.screen.blit(screenshot, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        buttons_group.sprites()[cur].release()
                        cur += 1
                    elif event.key == pygame.K_DOWN:
                        buttons_group.sprites()[cur].release()
                        cur -= 1
                    elif event.key == pygame.K_RETURN:
                        return mean[cur]
                    elif event.key == pygame.K_ESCAPE:
                        return -1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        for i, sp in enumerate(buttons_group):
                            if sp.rect.collidepoint(event.pos):
                                if cur == i:
                                    return mean[cur]
                                buttons_group.sprites()[cur].release()
                                cur = i
                cur %= amount_of_options
                buttons_group.sprites()[cur].press()
            main_group.draw(self.screen)
            pygame.display.flip()

    def run_game(self, i: int, att: int = 0) -> typing.Union[typing.Tuple[int], typing.Tuple[int, int, int]]:
        """
        Runs the game.

        :param i: map index.
        :param att: amount of attempts.
        :return: status (see window).
        """
        init_groups()
        global raw_x, raw_y, all_sprites, unlocked
        game_map = Map(constants.MAPS[i])
        raw_x, raw_y = game_map.get_player_initial_coordinates()
        player = protagonist.Protagonist((0, 0), player_group)
        score_board = pygame.sprite.GroupSingle()
        sight = Sight(game_map)
        sight.move()
        picked_diamonds = 0
        common_sprites.PrimarySprite(
            preload.load_image(constants.SCORE_BOARD_FILE_IMAGE_NAME, ), (0, 0), score_board)
        all_sprites.add(player_group)

        def stat_update():
            score_board.sprite.image.blit(preload.load_image(constants.SCORE_BOARD_FILE_IMAGE_NAME, ), (0, 0))
            score_board.sprite.image.blit(
                widgets.PushButton(0, 0, constants.GOLDEN_ALPHABET, f"{self.lives}  ",
                                   None,
                                   3, (400, 50), None, (0, 0),
                                   preload.load_image(constants.HEAD,
                                                      None, 2)).image, (200, 0)
            )
            score_board.sprite.image.blit(
                widgets.PushButton(0, 0, constants.GOLDEN_ALPHABET,
                                   f"{picked_diamonds}/{self.max_amount_of_diamonds_per_map[i]}",
                                   None,
                                   3, (400, 50), None, (0, 0),
                                   preload.load_image(constants.MAP_DIAMOND,
                                                      None, 2.6)).image, (500, 0)
            )

        stat_update()
        st_kd = 0
        kd = 0
        clock = pygame.time.Clock()
        time = 0
        dkd = 0
        inner_dkd = 0
        ddt = 0
        dadt = 0
        reps = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ans = self.pause()
                        if ans != -1:
                            return ans, i, att
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        pass
            self.screen.fill(constants.BLACK_COLOR)
            t = clock.get_time()
            kd -= t
            st_kd += t
            time += t
            dkd += t
            inner_dkd += t
            dadt += t
            if kd <= 0:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_RIGHT]:
                    sp = is_rock(raw_x + 1, raw_y)
                    if game_map.theoretical_move(1, 0):
                        raw_x += 1
                        sight.move()
                        if not game_map.theoretical_move(0, 1):
                            player.set_m(1)
                        else:
                            player.set_cl_right()
                        kd = KDT
                    elif sp is not None:
                        if game_map.is_fully_empty(raw_x + 2, raw_y):
                            if sp.move(constants.TILE_WIDTH, time):
                                raw_x += 1
                                sight.move()
                                sp.next_image(1)
                        player.set_drag(1)
                        kd = KDT
                elif pressed_keys[pygame.K_LEFT]:
                    sp = is_rock(raw_x - 1, raw_y)
                    if game_map.theoretical_move(-1, 0):
                        raw_x -= 1
                        sight.move()
                        if not game_map.theoretical_move(0, 1):
                            player.set_m(-1)
                        else:
                            player.set_cl_left()
                        kd = KDT
                    elif sp is not None:
                        if game_map.is_fully_empty(raw_x - 2, raw_y):
                            if sp.move(-constants.TILE_WIDTH, time):
                                raw_x -= 1
                                sight.move()
                                sp.next_image(-1)
                        player.set_drag(-1)
                        kd = KDT
                elif pressed_keys[pygame.K_UP]:
                    if game_map.theoretical_move(0, -1):
                        raw_y -= 1
                        sight.move()
                        player.set_cl()
                        kd = KDT
                elif pressed_keys[pygame.K_DOWN]:
                    if game_map.theoretical_move(0, 1):
                        raw_y += 1
                        sight.move()
                        player.set_cl()
                        kd = KDT
                else:
                    if st_kd >= ST_KD and ddt < DYINGDT:
                        if not game_map.theoretical_move(0, 1):
                            player.set_stay()
                        else:
                            player.image = player.climbing_up_images[0]
                        st_kd = 0
            for sp in leaves:
                if sp.raw_x == raw_x and sp.raw_y == raw_y:
                    sp.disappear(time)
                sp.next_stage(time)
            if dkd >= DKD:
                if inner_dkd >= IDKD:
                    for sp in diamonds:
                        sp.next_image()
                    inner_dkd = 0
                    reps += 1
                if reps == 4:
                    dkd = 0
                    reps = 0
            for sp in rocks:
                rx, ry = sp.raw_x, sp.raw_y
                if is_rock_or_diamond(rx, ry + 1):
                    if game_map.is_fully_empty(rx - 1, ry) and game_map.is_fully_empty(rx - 1, ry + 1):
                        sp.fall(time, -1)
                    elif game_map.is_fully_empty(rx + 1, ry) and game_map.is_fully_empty(rx + 1, ry + 1):
                        sp.fall(time, 1)
                    else:
                        sp.t = -1
                elif game_map.is_fully_empty(rx, ry + 1, except_player=True):
                    if rx == raw_x and ry + 1 == raw_y:
                        ddt += clock.get_time()
                        if DYINGDT > ddt >= DYINGHALLERTDT:
                            player.image = player.dying_under_rock_images[0]
                        if ddt >= DYINGDT:
                            if dadt >= DYINGADT:
                                player.die_under_rock()
                                dadt = 0
                            if player.d2 == len(player.dying_under_rock_images) - 1:
                                if self.lives - 1 == 0:
                                    self.available_levels = 0
                                    self.amount_of_diamonds = 0
                                    self.amount_of_options = 5
                                    self.lives = 1
                                    self.info[0] = 1
                                    saving_stat.save_stat(self.lives, self.amount_of_diamonds, self.available_levels)
                                    return 6,
                                else:
                                    self.lives -= 1
                                    saving_stat.save_stat(self.lives, self.amount_of_diamonds, self.available_levels)
                                    return 11, i, att + 1
                    else:
                        ddt = 0
                        sp.fall(time, 0)
                else:
                    sp.t = -1
            for sp in diamonds:
                rx, ry = sp.raw_x, sp.raw_y
                if is_rock_or_diamond(rx, ry + 1):
                    if game_map.is_fully_empty(rx - 1, ry) and game_map.is_fully_empty(rx - 1, ry + 1):
                        sp.fall(time, -1)
                    elif game_map.is_fully_empty(rx + 1, ry) and game_map.is_fully_empty(rx + 1, ry + 1):
                        sp.fall(time, 1)
                    else:
                        sp.t = -1
                elif game_map.is_fully_empty(rx, ry + 1):
                    sp.fall(time, 0)
                else:
                    sp.t = -1
            sight.render(self.screen, 0, 1, 2, 5, 10, 6, 7, 8)  # 9 - checkpoints
            all_sprites.draw(self.screen)
            sight.render(self.screen, 3)
            for sp in diamonds:
                if sp.raw_x == raw_x and sp.raw_y == raw_y:
                    picked_diamonds += 1
                    stat_update()
                    sp.kill()
            score_board.draw(self.screen)
            pygame.display.flip()
            clock.tick()
            if picked_diamonds == self.max_amount_of_diamonds_per_map[i]:
                unlocked = True
            if game_map.is_exit(raw_x, raw_y):
                return self.run_final_window(att, i),
            # print(clock.get_fps())
