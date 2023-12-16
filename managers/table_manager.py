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

        self.initialize()

    def initialize(self):
        self.initialize_leaper_attack_tables()

    def initialize_leaper_attack_tables(self):
        self.initialize_pawn_attack_table()

    def initialize_pawn_attack_table(self):
        for square in range(SQUARES):
            white_pawn_attacks = Attack.get_pawn_attacks(colors["white"], square)
            black_pawn_attacks = Attack.get_pawn_attacks(colors["black"], square)

            self.pawn_attack_table[colors["white"]][square] = white_pawn_attacks
            self.pawn_attack_table[colors["black"]][square] = black_pawn_attacks
