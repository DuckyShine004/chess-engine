from src.generator.pieces.piece import Piece

from src.routines.attacked import Attacked

from src.utilities.bit import Bit
from src.utilities.attack import Attack

from src.constants.board_constants import SQUARES

from src.constants.piece_constants import (
    SIDES,
    PIECES,
    CASTLE,
    KING_SIDE_SQUARES,
    QUEEN_SIDE_SQUARES,
    KING_ATTACKED_SQUARES,
    QUEEN_ATTACKED_SQUARES,
)


class King(Piece):
    def __init__(self, move_generator, app):
        super().__init__(move_generator, app)

        self.king_side = CASTLE["K"] if self.side == SIDES["white"] else CASTLE["k"]
        self.king_side_source_square = SQUARES["e1"] if self.side == SIDES["white"] else SQUARES["e8"]
        self.king_side_target_square = SQUARES["g1"] if self.side == SIDES["white"] else SQUARES["g8"]

        self.queen_side = CASTLE["Q"] if self.side == SIDES["white"] else CASTLE["q"]
        self.queen_side_source_square = SQUARES["e1"] if self.side == SIDES["white"] else SQUARES["e8"]
        self.queen_side_target_square = SQUARES["c1"] if self.side == SIDES["white"] else SQUARES["c8"]

    def generate_moves(self, bitboard):
        self.generate_castling_moves()

        while bitboard:
            source_square = Bit.get_least_significant_first_bit(bitboard)

            self.move_parameters.source_square = source_square

            self.generate_capture_moves(source_square)

            bitboard = Bit.pop_bit(bitboard, source_square)

    def generate_capture_moves(self, source_square):
        offset = ~self.occupancies[self.side]
        attacks = self.king_attack_table[source_square] & offset

        while attacks:
            target_square = Bit.get_least_significant_first_bit(attacks)

            self.move_parameters.target_square = target_square

            if self.check_piece_in_the_way(target_square):
                self.add_capture_move()
            else:
                self.add_quiet_move()

            attacks = Bit.pop_bit(attacks, target_square)

    def generate_castling_moves(self):
        if self.castle & self.king_side:
            self.generate_king_side_castling_moves()

        if self.castle & self.queen_side:
            self.generate_queen_side_castling_moves()

    def generate_king_side_castling_moves(self):
        king_side_squares = KING_SIDE_SQUARES[self.side]
        king_attacked_squares = KING_ATTACKED_SQUARES[self.side]

        if self.check_pieces_in_between_rook_and_king(king_side_squares):
            return

        if self.check_piece_under_attack(king_attacked_squares):
            return

        self.add_castling_move(self.king_side_source_square, self.king_side_target_square)

    def generate_queen_side_castling_moves(self):
        queen_side_squares = QUEEN_SIDE_SQUARES[self.side]
        queen_attacked_squares = QUEEN_ATTACKED_SQUARES[self.side]

        if self.check_pieces_in_between_rook_and_king(queen_side_squares):
            return

        if self.check_piece_under_attack(queen_attacked_squares):
            return

        self.add_castling_move(self.queen_side_source_square, self.queen_side_target_square)

    def add_castling_move(self, source_square, target_square):
        self.move_parameters.source_square = source_square
        self.move_parameters.target_square = target_square
        self.move_parameters.castling_flag = 1

        self.add_move()
        self.reset_move_parameters()

    def add_capture_move(self):
        self.move_parameters.capture_flag = 1

        self.add_move()
        self.reset_move_parameters()

    def add_quiet_move(self):
        self.add_move()

    def check_piece_in_the_way(self, target_square):
        return Bit.get_bit(self.occupancies[self.side ^ 1], target_square)

    def check_piece_under_attack(self, squares):
        for square in squares:
            if Attacked.check_squares_attacked(self.app, square, self.side ^ 1):
                return True

        return False

    def check_pieces_in_between_rook_and_king(self, squares):
        for square in squares:
            if Bit.get_bit(self.occupancies[SIDES["all"]], square):
                return True

        return False
