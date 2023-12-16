from src.utilities.bit import Bit

from src.constants.board_constants import (
    NOT_A_FILE,
    NOT_H_FILE,
    NOT_HG_FILE,
    NOT_AB_FILE,
)


class Attack:
    @staticmethod
    def get_pawn_attacks(side, square):
        attacks = bitboard = 0

        bitboard = Bit.set_bit(bitboard, square)

        if not side:
            if NOT_A_FILE & (bitboard >> 7):
                attacks |= bitboard >> 7

            if NOT_H_FILE & (bitboard >> 9):
                attacks |= bitboard >> 9
        else:
            if NOT_H_FILE & (bitboard << 7):
                attacks |= bitboard << 7

            if NOT_A_FILE & (bitboard << 9):
                attacks |= bitboard << 9

        return attacks
