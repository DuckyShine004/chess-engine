from src.generator.pieces.piece import Piece

from src.utilities.bit import Bit

from src.constants.piece_constants import SIDES, PIECES
from src.constants.board_constants import SQUARES


class Pawn(Piece):
    def __init__(self, move_generator, app):
        super().__init__(move_generator, app)

        self.offset = -8 if self.side == SIDES["white"] else 8

    def generate_moves(self, bitboard):
        while bitboard:
            source_square = Bit.get_least_significant_first_bit(bitboard)
            target_square = source_square + self.offset

            self.move_parameters.source_square = source_square
            self.move_parameters.target_square = target_square

            self.generate_promotion_moves(source_square, target_square)
            self.generate_capture_moves(source_square)
            self.generate_enpassant_moves(source_square)

            bitboard = Bit.pop_bit(bitboard, source_square)

    def generate_promotion_moves(self, source_square, target_square):
        if self.side == SIDES["white"] and target_square < SQUARES["a8"]:
            return

        if self.side == SIDES["black"] and target_square > SQUARES["h1"]:
            return

        if Bit.get_bit(self.occupancies[SIDES["all"]], target_square):
            return

        file_a = SQUARES["a7"] if self.side == SIDES["white"] else SQUARES["a2"]
        file_b = SQUARES["h7"] if self.side == SIDES["white"] else SQUARES["h2"]

        queen_ascii_piece = PIECES["Q"] if self.side == SIDES["white"] else PIECES["q"]
        rook_ascii_piece = PIECES["R"] if self.side == SIDES["white"] else PIECES["r"]
        bishop_ascii_piece = PIECES["B"] if self.side == SIDES["white"] else PIECES["b"]
        knight_ascii_piece = PIECES["N"] if self.side == SIDES["white"] else PIECES["n"]

        if file_a <= source_square <= file_b:
            self.add_promotion_move(queen_ascii_piece)
            self.add_promotion_move(rook_ascii_piece)
            self.add_promotion_move(bishop_ascii_piece)
            self.add_promotion_move(knight_ascii_piece)
        else:
            self.add_single_push_move()
            self.add_double_push_move(source_square, target_square)

    def generate_promotion_capture_moves(self, source_square):
        file_a = SQUARES["a7"] if self.side == SIDES["white"] else SQUARES["a2"]
        file_b = SQUARES["h7"] if self.side == SIDES["white"] else SQUARES["h2"]

        queen_ascii_piece = PIECES["Q"] if self.side == SIDES["white"] else PIECES["q"]
        rook_ascii_piece = PIECES["R"] if self.side == SIDES["white"] else PIECES["r"]
        bishop_ascii_piece = PIECES["B"] if self.side == SIDES["white"] else PIECES["b"]
        knight_ascii_piece = PIECES["N"] if self.side == SIDES["white"] else PIECES["n"]

        if file_a <= source_square <= file_b:
            self.add_promotion_capture_move(queen_ascii_piece)
            self.add_promotion_capture_move(rook_ascii_piece)
            self.add_promotion_capture_move(bishop_ascii_piece)
            self.add_promotion_capture_move(knight_ascii_piece)
        else:
            self.add_capture_move()

    def generate_capture_moves(self, source_square):
        attacks = self.pawn_attack_table[self.side][source_square] & self.occupancies[self.side ^ 1]

        while attacks:
            target_square = Bit.get_least_significant_first_bit(attacks)

            self.move_parameters.target_square = target_square

            self.generate_promotion_capture_moves(source_square)

            attacks = Bit.pop_bit(attacks, target_square)

    def generate_enpassant_moves(self, source_square):
        if self.enpassant == SQUARES["null"]:
            return

        offset = Bit.left_shift(1, self.enpassant)
        enpassant_attacks = self.pawn_attack_table[self.side][source_square] & offset

        if not enpassant_attacks:
            return

        enpassant_square = Bit.get_least_significant_first_bit(enpassant_attacks)

        self.add_enpassant_move(enpassant_square)

    def add_single_push_move(self):
        self.add_move()

    def add_double_push_move(self, source_square, target_square):
        file_a = SQUARES["a2"] if self.side == SIDES["white"] else SQUARES["a7"]
        file_b = SQUARES["h2"] if self.side == SIDES["white"] else SQUARES["h7"]

        if not file_a <= source_square <= file_b:
            return

        if Bit.get_bit(self.occupancies[SIDES["all"]], target_square + self.offset):
            return

        self.move_parameters.target_square = target_square + self.offset
        self.move_parameters.double_pawn_push_flag = 1

        self.add_move()
        self.reset_move_parameters()

    def add_capture_move(self):
        self.move_parameters.capture_flag = 1

        self.add_move()
        self.reset_move_parameters()

    def add_promotion_move(self, promotion_piece):
        self.move_parameters.promotion_piece = promotion_piece

        self.add_move()
        self.reset_move_parameters()

    def add_promotion_capture_move(self, promotion_piece):
        self.move_parameters.promotion_piece = promotion_piece
        self.move_parameters.capture_flag = 1

        self.add_move()
        self.reset_move_parameters()

    def add_enpassant_move(self, enpassant_square):
        self.move_parameters.target_square = enpassant_square
        self.move_parameters.capture_flag = 1
        self.move_parameters.enpassant_flag = 1

        self.add_move()
        self.reset_move_parameters()
