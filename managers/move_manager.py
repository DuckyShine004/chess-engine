from src.routines.codec import Codec
from src.routines.attacked import Attacked

from src.utilities.bit import Bit

from src.constants.piece_constants import SIDES, PIECES, CASTLING_RIGHTS
from src.constants.board_constants import ALL_SIDES, SQUARES, MOVE_TYPES


class MoveManager:
    def __init__(self, app, manager):
        self.app = app
        self.manager = manager

    def set_attributes_to_parameters(self, parameters):
        self.source_square = parameters.source_square
        self.target_square = parameters.target_square
        self.piece = parameters.piece
        self.promotion_piece = parameters.promotion_piece
        self.capture_flag = parameters.capture_flag
        self.double_pawn_push_flag = parameters.double_pawn_push_flag
        self.enpassant_flag = parameters.enpassant_flag
        self.castling_flag = parameters.castling_flag

    def make_move(self, move, move_type):
        if move_type == MOVE_TYPES["all"]:
            return self.handle_king_under_check()
        else:
            if not Codec.get_decoded_capture_flag(move):
                return False

            self.make_move(move, move_type)

    def handle_king_under_check(self):
        self.manager.side ^= 1

        bitboard = None

        if self.manager.side == SIDES["white"]:
            bitboard = self.manager.bitboards[PIECES["k"]]
        else:
            bitboard = self.manager.bitboards[PIECES["K"]]

        square = Bit.get_least_significant_first_bit(bitboard)

        if Attacked.check_squares_attacked(self.app, square, self.manager.side):
            self.manager.set_attributes()
            return False

        return True
