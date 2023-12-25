from src.data.parameters.move_parameters import MoveParameters

from src.utilities.bit import Bit

from src.constants.file_constants import DESERIALIZER_METHODS
from src.constants.board_constants import MOVE_OFFSETS

from src.constants.bit_constants import (
    SOURCE_SQUARE_OFFSET,
    TARGET_SQUARE_OFFSET,
    PIECE_OFFSET,
    PROMOTED_PIECE_OFFSET,
    CAPTURE_FLAG_OFFSET,
    DOUBLE_PAWN_PUSH_FLAG,
    ENPASSANT_FLAG,
    CASTLING_FLAG,
)


class Codec:
    @staticmethod
    def get_encoded_move(parameters):
        encoded_value = 0

        for key, offset in MOVE_OFFSETS.items():
            value = getattr(parameters, key)
            encoded_value |= Bit.left_shift(value, offset)

        return encoded_value

    @staticmethod
    def get_decoded_move_parameters(move):
        arguments = []

        for method_name in DESERIALIZER_METHODS:
            method = getattr(Codec, method_name)
            arguments.append(method(move))

        return MoveParameters(*arguments)

    @staticmethod
    def get_decoded_source_square(move):
        return move & SOURCE_SQUARE_OFFSET

    @staticmethod
    def get_decoded_target_square(move):
        return Bit.right_shift((move & TARGET_SQUARE_OFFSET), 6)

    @staticmethod
    def get_decoded_piece(move):
        return Bit.right_shift((move & PIECE_OFFSET), 12)

    @staticmethod
    def get_decoded_promoted_piece(move):
        return Bit.right_shift((move & PROMOTED_PIECE_OFFSET), 16)

    @staticmethod
    def get_decoded_capture_flag(move):
        return bool(move & CAPTURE_FLAG_OFFSET)

    @staticmethod
    def get_decoded_double_pawn_push_flag(move):
        return bool(move & DOUBLE_PAWN_PUSH_FLAG)

    @staticmethod
    def get_decoded_enpassant_flag(move):
        return bool(move & ENPASSANT_FLAG)

    @staticmethod
    def get_decoded_castling_flag(move):
        return bool(move & CASTLING_FLAG)
