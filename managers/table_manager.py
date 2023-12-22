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

            self.initialize_slider_attacks(square, is_bishop)

    def initialize_slider_attacks(self, square, is_bishop):
        attack_mask = self.get_attack_mask(square, is_bishop)
        relevant_bits = Bit.get_bit_count(attack_mask)
        indices = Bit.left_shift(1, relevant_bits)

        for index in range(indices):
            occupancy = Bit.set_occupancy(index, relevant_bits, attack_mask)
            magic_index = self.get_magic_index(square, occupancy, is_bishop)
            self.update_attack_table(square, magic_index, occupancy, is_bishop)

    def get_attack_mask(self, square, is_bishop):
        if is_bishop:
            return self.bishop_attack_masks[square]

        return self.rook_attack_masks[square]

    def get_magic_index(self, square, occupancy, is_bishop):
        if is_bishop:
            magic_number = BISHOP_MAGIC_NUMBERS[square]
            offset = 64 - BISHOP_RELEVANT_BITS[square]
        else:
            magic_number = ROOK_MAGIC_NUMBERS[square]
            offset = 64 - ROOK_RELEVANT_BITS[square]

        magic_mask = Math.multiply(occupancy, magic_number)

        return Bit.right_shift32(magic_mask, offset)

    def get_attacks_on_the_fly(self, square, occupancy, is_bishop):
        if is_bishop:
            return Attack.get_bishop_attacks_on_the_fly(square, occupancy)

        return Attack.get_rook_attacks_on_the_fly(square, occupancy)

    def update_attack_table(self, square, magic_index, occupancy, is_bishop):
        attacks_on_the_fly = self.get_attacks_on_the_fly(square, occupancy, is_bishop)

        if is_bishop:
            self.bishop_attack_table[square][magic_index] = attacks_on_the_fly
        else:
            self.rook_attack_table[square][magic_index] = attacks_on_the_fly
