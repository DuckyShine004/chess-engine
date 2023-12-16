from src.utilities.attack import Attack

from src.lookup.colors import colors
from src.lookup.squares import squares

from src.constants.board_constants import (
    SIDES,
    SQUARES,
)


class TableManager:
    def __init__(self):
        self.pawn_attack_table = [[0] * SQUARES for _ in range(SIDES)]
        self.king_attack_table = [0] * SQUARES
        self.bishop_attack_table = [0] * SQUARES
        self.knight_attack_table = [0] * SQUARES

        self.initialize()

    def initialize(self):
        self.initialize_leaper_attack_tables()

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
