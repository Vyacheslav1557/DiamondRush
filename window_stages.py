import typing
import advanced_sprites
import constants
import pygame
import sys
import preload
import common_sprites
import text
import widgets
import saving_stat


class BasicWindow:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode(constants.WINDOW_SIZE)
        pygame.display.set_caption(constants.WINDOW_TITLE)

    @staticmethod
    def terminate() -> None:
        """
        Terminates the window.
        """
        pygame.quit()
        sys.exit()


class Menu(BasicWindow):
    def __init__(self) -> None:
        super(Menu, self).__init__()

    def show_menu(self, amount_of_options: int) -> int:
        """
        :param amount_of_options: amount_of_options.
        :return: status (see window).
        """
        tiles_group = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        buttons_group = pygame.sprite.Group()
        bricks_font = preload.load_image(constants.BRICKS_BACKGROUND_FILE_IMAGE_NAME)
        for y in range(constants.WINDOW_HEIGHT_MEASURED_IN_TILES):
            for x in range(constants.WINDOW_WIDTH_MEASURED_IN_TILES):
                tiles_group.add(common_sprites.Tile(bricks_font, (x, y)))
        logo = common_sprites.PrimarySprite(preload.load_image(constants.STARTING_LOGO_FILE_IMAGE_NAME),
                                            (148, -30))
        indent = 20
        upper = constants.WINDOW_HEIGHT - constants.TILE_HEIGHT * amount_of_options - indent
        lower = constants.WINDOW_HEIGHT - 4 - indent
        sp1 = common_sprites.PrimarySprite(
            pygame.surface.Surface((constants.WINDOW_WIDTH,
                                    constants.TILE_HEIGHT * amount_of_options),
                                   pygame.SRCALPHA).convert_alpha(),
            (0, upper)
        )
        sp1.image.fill(constants.MENU_LIGHT_BLUE_COLOR)

        sp2 = common_sprites.PrimarySprite(
            pygame.surface.Surface((constants.WINDOW_WIDTH, 4), pygame.SRCALPHA).convert_alpha(),
            (0, upper)
        )
        sp2.image.fill(constants.WHITE_COLOR)
        sp3 = common_sprites.PrimarySprite(
            pygame.surface.Surface((constants.WINDOW_WIDTH, 4), pygame.SRCALPHA).convert_alpha(),
            (0, lower)
        )
        sp3.image.fill(constants.WHITE_COLOR)

        indent = 10
        n = 5
        surface_size = (constants.WINDOW_WIDTH, constants.TILE_HEIGHT - 5)
        col = constants.MENU_LIGHT_ORANGE_COLOR
        btn4 = widgets.PushButton(0, lower - constants.TILE_HEIGHT * 4, constants.GOLDEN_ALPHABET,
                                  "NEW GAME", None, n, surface_size, col, (111, indent))
        btn3 = widgets.PushButton(0, lower - constants.TILE_HEIGHT * 3, constants.GOLDEN_ALPHABET,
                                  "LEADERBOARD", None, n, surface_size, col, (15, indent))
        btn2 = widgets.PushButton(0, lower - constants.TILE_HEIGHT * 2, constants.GOLDEN_ALPHABET,
                                  "OPTIONS", None, n, surface_size, col, (180, indent))
        btn1 = widgets.PushButton(0, lower - constants.TILE_HEIGHT, constants.GOLDEN_ALPHABET,
                                  "HELP", None, n, surface_size, col, (255, indent))
        btn0 = widgets.PushButton(0, lower, constants.GOLDEN_ALPHABET,
                                  "EXIT", None, n, surface_size, col, (280, indent))
        buttons_group.add(btn0, btn1, btn2, btn3, btn4, btn4)
        if amount_of_options == 6:
            widgets.PushButton(0, lower - constants.TILE_HEIGHT * 5, constants.GOLDEN_ALPHABET,
                               "CONTINUE", buttons_group, n, surface_size, col, (130, indent))
        all_sprites.add(tiles_group,
                        logo,
                        sp1, buttons_group, sp2, sp3)
        cur = amount_of_options - 1
        while True:
            self.screen.fill(constants.BLACK_COLOR)
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
                        return cur
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        for i, sp in enumerate(buttons_group):
                            if sp.rect.collidepoint(event.pos):
                                if cur == i:
                                    return cur
                                buttons_group.sprites()[cur].release()
                                cur = i
                                buttons_group.sprites()[cur].press()
                cur %= amount_of_options
                buttons_group.sprites()[cur].press()
            all_sprites.draw(self.screen)
            pygame.display.flip()


class Help(BasicWindow):
    def __init__(self) -> None:
        super(Help, self).__init__()

    def show_help(self) -> int:
        """
        :return: status (see window).
        """
        all_sprites = pygame.sprite.Group()
        text_group = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        bricks_font = preload.load_image(constants.BRICKS_BACKGROUND_FILE_IMAGE_NAME)
        for y in range(constants.WINDOW_HEIGHT_MEASURED_IN_TILES):
            for x in range(constants.WINDOW_WIDTH_MEASURED_IN_TILES):
                tiles_group.add(common_sprites.Tile(bricks_font, (x, y)))
        n = 4
        surface_size = (constants.WINDOW_WIDTH, constants.TILE_HEIGHT)
        indent = 45
        upper = 80
        text.String(280, upper, constants.GOLDEN_ALPHABET, "HELP",
                    text_group, n, surface_size)
        text.String(160, upper + constants.TILE_HEIGHT, constants.GOLDEN_ALPHABET, "How to move:",
                    text_group, n, surface_size)
        n = 2
        text.String(130, upper + constants.TILE_HEIGHT + indent, constants.GOLDEN_ALPHABET,
                    "Press [Key right] to move right.", text_group, n, surface_size)
        text.String(140, upper + constants.TILE_HEIGHT + indent * 2, constants.GOLDEN_ALPHABET,
                    "Press [Key left] to move left.", text_group, n, surface_size)
        text.String(175, upper + constants.TILE_HEIGHT + indent * 3, constants.GOLDEN_ALPHABET,
                    "Press [Key up] to climb up.", text_group, n, surface_size)
        text.String(125, upper + constants.TILE_HEIGHT + indent * 4, constants.GOLDEN_ALPHABET,
                    "Press [Key down] to climb down.", text_group, n, surface_size)
        # text.String(115, upper + constants.TILE_HEIGHT + indent * 5.5, constants.GOLDEN_ALPHABET,
        #             "Press [Key space] to use a weapon.", text_group, n, surface_size)
        text.String(90, upper + constants.TILE_HEIGHT + indent * 7, constants.GOLDEN_ALPHABET,
                    "Press [Key enter] over a checkpoint to", text_group, n, surface_size)
        text.String(280, upper + constants.TILE_HEIGHT + indent * 8, constants.GOLDEN_ALPHABET,
                    "reset the room.", text_group, n, surface_size)
        text.String(110, upper + constants.TILE_HEIGHT + indent * 9.5, constants.GOLDEN_ALPHABET,
                    "Press [F4] to reset and lose a life.", text_group, n, surface_size)
        text.String(160, upper + constants.TILE_HEIGHT + indent * 11, constants.GOLDEN_ALPHABET,
                    "Press [ESC] to set a pause.", text_group, n, surface_size)
        bck_img = preload.load_image(constants.RETURN_BACK_FILE_IMAGE_NAME, constants.COLOR_KEY, n)
        btn0 = widgets.PushButton(constants.WINDOW_WIDTH - 120, constants.WINDOW_HEIGHT - 15,
                                  constants.GOLDEN_ALPHABET, "back ", None, n,
                                  (150, 30), None, (0, 0), bck_img)
        all_sprites.add(tiles_group, text_group, btn0)
        while True:
            self.screen.fill(constants.BLACK_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 6
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if btn0.rect.collidepoint(event.pos):
                            return 6
            all_sprites.draw(self.screen)
            pygame.display.flip()


class Options(BasicWindow):
    def __init__(self) -> None:
        super(Options, self).__init__()

    def show_options(self) -> int:
        """
        :return: status (see window).
        """
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        bricks_font = preload.load_image(constants.BRICKS_BACKGROUND_FILE_IMAGE_NAME)
        for y in range(constants.WINDOW_HEIGHT_MEASURED_IN_TILES):
            for x in range(constants.WINDOW_WIDTH_MEASURED_IN_TILES):
                tiles_group.add(common_sprites.Tile(bricks_font, (x, y)))
        n = 2
        bck_img = preload.load_image(constants.RETURN_BACK_FILE_IMAGE_NAME, constants.COLOR_KEY, n)
        btn0 = widgets.PushButton(constants.WINDOW_WIDTH - 120, constants.WINDOW_HEIGHT - 15,
                                  constants.GOLDEN_ALPHABET, "back ", None, n,
                                  (150, 30), None, (0, 0), bck_img)
        all_sprites.add(tiles_group, btn0)
        while True:
            self.screen.fill(constants.BLACK_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 6
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if btn0.rect.collidepoint(event.pos):
                            return 6
            all_sprites.draw(self.screen)
            pygame.display.flip()


class LeaderBoard(BasicWindow):
    def __init__(self) -> None:
        super(LeaderBoard, self).__init__()

    def show_leaderboard(self) -> int:
        """
        :return: status (see window).
        """
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        bricks_font = preload.load_image(constants.BRICKS_BACKGROUND_FILE_IMAGE_NAME)
        for y in range(constants.WINDOW_HEIGHT_MEASURED_IN_TILES):
            for x in range(constants.WINDOW_WIDTH_MEASURED_IN_TILES):
                tiles_group.add(common_sprites.Tile(bricks_font, (x, y)))
        n = 2
        bck_img = preload.load_image(constants.RETURN_BACK_FILE_IMAGE_NAME, constants.COLOR_KEY, n)
        btn0 = widgets.PushButton(constants.WINDOW_WIDTH - 120, constants.WINDOW_HEIGHT - 15,
                                  constants.GOLDEN_ALPHABET, "back ", None, n,
                                  (150, 30), None, (0, 0), bck_img)
        all_sprites.add(tiles_group, btn0)
        while True:
            self.screen.fill(constants.BLACK_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 6
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if btn0.rect.collidepoint(event.pos):
                            return 6
            all_sprites.draw(self.screen)
            pygame.display.flip()


class MapMenu(BasicWindow):
    def __init__(self) -> None:
        super(MapMenu, self).__init__()

    def show_mapmenu(self, a: int, b: int, c: int) -> int:
        """
        :param a: first location status.
        :param b: second location status.
        :param c: third location status.
        :return: status (see window).
        """
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        grass = preload.load_image(constants.GRASS_BACKGROUND_FILE_IMAGE_NAME)
        for y in range(constants.WINDOW_HEIGHT_MEASURED_IN_TILES):
            for x in range(constants.WINDOW_WIDTH_MEASURED_IN_TILES):
                tiles_group.add(common_sprites.Tile(grass, (x, y)))
        n = 2
        bck_img = preload.load_image(constants.RETURN_BACK_FILE_IMAGE_NAME, constants.COLOR_KEY, n)
        acc_img = preload.load_image(constants.ACCEPT_FILE_IMAGE_NAME, constants.COLOR_KEY, n)
        btn0 = widgets.PushButton(constants.WINDOW_WIDTH - 190, constants.WINDOW_HEIGHT - 15,
                                  constants.GOLDEN_ALPHABET, "main menu ", None, n,
                                  (200, 30), None, (0, 0), bck_img)
        btn1 = widgets.PushButton(15, constants.WINDOW_HEIGHT - 15,
                                  constants.GOLDEN_ALPHABET, "ok ", None, n,
                                  (150, 30), None, (0, 0), acc_img)
        n = 3
        mapmenu = common_sprites.PrimarySprite(preload.load_image(constants.MAP_MENU_FILE_IMAGE_NAME,
                                                                  constants.COLOR_KEY, n), (220, 100))
        btn_size = (80, 80)
        if a == 0:
            btn2 = widgets.PushButton(286, 253,
                                      {}, "", None, n,
                                      btn_size, None, (0, 0),
                                      preload.load_image(constants.FIRST_DIAMOND_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, n))
        elif a == 1:
            btn2 = widgets.PushButton(296, 236,
                                      {}, "", None, n,
                                      btn_size, None, (0, 0),
                                      preload.load_image(constants.FIRE_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, n))
        else:
            btn2 = widgets.PushButton(296, 236,
                                      {}, "", None, n,
                                      btn_size, None, (0, 0),
                                      preload.load_image(constants.FIRE0_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, n))
        if b == 0:
            btn3 = widgets.PushButton(430, 253,
                                      {}, "", None, n,
                                      btn_size, None, (0, 0),
                                      preload.load_image(constants.SECOND_DIAMOND_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, n))
        elif b == 1:
            btn3 = widgets.PushButton(439, 236,
                                      {}, "", None, n,
                                      btn_size, None, (0, 0),
                                      preload.load_image(constants.HELMET_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, n))
        else:
            btn3 = widgets.PushButton(439, 236,
                                      {}, "", None, n,
                                      btn_size, None, (0, 0),
                                      preload.load_image(constants.HELMET0_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, n))

        if c == 0:
            btn4 = widgets.PushButton(358, 394, {}, "", None, n,
                                      btn_size, None, (0, 0),
                                      preload.load_image(constants.THIRD_DIAMOND_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, n))
        elif c == 1:
            btn4 = widgets.PushButton(367, 380, {}, "", None, n,
                                      btn_size, None, (0, 0),
                                      preload.load_image(constants.ASTERISK_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, n))
        else:
            btn4 = widgets.PushButton(367, 380, {}, "", None, n,
                                      btn_size, None, (0, 0),
                                      preload.load_image(constants.ASTERISK0_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, n))

        btn5 = widgets.PushButton(480, 390, {}, "", None, n,
                                  btn_size, None, (0, 0),
                                  preload.load_image(constants.SHOP_DIAMOND_FILE_IMAGE_NAME,
                                                     constants.COLOR_KEY, n))

        coords = (300, 100), (445, 100), (375, 240), (475, 270)
        forefinger = advanced_sprites.ForeFinger(preload.load_image(constants.FOREFINGER_FILE_IMAGE_NAME,
                                                                    constants.COLOR_KEY,
                                                                    n), (0, 0))

        all_sprites.add(tiles_group, mapmenu, btn0, btn1, btn2, btn3, btn4, btn5, forefinger)
        cur = 7
        fing = False
        clock = pygame.time.Clock()
        ticks = 0
        while True:
            self.screen.fill(constants.BLACK_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 6
                    elif event.key == pygame.K_RETURN:
                        return cur
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if btn0.rect.collidepoint(event.pos):
                            return 6
                        elif btn2.rect.collidepoint(event.pos) and a != 2:
                            if cur == 7:
                                return 7
                            cur = 7
                        elif btn3.rect.collidepoint(event.pos) and b != 2:
                            if cur == 8:
                                return 8
                            cur = 8
                        elif btn4.rect.collidepoint(event.pos) and c != 2:
                            if cur == 9:
                                return 9
                            cur = 9
                        elif btn1.rect.collidepoint(event.pos):
                            return cur
                        elif btn5.rect.collidepoint(event.pos):
                            if cur == 10:
                                return 10
                            cur = 10
            all_sprites.draw(self.screen)
            ticks += clock.get_time()
            if ticks > constants.FOREFINGER_SHAKE_DELTA_TIME:
                forefinger.move(coords[cur - 7])
                forefinger.shake(fing)
                fing ^= 1
                ticks = 0
            clock.tick()
            pygame.display.flip()


class AngkorWatMiniMap(BasicWindow):
    def __init__(self) -> None:
        super(AngkorWatMiniMap, self).__init__()

    def run_angkor_wat(self) -> int:
        """
        :return: status (see window).
        """
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        bck = pygame.Surface(constants.WINDOW_SIZE)
        bck.fill(constants.ANGKOR_MAP_COLOR)
        stat_bar = pygame.sprite.Group()
        mini_player = pygame.sprite.GroupSingle()
        background = common_sprites.PrimarySprite(bck, (0, 0))
        n = 2
        upper_img = common_sprites.PrimarySprite(preload.load_image(constants.UPPER_ANGKOR_FILE_IMAGE_NAME,
                                                                    constants.COLOR_KEY, n), (0, 0))
        minimap = common_sprites.PrimarySprite(preload.load_image(constants.WOODEN_MAP_FILE_IMAGE_NAME,
                                                                  constants.COLOR_KEY, 2.5), (167, 180))
        minimap.image.blit(preload.load_image(constants.ANGKOR_WAT_POINTED_MAP, None, 2.5), (0, 0))
        n = 2
        back_btn = widgets.PushButton(570, 790, constants.GOLDEN_ALPHABET, "Seal/Store ",
                                      None, n, (300, 60), None, (0, 0),
                                      preload.load_image(constants.RETURN_BACK_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, n))
        acc_btn = widgets.PushButton(10, 790, constants.GOLDEN_ALPHABET, "Play ",
                                     None, n, (300, 60), None, (0, 0),
                                     preload.load_image(constants.ACCEPT_FILE_IMAGE_NAME,
                                                        constants.COLOR_KEY, n))
        widgets.PushButton(100, 700, constants.GOLDEN_ALPHABET, f"{self.lives}  ",
                           stat_bar, n + 2, (400, 80), None, (0, 0),
                           preload.load_image(constants.HEAD,
                                              None, 3))
        widgets.PushButton(500, 700, constants.GOLDEN_ALPHABET, f"{self.amount_of_diamonds}  ",
                           stat_bar, n + 2, (400, 80), None, (0, 0),
                           preload.load_image(constants.MAP_DIAMOND,
                                              None, 3))
        coords = [(235, 235), (330, 260), (430, 230)]
        advanced_sprites.MiniPlayer(preload.load_image(constants.MINI_PLAYER, None, 2.5),
                                    coords[0], mini_player)
        tiles_group.add(background, upper_img, minimap)
        all_sprites.add(tiles_group, back_btn, acc_btn)
        cur_i = 0
        while True:
            self.screen.fill(constants.BLACK_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 5, -1
                    elif event.key == pygame.K_RETURN:
                        return 11, cur_i
                    elif event.key == pygame.K_RIGHT:
                        if min(cur_i + 1, len(coords) - 1) <= self.available_levels:
                            cur_i = min(cur_i + 1, len(coords) - 1)
                    elif event.key == pygame.K_LEFT:
                        cur_i = max(0, cur_i - 1)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if acc_btn.rect.collidepoint(event.pos):
                            return 11, cur_i
                        elif back_btn.rect.collidepoint(event.pos):
                            return 5, -1
            all_sprites.draw(self.screen)
            stat_bar.draw(self.screen)
            mini_player.sprite.move(coords[cur_i])
            mini_player.draw(self.screen)
            pygame.display.flip()


class BavariaMiniMap(BasicWindow):
    def __init__(self) -> None:
        super(BavariaMiniMap, self).__init__()

    def run_bavaria(self) -> int:
        """
        :return: status (see window).
        """
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        bck = pygame.Surface(constants.WINDOW_SIZE)
        bck.fill(constants.BAVARIA_MAP_COLOR)
        background = common_sprites.PrimarySprite(bck, (0, 0))
        n = 2
        upper_img = common_sprites.PrimarySprite(preload.load_image(constants.UPPER_BAVARIA_FILE_IMAGE_NAME,
                                                                    constants.COLOR_KEY, n), (0, 0))
        minimap = common_sprites.PrimarySprite(preload.load_image(constants.WOODEN_MAP_FILE_IMAGE_NAME,
                                                                  constants.COLOR_KEY, 2.5), (167, 180))
        back_btn = widgets.PushButton(570, 790, constants.GOLDEN_ALPHABET, "Seal/Store ",
                                      None, 2, (300, 60), None, (0, 0),
                                      preload.load_image(constants.RETURN_BACK_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, 2))
        acc_btn = widgets.PushButton(10, 790, constants.GOLDEN_ALPHABET, "Play ",
                                     None, 2, (300, 60), None, (0, 0),
                                     preload.load_image(constants.ACCEPT_FILE_IMAGE_NAME,
                                                        constants.COLOR_KEY, 2))
        tiles_group.add(background, upper_img, minimap)
        all_sprites.add(tiles_group, back_btn, acc_btn)
        while True:
            self.screen.fill(constants.BLACK_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 4
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if acc_btn.rect.collidepoint(event.pos):
                            return 11
                        elif back_btn.rect.collidepoint(event.pos):
                            return 4
            all_sprites.draw(self.screen)
            pygame.display.flip()


class TibetMiniMap(BasicWindow):
    def __init__(self) -> None:
        super(TibetMiniMap, self).__init__()

    def run_tibet(self) -> int:
        """
        :return: status (see window).
        """
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        bck = pygame.Surface(constants.WINDOW_SIZE)
        bck.fill(constants.TIBET_MAP_COLOR)
        background = common_sprites.PrimarySprite(bck, (0, 0))
        upper_img = common_sprites.PrimarySprite(preload.load_image(constants.UPPER_TIBET_FILE_IMAGE_NAME,
                                                                    constants.COLOR_KEY, 3.32), (0, 0))
        minimap = common_sprites.PrimarySprite(preload.load_image(constants.WOODEN_MAP_FILE_IMAGE_NAME,
                                                                  constants.COLOR_KEY, 2.5), (167, 180))
        back_btn = widgets.PushButton(570, 790, constants.GOLDEN_ALPHABET, "Seal/Store ",
                                      None, 2, (300, 60), None, (0, 0),
                                      preload.load_image(constants.RETURN_BACK_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, 2))
        acc_btn = widgets.PushButton(10, 790, constants.GOLDEN_ALPHABET, "Play ",
                                     None, 2, (300, 60), None, (0, 0),
                                     preload.load_image(constants.ACCEPT_FILE_IMAGE_NAME,
                                                        constants.COLOR_KEY, 2))
        tiles_group.add(background, upper_img, minimap)
        all_sprites.add(tiles_group, back_btn, acc_btn)
        while True:
            self.screen.fill(constants.BLACK_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 4
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if acc_btn.rect.collidepoint(event.pos):
                            return 11
                        elif back_btn.rect.collidepoint(event.pos):
                            return 4
            all_sprites.draw(self.screen)
            pygame.display.flip()


class Shop(BasicWindow):
    def __init__(self) -> None:
        super(Shop, self).__init__()

    def run_shop(self) -> int:
        """
        :return: status (see window).
        """
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        text_group = pygame.sprite.Group()
        hp_group = pygame.sprite.GroupSingle()
        cost_group = pygame.sprite.GroupSingle()
        stat_group = pygame.sprite.GroupSingle()
        my_money = pygame.sprite.GroupSingle()
        grass = preload.load_image(constants.GRASS_BACKGROUND_FILE_IMAGE_NAME)
        for y in range(constants.WINDOW_HEIGHT_MEASURED_IN_TILES):
            for x in range(constants.WINDOW_WIDTH_MEASURED_IN_TILES):
                tiles_group.add(common_sprites.Tile(grass, (x, y)))
        back_btn = widgets.PushButton(670, 790, constants.GOLDEN_ALPHABET, "Back ",
                                      None, 2, (180, 60), None, (0, 0),
                                      preload.load_image(constants.RETURN_BACK_FILE_IMAGE_NAME,
                                                         constants.COLOR_KEY, 2))
        acc_btn = widgets.PushButton(10, 790, constants.GOLDEN_ALPHABET, "Buy ",
                                     None, 2, (300, 60), None, (0, 0),
                                     preload.load_image(constants.ACCEPT_FILE_IMAGE_NAME,
                                                        constants.COLOR_KEY, 2))
        text.String(270, 80, constants.GOLDEN_ALPHABET,
                    "STORE", text_group, 4, (300, 80))
        coords = (80, 125), (80, 175), (80, 225), (80, 275)
        n = 3
        btn1 = widgets.PushButton(200, 160, constants.GOLDEN_ALPHABET,
                                  "Chain vest", text_group, n, (300, 50))
        common_sprites.PrimarySprite(preload.load_image(constants.CHAIN_VEST_FILE_IMAGE_NAME,
                                                        constants.COLOR_KEY,
                                                        n), (120, 125), text_group)
        btn2 = widgets.PushButton(200, 210, constants.GOLDEN_ALPHABET,
                                  "Magical suit", text_group, n, (340, 50))
        common_sprites.PrimarySprite(preload.load_image(constants.MAGICAL_SUIT_FILE_IMAGE_NAME,
                                                        constants.COLOR_KEY,
                                                        n), (120, 175), text_group)
        btn3 = widgets.PushButton(200, 260, constants.GOLDEN_ALPHABET,
                                  "Mithril vest", text_group, n, (340, 50))
        common_sprites.PrimarySprite(preload.load_image(constants.MITHRIL_VEST_FILE_IMAGE_NAME,
                                                        constants.COLOR_KEY,
                                                        n), (120, 225), text_group)
        btn4 = widgets.PushButton(200, 310, constants.GOLDEN_ALPHABET,
                                  "Crystal jacket", text_group, n, (380, 50))
        common_sprites.PrimarySprite(preload.load_image(constants.CRYSTAL_JACKET_FILE_IMAGE_NAME,
                                                        constants.COLOR_KEY,
                                                        n), (120, 275), text_group)
        picker = common_sprites.PrimarySprite(
            pygame.transform.rotate(preload.load_image(constants.POINTER_FILE_IMAGE_NAME,
                                                       constants.COLOR_KEY,
                                                       n), 90), coords[0])
        cur = 0
        y1, y2 = 400, 450
        x = 120
        t1 = text.String(x, y1, constants.GOLDEN_ALPHABET,
                         f"Extra lives: {self.prices_and_hp[0][1]}", None, n, (800, 50))
        t2 = text.String(x, y2, constants.GOLDEN_ALPHABET,
                         f"Cost: {self.prices_and_hp[0][0]}", None, n, (800, 50))
        t3 = text.String(x, y1, constants.GOLDEN_ALPHABET,
                         f"Extra lives: {self.prices_and_hp[1][1]}", None, n, (800, 50))
        t4 = text.String(x, y2, constants.GOLDEN_ALPHABET,
                         f"Cost: {self.prices_and_hp[1][0]}", None, n, (800, 50))
        t5 = text.String(x, y1, constants.GOLDEN_ALPHABET,
                         f"Extra lives: {self.prices_and_hp[2][1]}", None, n, (800, 50))
        t6 = text.String(x, y2, constants.GOLDEN_ALPHABET,
                         f"Cost: {self.prices_and_hp[2][0]}", None, n, (800, 50))
        t7 = text.String(x, y1, constants.GOLDEN_ALPHABET,
                         f"Extra lives: {self.prices_and_hp[3][1]}", None, n, (800, 50))
        t8 = text.String(x, y2, constants.GOLDEN_ALPHABET,
                         f"Cost: {self.prices_and_hp[3][0]}", None, n, (800, 50))
        info = [(t1, t2), (t3, t4), (t5, t6), (t7, t8)]
        all_sprites.add(tiles_group, text_group, back_btn, acc_btn, picker)
        while True:
            self.screen.fill(constants.BLACK_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 5
                    elif event.key == pygame.K_RETURN:
                        self.buy(cur, stat_group)
                    elif event.key == pygame.K_DOWN:
                        cur = (cur + 1) % len(info)
                        stat_group.empty()
                    elif event.key == pygame.K_UP:
                        cur = (cur - 1) % len(info)
                        stat_group.empty()
                    picker.rect.topleft = coords[cur]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if acc_btn.rect.collidepoint(event.pos):
                            self.buy(cur, stat_group)
                        elif back_btn.rect.collidepoint(event.pos):
                            return 5
                        elif btn1.rect.collidepoint(event.pos):
                            if cur == 0:
                                self.buy(0, stat_group)
                            else:
                                cur = 0
                                stat_group.empty()
                        elif btn2.rect.collidepoint(event.pos):
                            if cur == 1:
                                self.buy(1, stat_group)
                            else:
                                cur = 1
                                stat_group.empty()
                        elif btn3.rect.collidepoint(event.pos):
                            if cur == 2:
                                self.buy(2, stat_group)
                            else:
                                cur = 2
                                stat_group.empty()
                        elif btn4.rect.collidepoint(event.pos):
                            if cur == 3:
                                self.buy(3, stat_group)
                            else:
                                cur = 3
                                stat_group.empty()
                        picker.rect.topleft = coords[cur]
            hp_group.add(info[cur][0])
            my_money.add(text.String(120, 600, constants.GOLDEN_ALPHABET,
                                     f"You have {self.amount_of_diamonds} diamonds",
                                     text_group, n, (800, 50)))
            cost_group.add(info[cur][1])
            all_sprites.draw(self.screen)
            hp_group.draw(self.screen)
            cost_group.draw(self.screen)
            stat_group.draw(self.screen)
            my_money.draw(self.screen)
            pygame.display.flip()

    def buy(self, i: int, group: pygame.sprite.GroupSingle) -> typing.Union[None, pygame.sprite.Sprite]:
        """

        :param i: item index.
        :param group: sprite group where to put the object.
        :return: sprite.
        """
        if self.amount_of_diamonds >= self.prices_and_hp[i][0]:
            self.amount_of_diamonds -= self.prices_and_hp[i][0]
            self.lives += self.prices_and_hp[i][1]
            saving_stat.save_stat(self.lives, self.amount_of_diamonds, self.available_levels)
            return None
        else:
            return text.String(140, 650, constants.GOLDEN_ALPHABET, "Not enough diamonds.", group, 3, (800, 50))
