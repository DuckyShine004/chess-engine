from src.generator.pieces.piece import Piece

from src.utilities.bit import Bit


class Knight(Piece):
    def __init__(self, move_generator, app):
        super().__init__(move_generator, app)

    def generate_moves(self, bitboard):
        while bitboard:
            source_square = Bit.get_least_significant_first_bit(bitboard)

            self.move_parameters.source_square = source_square

            self.generate_capture_moves(source_square)

            bitboard = Bit.pop_bit(bitboard, source_square)

    def generate_capture_moves(self, source_square):
        offset = ~self.occupancies[self.side]
        attacks = self.knight_attack_table[source_square] & offset

        while attacks:
            target_square = Bit.get_least_significant_first_bit(attacks)

            self.move_parameters.target_square = target_square

            if self.check_piece_in_the_way(target_square):
                self.add_capture_move()
            else:
                self.add_quiet_move()

            attacks = Bit.pop_bit(attacks, target_square)

    def add_capture_move(self):
        self.move_parameters.capture_flag = 1

        self.add_move()
        self.reset_move_parameters()

    def add_quiet_move(self):
        self.add_move()

    def check_piece_in_the_way(self, target_square):
        return Bit.get_bit(self.occupancies[self.side ^ 1], target_square)
