from src.utilities.bit import Bit

from src.constants.bit_constants import SOURCE_SQUARE_OFFSET
from src.constants.board_constants import ENCODED_ARGUMENT_VALUES


class Serlialize:
    @staticmethod
    def get_encoded_moves(**parameters: int):
        encoded_value = 0

        for argument, value in ENCODED_ARGUMENT_VALUES.items():
            encoded_value |= Bit.left_shift(parameters[argument], value)

        return encoded_value

    @staticmethod
    def get_source_square(move):
        return move & SOURCE_SQUARE_OFFSET
