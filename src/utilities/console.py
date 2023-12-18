from src.utilities.bit import Bit

from src.lookup.board_lookup import COORDINATES
from src.lookup.piece_lookup import CASTLE, UNICODE_PIECES

from src.constants.board_constants import (
    RANKS,
    FILES,
    NUMBER_OF_SQUARES,
    NUMBER_OF_BITBOARDS,
)


class Console:
    @staticmethod
    def print_bitboard(bitboard):
        print()

        for rank in range(RANKS):
            print(f"{8 - rank} ", end="")

            for file in range(FILES):
                square = rank * 8 + file
                print(f" {1 if Bit.get_bit(bitboard, square) else 0}", end="")

            print()

        print("\n   a b c d e f g h\n")
        print(f"   Bitboard: {bitboard}")

    @staticmethod
    def print_board(bitboards, enpassant, castle, side):
        enpassant_msg = COORDINATES[enpassant] if enpassant < NUMBER_OF_SQUARES else "no"

        castle_white_king_side = "K" if castle & CASTLE["white_king_side"] else "-"
        castle_white_queen_side = "Q" if castle & CASTLE["white_queen_side"] else "-"
        castle_black_king_side = "k" if castle & CASTLE["black_king_side"] else "-"
        castle_black_queen_side = "q" if castle & CASTLE["black_queen_side"] else "-"

        print()

        for rank in range(RANKS):
            print(f"{8 - rank} ", end="")

            for file in range(FILES):
                square = rank * 8 + file
                piece = -1

                for bitboard_piece in range(NUMBER_OF_BITBOARDS):
                    if Bit.get_bit(bitboards[bitboard_piece], square):
                        piece = bitboard_piece

                print(f" {'.' if piece == -1 else UNICODE_PIECES[piece]}", end="")

            print()

        print("\n   a b c d e f g h\n")
        print(f"   Side:     {'white' if not side and side != -1 else 'black'}")
        print(f"   Enpassant:   {enpassant_msg}")
        print("   Castling:  ", end="")
        print(castle_white_king_side + castle_white_queen_side, end="")
        print(castle_black_king_side + castle_black_queen_side, end="")
