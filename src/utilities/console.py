import numpy

from src.constants.board_constants import RANKS, FILES


class Console:
    @staticmethod
    def print_bitboard(bitboard: numpy.uint64):
        for rank in range(RANKS):
            for file in range(FILES):
                square = rank * 8 + file
                print(square, end=" ")

            print()
