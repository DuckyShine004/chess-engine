from src.lookup.squares import squares
from src.lookup.colors import colors

from src.utilities.bit import Bit
from src.utilities.console import Console

from src.constants.board_constants import (
    NOT_A_FILE,
    NOT_H_FILE,
    NOT_HG_FILE,
    NOT_AB_FILE,
)


def pawn_attacks(square, side):
    attacks = bitboard = 0

    bitboard = Bit.set_bit(bitboard, square)

    if not side:
        attacks = Bit.right_shift(bitboard, 7)
    else:
        pass

    return attacks


# bitboard = 0
# Console.print_bitboard(bitboard)
