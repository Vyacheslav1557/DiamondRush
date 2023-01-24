import os

PATH_TO_DATA = "data"

PATH_TO_TEXTURES = os.path.join(PATH_TO_DATA, "textures")
PATH_TO_MAPS = os.path.join(PATH_TO_DATA, "maps")
PATH_TO_STAT = os.path.join(PATH_TO_DATA, "statistics")


STAT_FILE_TXT_NAME = os.path.join(PATH_TO_STAT, "stat.txt")

PATH_TO_ANGKOR_WAT = os.path.join(PATH_TO_MAPS, "AngkorWat")

AW_STAGE1_FILE_NAME = os.path.join(PATH_TO_ANGKOR_WAT, "stage1.tmx")
AW_STAGE2_FILE_NAME = os.path.join(PATH_TO_ANGKOR_WAT, "stage2.tmx")
AW_STAGE3_FILE_NAME = os.path.join(PATH_TO_ANGKOR_WAT, "stage3.tmx")

MAPS = AW_STAGE1_FILE_NAME, AW_STAGE2_FILE_NAME, AW_STAGE3_FILE_NAME

PATH_TO_UI = os.path.join(PATH_TO_TEXTURES, "ui")
PATH_TO_FIRST_LOCATION = os.path.join(PATH_TO_TEXTURES, "0")
PATH_TO_SECOND_LOCATION = os.path.join(PATH_TO_TEXTURES, "1")
PATH_TO_THIRD_LOCATION = os.path.join(PATH_TO_TEXTURES, "2")
PATH_TO_MMV = os.path.join(PATH_TO_TEXTURES, "mmv")
PATH_TO_MS = os.path.join(PATH_TO_TEXTURES, "ms")
PATH_TO_PLAYER = os.path.join(PATH_TO_TEXTURES, "player")
PATH_TO_CM = os.path.join(PATH_TO_TEXTURES, "cm")

PATH_TO_MAP_ELEMENTS = os.path.join(PATH_TO_MS, "map_elements")

ANGKOR_WAT_POINTED_MAP = os.path.join(PATH_TO_MAP_ELEMENTS, "angkor_wat_points.png")
MINI_PLAYER = os.path.join(PATH_TO_MAP_ELEMENTS, "mini_player.png")
MAP_DIAMOND = os.path.join(PATH_TO_MAP_ELEMENTS, "ms.f-0-Image-Sec-0-1110.png")
HEAD = os.path.join(PATH_TO_MAP_ELEMENTS, "ms.f-0-Image-Sec-0-1111.png")

PATH_TO_SCORE_BOARD = os.path.join(PATH_TO_UI, "upper_helping_score")
SCORE_BOARD_FILE_IMAGE_NAME = os.path.join(PATH_TO_SCORE_BOARD, "score_board2.png")

PATH_TO_DIAMONDS = os.path.join(PATH_TO_CM, "diamonds")
PATH_TO_LOCK = os.path.join(PATH_TO_CM, "lock")

LOCKED_LOCK_IMAGE_NAME = os.path.join(PATH_TO_LOCK, "locked_lock.png")
UNLOCKED_LOCK_IMAGE_NAME = os.path.join(PATH_TO_LOCK, "unlocked_lock.png")

PATH_TO_PURPLE_DIAMOND = os.path.join(PATH_TO_DIAMONDS, "purple")
PATH_TO_ORANGE_DIAMOND = os.path.join(PATH_TO_DIAMONDS, "orange")

PURPLE_DIAMOND_IMAGE_NAMES = [os.path.join(PATH_TO_PURPLE_DIAMOND, f"cm.f-2-Image-Sec-0-{i}.png") for i in
                              range(280, 284)]
ORANGE_DIAMOND_IMAGE_NAMES = [os.path.join(PATH_TO_ORANGE_DIAMOND, f"cm.f-2-Image-Sec-1-{i}.png") for i in
                              range(284, 288)]

PATH_TO_ROCKS = os.path.join(PATH_TO_FIRST_LOCATION, "rock")
PATH_TO_LEAVES = os.path.join(PATH_TO_FIRST_LOCATION, "leaf")

ROCKS_IMAGE_NAMES = [os.path.join(PATH_TO_ROCKS, f"0.f-0-Image-Sec-0-{i}.png") for i in range(1, 9)]
LEAVES_IMAGE_NAMES = [os.path.join(PATH_TO_LEAVES, f"0.f-1-Image-Sec-0-{i}.png") for i in range(9, 13)]



PATH_TO_DRAG = os.path.join(PATH_TO_PLAYER, "drag")
PATH_TO_HIT = os.path.join(PATH_TO_PLAYER, "hit")
PATH_TO_MOVING = os.path.join(PATH_TO_PLAYER, "moving")
PATH_TO_SHOT = os.path.join(PATH_TO_PLAYER, "shot")
PATH_TO_STAYING = os.path.join(PATH_TO_PLAYER, "staying")
PATH_TO_CLIMBING_UP = os.path.join(PATH_TO_PLAYER, "climbing_up")
PATH_TO_CLIMBING_RIGHT = os.path.join(PATH_TO_PLAYER, "climbing_right")
PATH_TO_DYING_UNDER_ROCK = os.path.join(PATH_TO_PLAYER, "dying_under_rock")

HIT_IMAGE_NAMES = [os.path.join(PATH_TO_HIT, f"IMG_20220501_203734 ({i}).png") for i in range(13, 19)]
DRAG_IMAGE_NAMES = [os.path.join(PATH_TO_DRAG, f"IMG_20220501_203734 ({i}).png") for i in range(23, 26)]
MOVING_IMAGE_NAMES = [os.path.join(PATH_TO_MOVING, f"IMG_20220501_203734 ({i}).png") for i in range(9, 13)]
SHOT_IMAGE_NAMES = [os.path.join(PATH_TO_SHOT, f"IMG_20220501_203734 ({i}).png") for i in range(19, 23)]
STAYING_IMAGE_NAMES = [os.path.join(PATH_TO_STAYING, f"IMG_20220501_203734 ({i}).png") for i in range(1, 9)]
CLIMBING_UP_IMAGE_NAMES = [os.path.join(PATH_TO_CLIMBING_UP, f"cl{i}.png") for i in range(1, 7)]
CLIMBING_RIGHT_IMAGE_NAMES = [os.path.join(PATH_TO_CLIMBING_RIGHT, f"cl_right{i}.png") for i in range(1, 5)]
DYING_UNDER_ROCK_IMAGE_NAMES = [os.path.join(PATH_TO_DYING_UNDER_ROCK, f"dur{i}.png") for i in range(1, 4)]

PATH_TO_STARTING_LOGO = os.path.join(PATH_TO_UI, "starting_logo")
PATH_TO_BRICKS_BACKGROUND = os.path.join(PATH_TO_SECOND_LOCATION, "bricks_font")

PATH_TO_GRASS_FONT = os.path.join(PATH_TO_FIRST_LOCATION, "grass_font")
GRASS_BACKGROUND_FILE_IMAGE_NAME = os.path.join(PATH_TO_GRASS_FONT, "0.f-3-Image-Sec-0-52.png")

STARTING_LOGO_FILE_IMAGE_NAME = os.path.join(PATH_TO_STARTING_LOGO, "778ec54d2f104e8a8e625928cbcba42f.png")
BRICKS_BACKGROUND_FILE_IMAGE_NAME = os.path.join(PATH_TO_BRICKS_BACKGROUND, "1.f-3-Image-Sec-0-117.png")

PATH_TO_MAIN_MAP = os.path.join(PATH_TO_MMV, "main_map")
PATH_TO_DIAMONDS_OF_COMPLETING = os.path.join(PATH_TO_MMV, "diamonds_of_completing")
PATH_TO_SHOP = os.path.join(PATH_TO_MMV, "shop")

CHAIN_VEST_FILE_IMAGE_NAME = os.path.join(PATH_TO_SHOP, "chain_vest.png")
CRYSTAL_JACKET_FILE_IMAGE_NAME = os.path.join(PATH_TO_SHOP, "crystal_jacket.png")
MAGICAL_SUIT_FILE_IMAGE_NAME = os.path.join(PATH_TO_SHOP, "magical_suit.png")
MITHRIL_VEST_FILE_IMAGE_NAME = os.path.join(PATH_TO_SHOP, "mithril_vest.png")

PATH_TO_WOODEN_MAP = os.path.join(PATH_TO_MS, "wooden_map")
PATH_TO_UPPER_IMAGES = os.path.join(PATH_TO_MS, "upper_images")

UPPER_ANGKOR_FILE_IMAGE_NAME = os.path.join(PATH_TO_UPPER_IMAGES, "upper_angkor.png")
UPPER_BAVARIA_FILE_IMAGE_NAME = os.path.join(PATH_TO_UPPER_IMAGES, "upper_bavaria.png")
UPPER_TIBET_FILE_IMAGE_NAME = os.path.join(PATH_TO_UPPER_IMAGES, "upper_tibet.png")
WOODEN_MAP_FILE_IMAGE_NAME = os.path.join(PATH_TO_WOODEN_MAP, "wooden_map.png")

PATH_TO_UPPER_HELPING_SCORE = os.path.join(PATH_TO_UI, "upper_helping_score")

POINTER_FILE_IMAGE_NAME = os.path.join(PATH_TO_UPPER_HELPING_SCORE, "ui.f-2-Image-Sec-0-2211.png")

ASTERISK_FILE_IMAGE_NAME = os.path.join(PATH_TO_MAIN_MAP, "asterisk.png")
ASTERISK0_FILE_IMAGE_NAME = os.path.join(PATH_TO_MAIN_MAP, "asterisk0.png")
FIRE_FILE_IMAGE_NAME = os.path.join(PATH_TO_MAIN_MAP, "fire.png")
FIRE0_FILE_IMAGE_NAME = os.path.join(PATH_TO_MAIN_MAP, "fire0.png")
HELMET_FILE_IMAGE_NAME = os.path.join(PATH_TO_MAIN_MAP, "helmet.png")
HELMET0_FILE_IMAGE_NAME = os.path.join(PATH_TO_MAIN_MAP, "helmet0.png")
MAP_MENU_FILE_IMAGE_NAME = os.path.join(PATH_TO_MAIN_MAP, "mapmenu.png")
FIRST_DIAMOND_FILE_IMAGE_NAME = os.path.join(PATH_TO_DIAMONDS_OF_COMPLETING, "mmv.f-3-Image-Sec-0-1082.png")
SECOND_DIAMOND_FILE_IMAGE_NAME = os.path.join(PATH_TO_DIAMONDS_OF_COMPLETING, "mmv.f-2-Image-Sec-0-1081.png")
THIRD_DIAMOND_FILE_IMAGE_NAME = os.path.join(PATH_TO_DIAMONDS_OF_COMPLETING, "mmv.f-1-Image-Sec-0-1080.png")
SHOP_DIAMOND_FILE_IMAGE_NAME = os.path.join(PATH_TO_MAIN_MAP, "ms.f-0-Image-Sec-0-1110.png")
FOREFINGER_FILE_IMAGE_NAME = os.path.join(PATH_TO_MAIN_MAP, "forefinger.png")

PATH_TO_GOLDEN_SYMBOLS = os.path.join(PATH_TO_UI, "golden_symbols")
PATH_TO_GREEN_SYMBOLS = os.path.join(PATH_TO_UI, "green_symbols")
PATH_TO_ORANGE_SYMBOLS = os.path.join(PATH_TO_UI, "orange_symbols")
PATH_TO_ORIENTATION_HELP = os.path.join(PATH_TO_UI, "orientation_help")

GOLDEN_SPACE_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1931.png")
GOLDEN_EXCLAMATION_MARK_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1932.png")
GOLDEN_APOSTROPHE_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1933.png")
GOLDEN_COMMA_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1934.png")
GOLDEN_DASH_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1935.png")
GOLDEN_DOT_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1936.png")
GOLDEN_SLASH_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1937.png")
GOLDEN_0_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1938.png")
GOLDEN_1_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1939.png")
GOLDEN_2_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1940.png")
GOLDEN_3_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1941.png")
GOLDEN_4_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1942.png")
GOLDEN_5_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1943.png")
GOLDEN_6_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1944.png")
GOLDEN_7_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1945.png")
GOLDEN_8_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1946.png")
GOLDEN_9_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1947.png")
GOLDEN_QUESTION_MARK_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1948.png")
GOLDEN_AT_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1949.png")
GOLDEN_A_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1950.png")
GOLDEN_B_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1951.png")
GOLDEN_C_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1952.png")
GOLDEN_D_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1953.png")
GOLDEN_E_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1954.png")
GOLDEN_F_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1955.png")
GOLDEN_G_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1956.png")
GOLDEN_H_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1957.png")
GOLDEN_I_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1958.png")
GOLDEN_J_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1959.png")
GOLDEN_K_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1960.png")
GOLDEN_L_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1961.png")
GOLDEN_M_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1962.png")
GOLDEN_N_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1963.png")
GOLDEN_O_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1964.png")
GOLDEN_P_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1965.png")
GOLDEN_Q_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1966.png")
GOLDEN_R_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1967.png")
GOLDEN_S_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1968.png")
GOLDEN_T_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1969.png")
GOLDEN_U_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1970.png")
GOLDEN_V_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1971.png")
GOLDEN_W_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1972.png")
GOLDEN_X_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1973.png")
GOLDEN_Y_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1974.png")
GOLDEN_Z_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1975.png")
GOLDEN_LOWER_A_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1976.png")
GOLDEN_LOWER_B_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1977.png")
GOLDEN_LOWER_C_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1978.png")
GOLDEN_LOWER_D_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1979.png")
GOLDEN_LOWER_E_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1980.png")
GOLDEN_LOWER_F_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1981.png")
GOLDEN_LOWER_G_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1982.png")
GOLDEN_LOWER_H_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1983.png")
GOLDEN_LOWER_I_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1984.png")
GOLDEN_LOWER_J_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1985.png")
GOLDEN_LOWER_K_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1986.png")
GOLDEN_LOWER_L_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1987.png")
GOLDEN_LOWER_M_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1988.png")
GOLDEN_LOWER_N_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1989.png")
GOLDEN_LOWER_O_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1990.png")
GOLDEN_LOWER_P_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1991.png")
GOLDEN_LOWER_Q_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1992.png")
GOLDEN_LOWER_R_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1993.png")
GOLDEN_LOWER_S_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1994.png")
GOLDEN_LOWER_T_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1995.png")
GOLDEN_LOWER_U_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1996.png")
GOLDEN_LOWER_V_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1997.png")
GOLDEN_LOWER_W_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1998.png")
GOLDEN_LOWER_X_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-1999.png")
GOLDEN_LOWER_Y_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2000.png")
GOLDEN_LOWER_Z_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2001.png")
GOLDEN_ASTERISK_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2002.png")
_2 = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2003.png")
_3 = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2004.png")
_4 = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2005.png")
GOLDEN_COLON_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2006.png")
_5 = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2007.png")
_6 = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2008.png")
_7 = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2009.png")
_8 = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2010.png")
_9 = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2011.png")
GOLDEN_OPENING_ROUNDED_BRACKET_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2012.png")
GOLDEN_CLOSING_ROUNDED_BRACKET_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2013.png")
GOLDEN_OPENING_SQUARE_BRACKET_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2015.png")
GOLDEN_CLOSING_SQUARE_BRACKET_FILE_IMAGE_NAME = os.path.join(PATH_TO_GOLDEN_SYMBOLS, "ui.f-1-Image-Sec-0-2014.png")

RETURN_BACK_FILE_IMAGE_NAME = os.path.join(PATH_TO_ORIENTATION_HELP, "ui.f-3-Image-Sec-0-2216.png")
ACCEPT_FILE_IMAGE_NAME = os.path.join(PATH_TO_ORIENTATION_HELP, "ui.f-3-Image-Sec-0-2217.png")

GOLDEN_ALPHABET = {
    "!": GOLDEN_EXCLAMATION_MARK_FILE_IMAGE_NAME,
    "?": GOLDEN_QUESTION_MARK_FILE_IMAGE_NAME,
    "'": GOLDEN_APOSTROPHE_FILE_IMAGE_NAME,
    ",": GOLDEN_COMMA_FILE_IMAGE_NAME,
    "-": GOLDEN_DASH_FILE_IMAGE_NAME,
    ".": GOLDEN_DOT_FILE_IMAGE_NAME,
    "/": GOLDEN_SLASH_FILE_IMAGE_NAME,
    "0": GOLDEN_0_FILE_IMAGE_NAME,
    "1": GOLDEN_1_FILE_IMAGE_NAME,
    "2": GOLDEN_2_FILE_IMAGE_NAME,
    "3": GOLDEN_3_FILE_IMAGE_NAME,
    "4": GOLDEN_4_FILE_IMAGE_NAME,
    "5": GOLDEN_5_FILE_IMAGE_NAME,
    "6": GOLDEN_6_FILE_IMAGE_NAME,
    "7": GOLDEN_7_FILE_IMAGE_NAME,
    "8": GOLDEN_8_FILE_IMAGE_NAME,
    "9": GOLDEN_9_FILE_IMAGE_NAME,
    "A": GOLDEN_A_FILE_IMAGE_NAME,
    "B": GOLDEN_B_FILE_IMAGE_NAME,
    "C": GOLDEN_C_FILE_IMAGE_NAME,
    "D": GOLDEN_D_FILE_IMAGE_NAME,
    "E": GOLDEN_E_FILE_IMAGE_NAME,
    "F": GOLDEN_F_FILE_IMAGE_NAME,
    "G": GOLDEN_G_FILE_IMAGE_NAME,
    "H": GOLDEN_H_FILE_IMAGE_NAME,
    "I": GOLDEN_I_FILE_IMAGE_NAME,
    "J": GOLDEN_J_FILE_IMAGE_NAME,
    "K": GOLDEN_K_FILE_IMAGE_NAME,
    "L": GOLDEN_L_FILE_IMAGE_NAME,
    "M": GOLDEN_M_FILE_IMAGE_NAME,
    "N": GOLDEN_N_FILE_IMAGE_NAME,
    "O": GOLDEN_O_FILE_IMAGE_NAME,
    "P": GOLDEN_P_FILE_IMAGE_NAME,
    "Q": GOLDEN_Q_FILE_IMAGE_NAME,
    "R": GOLDEN_R_FILE_IMAGE_NAME,
    "S": GOLDEN_S_FILE_IMAGE_NAME,
    "T": GOLDEN_T_FILE_IMAGE_NAME,
    "U": GOLDEN_U_FILE_IMAGE_NAME,
    "V": GOLDEN_V_FILE_IMAGE_NAME,
    "W": GOLDEN_W_FILE_IMAGE_NAME,
    "X": GOLDEN_X_FILE_IMAGE_NAME,
    "Y": GOLDEN_Y_FILE_IMAGE_NAME,
    "Z": GOLDEN_Z_FILE_IMAGE_NAME,
    "a": GOLDEN_LOWER_A_FILE_IMAGE_NAME,
    "b": GOLDEN_LOWER_B_FILE_IMAGE_NAME,
    "c": GOLDEN_LOWER_C_FILE_IMAGE_NAME,
    "d": GOLDEN_LOWER_D_FILE_IMAGE_NAME,
    "e": GOLDEN_LOWER_E_FILE_IMAGE_NAME,
    "f": GOLDEN_LOWER_F_FILE_IMAGE_NAME,
    "g": GOLDEN_LOWER_G_FILE_IMAGE_NAME,
    "h": GOLDEN_LOWER_H_FILE_IMAGE_NAME,
    "i": GOLDEN_LOWER_I_FILE_IMAGE_NAME,
    "j": GOLDEN_LOWER_J_FILE_IMAGE_NAME,
    "k": GOLDEN_LOWER_K_FILE_IMAGE_NAME,
    "l": GOLDEN_LOWER_L_FILE_IMAGE_NAME,
    "m": GOLDEN_LOWER_M_FILE_IMAGE_NAME,
    "n": GOLDEN_LOWER_N_FILE_IMAGE_NAME,
    "o": GOLDEN_LOWER_O_FILE_IMAGE_NAME,
    "p": GOLDEN_LOWER_P_FILE_IMAGE_NAME,
    "q": GOLDEN_LOWER_Q_FILE_IMAGE_NAME,
    "r": GOLDEN_LOWER_R_FILE_IMAGE_NAME,
    "s": GOLDEN_LOWER_S_FILE_IMAGE_NAME,
    "t": GOLDEN_LOWER_T_FILE_IMAGE_NAME,
    "u": GOLDEN_LOWER_U_FILE_IMAGE_NAME,
    "v": GOLDEN_LOWER_V_FILE_IMAGE_NAME,
    "w": GOLDEN_LOWER_W_FILE_IMAGE_NAME,
    "x": GOLDEN_LOWER_X_FILE_IMAGE_NAME,
    "y": GOLDEN_LOWER_Y_FILE_IMAGE_NAME,
    "z": GOLDEN_LOWER_Z_FILE_IMAGE_NAME,
    " ": GOLDEN_SPACE_FILE_IMAGE_NAME,
    ":": GOLDEN_COLON_FILE_IMAGE_NAME,
    "*": GOLDEN_ASTERISK_FILE_IMAGE_NAME,
    "(": GOLDEN_OPENING_ROUNDED_BRACKET_FILE_IMAGE_NAME,
    ")": GOLDEN_CLOSING_ROUNDED_BRACKET_FILE_IMAGE_NAME,
    "[": GOLDEN_OPENING_SQUARE_BRACKET_FILE_IMAGE_NAME,
    "]": GOLDEN_CLOSING_SQUARE_BRACKET_FILE_IMAGE_NAME
}
