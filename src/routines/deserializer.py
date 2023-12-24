from src.utilities.bit import Bit

from src.constants.bit_constants import (
    SOURCE_SQUARE_OFFSET,
    TARGET_SQUARE_OFFSET,
    PIECE_OFFSET,
    PROMOTED_PIECE_OFFSET,
)


class Deserializer:
    @staticmethod
    def get_decoded_source_square(move):
        return move & SOURCE_SQUARE_OFFSET

    @staticmethod
    def get_decoded_target_square(move):
        return Bit.right_shift((move & TARGET_SQUARE_OFFSET), 6)
