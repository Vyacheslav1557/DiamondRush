import constants
import typing
import os


def save_stat(lives: int, diamonds: int, available_levels: int) -> None:
    """
    Saves current values to a file.

    :param lives: amount of lives.
    :param diamonds: amount_of_diamonds.
    :param available_levels: amount of available levels.
    """
    with open(constants.STAT_FILE_TXT_NAME, "w", encoding="utf-8") as file:
        file.write(f"{lives} {diamonds} {available_levels}")


def get_stat() -> typing.Tuple[int, int, int]:
    """
    Reads values from a file.

    :return: read values.
    """
    if not os.path.exists(constants.STAT_FILE_TXT_NAME):
        open(constants.STAT_FILE_TXT_NAME, 'w').close()
        return 0, 0, 0
    with open(constants.STAT_FILE_TXT_NAME, "r+", encoding="utf-8") as file:
        inp = file.read().split()
        if not inp:
            return 0, 0, 0
        return int(inp[0]), int(inp[1]), int(inp[2])
