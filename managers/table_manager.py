from src.utilities.attack import Attack

from src.lookup.colors import colors
from src.lookup.squares import squares


from src.utilities.bit import Bit
from src.utilities.math import Math

from src.lookup.magic_numbers import BISHOP_MAGIC_NUMBERS, ROOK_MAGIC_NUMBERS
from src.lookup.relevant_bits import BISHOP_RELEVANT_BITS, ROOK_RELEVANT_BITS

from src.constants.constants import OCCUPANCIES, MAGIC_NUMBERS
from src.constants.board_constants import SIDES, SQUARES


class TableManager:
    def __init__(self):
        self.pawn_attack_table = [[0] * SQUARES for _ in range(SIDES)]
        self.king_attack_table = [0] * SQUARES
        self.rook_attack_table = [[0] * SQUARES for _ in range(MAGIC_NUMBERS)]
        self.bishop_attack_table = [[0] * SQUARES for _ in range(OCCUPANCIES)]
        self.knight_attack_table = [0] * SQUARES

        self.rook_attack_masks = [0] * SQUARES
        self.bishop_attack_masks = [0] * SQUARES

        self.initialize()

    def initialize(self):
        self.initialize_leaper_attack_tables()
        # self.initialize_slider_attack_tables(is_bishop)

    def initialize_leaper_attack_tables(self):
        for square in range(SQUARES):
            white_pawn_attacks = Attack.get_pawn_attacks(colors["white"], square)
            black_pawn_attacks = Attack.get_pawn_attacks(colors["black"], square)
            king_attacks = Attack.get_king_attacks(square)
            knight_attacks = Attack.get_knight_attacks(square)

            self.pawn_attack_table[colors["white"]][square] = white_pawn_attacks
            self.pawn_attack_table[colors["black"]][square] = black_pawn_attacks
            self.king_attack_table[square] = king_attacks
            self.knight_attack_table[square] = knight_attacks

    def initialize_slider_attack_tables(self, is_bishop):
        for square in range(SQUARES):
            self.bishop_attack_masks[square] = Attack.get_bishop_attacks(square)
            self.rook_attack_masks[square] = Attack.get_rook_attacks(square)

            attack_mask = None

            if is_bishop:
                attack_mask = self.bishop_attack_masks[square]
            else:
                attack_mask = self.rook_attack_masks[square]

            relevant_bits = Bit.get_bit_count(attack_mask)
            occupancy_indices = Bit.left_shift(1, relevant_bits)

            for index in range(occupancy_indices):
                if is_bishop:
                    occupancy = Bit.set_occupancy(index, relevant_bits, attack_mask)
                    offset = 64 - BISHOP_RELEVANT_BITS[square]

                    magic_mask = Math.multiply(occupancy, BISHOP_MAGIC_NUMBERS[square])
                    magic_index = Bit.right_shift32(magic_mask, offset)

                    m_bishop = Attack.get_bishop_attacks_on_the_fly(square, occupancy)

                    self.bishop_attack_table[square][magic_index] = m_bishop
                else:
                    occupancy = Bit.set_occupancy(index, relevant_bits, attack_mask)
                    offset = 64 - ROOK_RELEVANT_BITS[square]

                    magic_mask = Math.multiply(occupancy, ROOK_MAGIC_NUMBERS[square])
                    magic_index = Bit.right_shift32(magic_mask, offset)

                    m_rook = Attack.get_rook_attacks_on_the_fly(square, occupancy)

                    self.rook_attack_table[square][magic_index] = m_rook
