from src.routines.attacked import Attacked
from src.routines.deserializer import Deserializer

from src.utilities.bit import Bit

from src.constants.piece_constants import CASTLE, UNICODE_PIECES, PROMOTED_PIECES

from src.constants.board_constants import (
    RANKS,
    FILES,
    NUMBER_OF_SQUARES,
    NUMBER_OF_BITBOARDS,
    COORDINATES,
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

        Console.print_board_messages(enpassant, castle, side)

    @staticmethod
    def print_board_messages(enpassant, castle, side):
        side_message = "white" if not side and side != -1 else "black"

        enpassant_message = COORDINATES[enpassant] if enpassant < NUMBER_OF_SQUARES else "no"

        castle_white_king_side_message = "K" if castle & CASTLE["K"] else "-"
        castle_white_queen_side_message = "Q" if castle & CASTLE["Q"] else "-"
        castle_black_king_side_message = "k" if castle & CASTLE["k"] else "-"
        castle_black_queen_side_message = "q" if castle & CASTLE["q"] else "-"

        print("\n   a b c d e f g h\n")
        print(
            f"   Side:{side_message:>10}\n"
            f"   Enpassant:{enpassant_message:>5}\n"
            f"   Castling:{castle_white_king_side_message:>3}"
            f"{castle_white_queen_side_message}"
            f"{castle_black_king_side_message}"
            f"{castle_black_queen_side_message}"
        )

    @staticmethod
    def print_attacked_squares(app, side):
        print()

        for rank in range(RANKS):
            print(f"{8 - rank} ", end="")

            for file in range(FILES):
                square = rank * 8 + file
                print(f" {int(Attacked.check_squares_attacked(app, square, side))}", end="")

            print()

        print("\n   a b c d e f g h\n")

    @staticmethod
    def print_move(move):
        move_parameters = Deserializer.get_decoded_move_parameters(move)

        print(
            f"{COORDINATES[move_parameters.source_square]}"
            f"{COORDINATES[move_parameters.target_square]}"
            f"{PROMOTED_PIECES.get(move_parameters.promoted_piece, ' ')}"
        )

    @staticmethod
    def print_extended_move(move):
        move_parameters = Deserializer.get_decoded_move_parameters(move)

        print(
            f"{COORDINATES[move_parameters.source_square]:>5}"
            f"{COORDINATES[move_parameters.target_square]}"
            f"{PROMOTED_PIECES.get(move_parameters.promoted_piece, ' ')}"
            f"{UNICODE_PIECES[move_parameters.piece]:>4}"
            f"{move_parameters.capture_flag:>8}"
            f"{move_parameters.double_pawn_push_flag:>10}"
            f"{move_parameters.enpassant_flag:>10}"
            f"{move_parameters.castling_flag:>10}"
        )

    @staticmethod
    def print_moves(moves):
        if not moves.count:
            print("\n   No move in the move list")
            return

        print("\n   move    piece   capture   double    enpass    castling\n")

        for move_count in range(moves.count):
            move = moves.moves[move_count]
            Console.print_extended_move(move)

        print(f"\n   Total number of moves: {moves.count}")
