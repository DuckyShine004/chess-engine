from src.utilities.bit import Bit

from src.constants.board_constants import ENCODED_ARGUMENT_VALUES


class Serlialize:
    @staticmethod
    def get_encoded_moves(source, target, piece, promoted, capture, double, enpassant, castling):
        encoded_value = 0

        for argument, value in ENCODED_ARGUMENT_VALUES.items():
            encoded_value
