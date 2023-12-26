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

        # while bitboard:

    def generate_castling_moves(self):
        if self.castle & self.king_side:
            self.generate_king_side_castling_moves()

        if self.castle & self.queen_side:
            self.generate_queen_side_castling_moves()

    def generate_king_side_castling_moves(self):
        king_side_squares = KING_SIDE_SQUARES[self.side]
        king_attacked_squares = KING_ATTACKED_SQUARES[self.side]

        if self.check_piece_in_the_way(king_side_squares):
            return

        if self.check_piece_under_attack(king_attacked_squares):
            return

        self.add_castling_move(self.king_side_source_square, self.king_side_target_square)

    def generate_queen_side_castling_moves(self):
        queen_side_squares = QUEEN_SIDE_SQUARES[self.side]
        queen_attacked_squares = QUEEN_ATTACKED_SQUARES[self.side]

        if self.check_piece_in_the_way(queen_side_squares):
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

    def check_piece_under_attack(self, squares):
        for square in squares:
            if Attacked.check_squares_attacked(self.app, square, self.side ^ 1):
                return True

        return False

    def check_piece_in_the_way(self, squares):
        for square in squares:
            if Bit.get_bit(self.occupancies[SIDES["all"]], square):
                return True

        return False
