from src.utilities.bit import Bit
from src.utilities.math import Math

from src.lookup.bit_lookup import BISHOP_RELEVANT_BITS, ROOK_RELEVANT_BITS
from src.lookup.piece_lookup import SIDES, PIECES
from src.lookup.number_lookup import BISHOP_MAGIC_NUMBERS, ROOK_MAGIC_NUMBERS

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
        attacks = 0
        bitboard = 0

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
        attacks = 0
        bitboard = 0

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
        attacks = 0
        bitboard = 0

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

    @staticmethod
    def get_bishop_attacks_on_the_fly(square, occupancy_bitboard):
        attacks = 0

        target_rank = square // RANKS
        target_file = square % FILES

        rank = target_rank + 1
        file = target_file + 1

        while rank <= 7 and file <= 7:
            attacks = Bit.set_bit(attacks, rank * 8 + file)

            if Bit.get_bit(occupancy_bitboard, rank * 8 + file):
                break

            rank += 1
            file += 1

        rank = target_rank - 1
        file = target_file + 1

        while rank >= 0 and file <= 7:
            attacks = Bit.set_bit(attacks, rank * 8 + file)

            if Bit.get_bit(occupancy_bitboard, rank * 8 + file):
                break

            rank -= 1
            file += 1

        rank = target_rank + 1
        file = target_file - 1

        while rank <= 7 and file >= 0:
            attacks = Bit.set_bit(attacks, rank * 8 + file)

            if Bit.get_bit(occupancy_bitboard, rank * 8 + file):
                break

            rank += 1
            file -= 1

        rank = target_rank - 1
        file = target_file - 1

        while rank >= 0 and file >= 0:
            attacks = Bit.set_bit(attacks, rank * 8 + file)

            if Bit.get_bit(occupancy_bitboard, rank * 8 + file):
                break

            rank -= 1
            file -= 1

        return attacks

    @staticmethod
    def get_rook_attacks_on_the_fly(square, occupancy_bitboard):
        attacks = 0

        target_rank = square // RANKS
        target_file = square % FILES

        for rank in range(target_rank + 1, 8):
            attacks = Bit.set_bit(attacks, rank * 8 + target_file)

            if Bit.get_bit(occupancy_bitboard, rank * 8 + target_file):
                break

        for rank in range(target_rank - 1, -1, -1):
            attacks = Bit.set_bit(attacks, rank * 8 + target_file)

            if Bit.get_bit(occupancy_bitboard, rank * 8 + target_file):
                break

        for file in range(target_file + 1, 8):
            attacks = Bit.set_bit(attacks, target_rank * 8 + file)

            if Bit.get_bit(occupancy_bitboard, target_rank * 8 + file):
                break

        for file in range(target_file - 1, -1, -1):
            attacks = Bit.set_bit(attacks, target_rank * 8 + file)

            if Bit.get_bit(occupancy_bitboard, target_rank * 8 + file):
                break

        return attacks

    @staticmethod
    def get_bishop_attack_masks(square, occupancy, attack_table, attack_mask):
        occupancy &= attack_mask[square]
        occupancy = Math.multiply(occupancy, BISHOP_MAGIC_NUMBERS[square])
        occupancy = Bit.right_shift(occupancy, 64 - BISHOP_RELEVANT_BITS[square])

        return attack_table[square][occupancy]

    @staticmethod
    def get_rook_attack_masks(square, occupancy, attack_table, attack_mask):
        occupancy &= attack_mask[square]
        occupancy = Math.multiply(occupancy, ROOK_MAGIC_NUMBERS[square])
        occupancy = Bit.right_shift(occupancy, 64 - ROOK_RELEVANT_BITS[square])

        return attack_table[square][occupancy]

    @staticmethod
    def get_queen_attack_masks(square, occupancy, attack_tables, attack_masks):
        bishop_attack_table, rook_attack_table = attack_tables
        bishop_attack_mask, rook_attack_mask = attack_masks

        bishop_attacks = Attack.get_bishop_attack_masks(
            square, occupancy, bishop_attack_table, bishop_attack_mask
        )

        rook_attacks = Attack.get_rook_attack_masks(
            square, occupancy, rook_attack_table, rook_attack_mask
        )

        return bishop_attacks | rook_attacks

    @staticmethod
    def check_square_attacked(app, square, side):
        # Attacked by white pawns
        if (side == SIDES["white"]) and (
            app.table_manager.pawn_attack_table[SIDES["black"]][square]
            & app.bitboard_manager.bitboards[PIECES["P"]]
        ):
            return True

        # Attacked by black pawns
        if (side == SIDES["black"]) and (
            app.table_manager.pawn_attack_table[SIDES["white"]][square]
            & app.bitboard_manager.bitboards[PIECES["p"]]
        ):
            return True

        return False
