from src.generator.pieces.piece import Piece

from src.utilities.bit import Bit
from src.utilities.attack import Attack

from src.constants.piece_constants import SIDES


class Bishop(Piece):
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
        attacks = self.get_bishop_attacks(source_square) & offset

        while attacks:
            target_square = Bit.get_least_significant_first_bit(attacks)

            self.move_parameters.target_square = target_square

            if self.check_piece_in_the_way(target_square):
                self.add_capture_move()
            else:
                self.add_quiet_move()

            attacks = Bit.pop_bit(attacks, target_square)

    def get_bishop_attacks(self, source_square):
        occupancy = self.occupancies[SIDES["all"]]
        attack_table = self.bishop_attack_table
        attack_masks = self.bishop_attack_masks

        return Attack.get_bishop_attack_masks(source_square, occupancy, attack_table, attack_masks)

    def add_capture_move(self):
        self.move_parameters.capture_flag = 1

        self.add_move()
        self.reset_move_parameters()

    def add_quiet_move(self):
        self.add_move()

    def check_piece_in_the_way(self, target_square):
        return Bit.get_bit(self.occupancies[self.side ^ 1], target_square)
