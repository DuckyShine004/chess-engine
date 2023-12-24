from src.utilities.bit import Bit

from src.constants.bit_constants import SOURCE_SQUARE_OFFSET
from src.constants.board_constants import MOVE_OFFSETS


class Serialize:
    @staticmethod
    def get_encoded_move(parameters):
        encoded_value = 0

        for key, offset in MOVE_OFFSETS.items():
            value = getattr(parameters, key)
            encoded_value |= Bit.left_shift(value, offset)

        return encoded_value

    @staticmethod
    def get_encoded_source_square(move):
        return move & SOURCE_SQUARE_OFFSET
