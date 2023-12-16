from src.utilities.bit import Bit

from src.constants.board_constants import (
    RANKS,
    FILES,
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
            if NOT_A_FILE & Bit.right_shift(bitboard, 7):
                attacks |= Bit.right_shift(bitboard, 7)

            if NOT_H_FILE & Bit.right_shift(bitboard, 9):
                attacks |= Bit.right_shift(bitboard, 9)
        else:
            if NOT_H_FILE & Bit.left_shift(bitboard, 7):
                attacks |= Bit.left_shift(bitboard, 7)

            if NOT_A_FILE & Bit.left_shift(bitboard, 9):
                attacks |= Bit.left_shift(bitboard, 9)

        return attacks

    @staticmethod
    def get_knight_attacks(square):
        attacks = bitboard = 0

        bitboard = Bit.set_bit(bitboard, square)

        if NOT_H_FILE & Bit.right_shift(bitboard, 17):
            attacks |= Bit.right_shift(bitboard, 17)

        if NOT_A_FILE & Bit.right_shift(bitboard, 15):
            attacks |= Bit.right_shift(bitboard, 15)

        if NOT_HG_FILE & Bit.right_shift(bitboard, 10):
            attacks |= Bit.right_shift(bitboard, 10)

        if NOT_AB_FILE & Bit.right_shift(bitboard, 6):
            attacks |= Bit.right_shift(bitboard, 6)

        if NOT_A_FILE & Bit.left_shift(bitboard, 17):
            attacks |= Bit.left_shift(bitboard, 17)

        if NOT_H_FILE & Bit.left_shift(bitboard, 15):
            attacks |= Bit.left_shift(bitboard, 15)

        if NOT_AB_FILE & Bit.left_shift(bitboard, 10):
            attacks |= Bit.left_shift(bitboard, 10)

        if NOT_HG_FILE & Bit.left_shift(bitboard, 6):
            attacks |= Bit.left_shift(bitboard, 6)

        return attacks

    @staticmethod
    def get_king_attacks(square):
        attacks = bitboard = 0

        bitboard = Bit.set_bit(bitboard, square)

        if Bit.right_shift(bitboard, 8):
            attacks |= Bit.right_shift(bitboard, 8)

        if NOT_H_FILE & Bit.right_shift(bitboard, 9):
            attacks |= Bit.right_shift(bitboard, 9)

        if NOT_A_FILE & Bit.right_shift(bitboard, 7):
            attacks |= Bit.right_shift(bitboard, 7)

        if NOT_H_FILE & Bit.right_shift(bitboard, 1):
            attacks |= Bit.right_shift(bitboard, 1)

        if Bit.left_shift(bitboard, 8):
            attacks |= Bit.left_shift(bitboard, 8)

        if NOT_A_FILE & (Bit.left_shift(bitboard, 9)):
            attacks |= Bit.left_shift(bitboard, 9)

        if NOT_H_FILE & Bit.left_shift(bitboard, 7):
            attacks |= Bit.left_shift(bitboard, 7)

        if NOT_A_FILE & Bit.left_shift(bitboard, 1):
            attacks |= Bit.left_shift(bitboard, 1)

        return attacks

    @staticmethod
    def get_bishop_attacks(square):
        attacks = 0

        target_rank = square // RANKS
        target_file = square % FILES

        rank = target_rank + 1
        file = target_file + 1

        while rank <= 6 and file <= 6:
            attacks = Bit.set_bit(attacks, rank * 8 + file)

            rank += 1
            file += 1

        rank = target_rank - 1
        file = target_file + 1

        while rank >= 1 and file <= 6:
            attacks = Bit.set_bit(attacks, rank * 8 + file)

            rank -= 1
            file += 1

        rank = target_rank + 1
        file = target_file - 1

        while rank <= 6 and file >= 1:
            attacks = Bit.set_bit(attacks, rank * 8 + file)

            rank += 1
            file -= 1

        rank = target_rank - 1
        file = target_file - 1

        while rank >= 1 and file >= 1:
            attacks = Bit.set_bit(attacks, rank * 8 + file)

            rank -= 1
            file -= 1

        return attacks

    @staticmethod
    def get_rook_attacks(square):
        attacks = 0

        target_rank = square // RANKS
        target_file = square % FILES

        for rank in range(target_rank + 1, 7):
            attacks = Bit.set_bit(attacks, rank * 8 + target_file)

        for rank in range(target_rank - 1, 0, -1):
            attacks = Bit.set_bit(attacks, rank * 8 + target_file)

        for file in range(target_file + 1, 7):
            attacks = Bit.set_bit(attacks, target_rank * 8 + file)

        for file in range(target_file - 1, 0, -1):
            attacks = Bit.set_bit(attacks, target_rank * 8 + file)

        return attacks
