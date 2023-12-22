from src.utilities.bit import Bit
from src.utilities.math import Math
from src.utilities.attack import Attack

from src.lookup.bit_lookup import BISHOP_RELEVANT_BITS, ROOK_RELEVANT_BITS
from src.lookup.piece_lookup import SIDES, SLIDERS
from src.lookup.board_lookup import SQUARES
from src.lookup.number_lookup import BISHOP_MAGIC_NUMBERS, ROOK_MAGIC_NUMBERS

from src.constants.bit_constants import OCCUPANCIES, MAGIC_NUMBERS
from src.constants.board_constants import NUMBER_OF_SIDES, NUMBER_OF_SQUARES


class TableManager:
    def __init__(self):
        self.pawn_attack_table = [[0] * NUMBER_OF_SQUARES for _ in range(NUMBER_OF_SIDES)]
        self.king_attack_table = [0] * NUMBER_OF_SQUARES
        self.rook_attack_table = [[0] * MAGIC_NUMBERS for _ in range(NUMBER_OF_SQUARES)]
        self.bishop_attack_table = [[0] * OCCUPANCIES for _ in range(NUMBER_OF_SQUARES)]
        self.knight_attack_table = [0] * NUMBER_OF_SQUARES

        self.rook_attack_masks = [0] * NUMBER_OF_SQUARES
        self.bishop_attack_masks = [0] * NUMBER_OF_SQUARES

        self.initialize_tables()

    def initialize_tables(self):
        self.initialize_leaper_attack_tables()
        self.initialize_slider_attack_tables(SLIDERS["bishop"])
        self.initialize_slider_attack_tables(SLIDERS["rook"])

    def initialize_leaper_attack_tables(self):
        for square in range(NUMBER_OF_SQUARES):
            self.initialize_pawn_attacks(square)
            self.king_attack_table[square] = Attack.get_king_attacks(square)
            self.knight_attack_table[square] = Attack.get_knight_attacks(square)

    def initialize_pawn_attacks(self, square):
        white_pawn_attacks = Attack.get_pawn_attacks(SIDES["white"], square)
        black_pawn_attacks = Attack.get_pawn_attacks(SIDES["black"], square)

        self.pawn_attack_table[SIDES["white"]][square] = white_pawn_attacks
        self.pawn_attack_table[SIDES["black"]][square] = black_pawn_attacks

    def initialize_slider_attack_tables(self, is_bishop):
        for square in range(NUMBER_OF_SQUARES):
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

    def get_relevant_bits(self, square, is_bishop):
        attack_mask = 0

        if is_bishop:
            attack_mask = self.bishop_attack_masks[square]
        else:
            attack_mask = self.rook_attack_masks[square]

        return Bit.get_bit_count(attack_mask)
