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
            self.update_manager_and_parameters(move)

            self.handle_quiet_moves()
            self.handle_capture_moves()
            self.handle_pawn_promotion_moves()
            self.handle_enpassant_moves()
            self.handle_double_pawn_push_moves()

            return self.handle_king_under_check()
        else:
            if not Codec.get_decoded_capture_flag(move):
                return False

            self.make_move(move, move_type)

    def update_manager_and_parameters(self, move):
        self.manager.preserve_attributes()
        move_parameters = Codec.get_decoded_move_parameters(move)
        self.set_attributes_to_parameters(move_parameters)

    def handle_quiet_moves(self):
        self.remove_piece(self.source_square, self.piece)
        self.set_piece(self.target_square, self.piece)

    def handle_capture_moves(self):
        if not self.capture_flag:
            return

        a = PIECES["p"] if self.manager.side == SIDES["white"] else PIECES["P"]
        b = PIECES["k"] if self.manager.side == SIDES["white"] else PIECES["K"]

        for piece in range(a, b + 1):
            if not Bit.get_bit(self.manager.bitboards[piece], self.target_square):
                continue

            self.remove_piece(self.target_square, piece)
            break

    def handle_pawn_promotion_moves(self):
        if not self.promotion_piece:
            return

        piece = PIECES["P"] if self.manager.side == SIDES["white"] else PIECES["p"]

        self.remove_piece(self.target_square, piece)
        self.set_piece(self.target_square, self.promotion_piece)

    def handle_enpassant_moves(self):
        if not self.enpassant_flag:
            return

        piece = PIECES["p"] if self.manager.side == SIDES["white"] else PIECES["P"]
        offset = 8 if self.manager.side == SIDES["white"] else -8

        self.remove_piece(self.target_square + offset, piece)

        self.manager.enpassant = SQUARES["null"]

    def handle_double_pawn_push_moves(self):
        if not self.double_pawn_push_flag:
            return

        if self.manager.side == SIDES["white"]:
            self.manager.enpassant = self.target_square + 8
        else:
            self.manager.enpassant = self.target_square - 8

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

    def remove_piece(self, square, piece):
        bitboard = Bit.pop_bit(self.manager.bitboards[piece], square)
        self.manager.bitboards[piece] = bitboard

    def set_piece(self, square, piece):
        bitboard = Bit.set_bit(self.manager.bitboards[piece], square)
        self.manager.bitboards[piece] = bitboard
