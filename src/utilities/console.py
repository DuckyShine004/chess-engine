from src.utilities.bit import Bit

from src.constants.board_constants import RANKS, FILES


class Console:
    @staticmethod
    def print_bitboard(bitboard):
        print()

        for rank in range(RANKS):
            print(f"  {8 - rank} ", end="")

            for file in range(FILES):
                square = rank * 8 + file
                print(f" {1 if Bit.get_bit(bitboard, square) else 0}", end="")

            print()

        print("\n     a b c d e f g h\n")
        print(f"     Bitboard: {bitboard}")
