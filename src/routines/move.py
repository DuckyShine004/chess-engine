from src.utilities.bit import Bit

from src.lookup.board_lookup import SQUARES, COORDINATES
from src.lookup.piece_lookup import SIDES, PIECES

from src.constants.board_constants import NUMBER_OF_BITBOARDS


class Move:
    # def __init__(self, bitboards):
    #     self.bitboards = bitboards

    @staticmethod
    def generate_moves(app):
        bitboards = app.bitboard_manager.bitboards
        occupancies = app.bitboard_manager.occupancies
        side = app.bitboard_manager.side
        pawn_attack_table = app.table_manager.pawn_attack_table
        enpassant = app.bitboard_manager.enpassant

        for board_index in range(NUMBER_OF_BITBOARDS):
            bitboard = bitboards[board_index]
            # Generate white pawns and white king castling move
            if side == SIDES["white"]:
                if board_index == PIECES["P"]:
                    # Loop over white pawns within white pawn bitboard
                    while bitboard:
                        source_square = Bit.get_least_significant_first_bit(bitboard)
                        target_square = source_square - 8

                        # Generate quiet pawn moves
                        if target_square >= SQUARES["a8"] and not Bit.get_bit(
                            occupancies[SIDES["all"]], target_square
                        ):
                            # Pawn promotion
                            if source_square >= SQUARES["a7"] and source_square <= SQUARES["h7"]:
                                print(
                                    f"pawn promotion: {COORDINATES[source_square]}{COORDINATES[target_square]}q"
                                )
                                print(
                                    f"pawn promotion: {COORDINATES[source_square]}{COORDINATES[target_square]}r"
                                )
                                print(
                                    f"pawn promotion: {COORDINATES[source_square]}{COORDINATES[target_square]}b"
                                )
                                print(
                                    f"pawn promotion: {COORDINATES[source_square]}{COORDINATES[target_square]}n"
                                )
                            else:
                                # One square ahead pawn move
                                print(
                                    f"pawn push: {COORDINATES[source_square]}{COORDINATES[target_square]}"
                                )

                                # Two squares ahead pawn move
                                if (
                                    source_square >= SQUARES["a2"] and source_square <= SQUARES["h2"]
                                ) and not Bit.get_bit(occupancies[SIDES["all"]], target_square - 8):
                                    print(
                                        f"double pawn push: {COORDINATES[source_square]}{COORDINATES[target_square - 8]}"
                                    )

                        # Initialize pawn attacks bitboard
                        attacks = pawn_attack_table[side][source_square] & occupancies[SIDES["black"]]

                        # Generate pawn captures
                        while attacks:
                            target_square = Bit.get_least_significant_first_bit(attacks)

                            if source_square >= SQUARES["a7"] and source_square <= SQUARES["h7"]:
                                print(
                                    f"pawn promotion capture: {COORDINATES[source_square]}{COORDINATES[target_square]}q"
                                )
                                print(
                                    f"pawn promotion capture: {COORDINATES[source_square]}{COORDINATES[target_square]}r"
                                )
                                print(
                                    f"pawn promotion capture: {COORDINATES[source_square]}{COORDINATES[target_square]}b"
                                )
                                print(
                                    f"pawn promotion capture: {COORDINATES[source_square]}{COORDINATES[target_square]}n"
                                )
                            else:
                                # One square ahead pawn move
                                print(
                                    f"pawn capture: {COORDINATES[source_square]}{COORDINATES[target_square]}"
                                )

                            attacks = Bit.pop_bit(attacks, target_square)

                        # Enpassant square captures
                        if enpassant != SQUARES["null"]:
                            # Lookup pawn attacks and bitwise and with enpassant square
                            enpassant_attacks = pawn_attack_table[side][source_square] & Bit.left_shift(
                                1, enpassant
                            )

                            if enpassant_attacks:
                                target_enpassant = Bit.get_least_significant_first_bit(enpassant_attacks)
                                print(
                                    f"pawn enpassant capture: {COORDINATES[source_square]}{COORDINATES[target_enpassant]}"
                                )

                        # Pop least significant first bit from bitboard
                        bitboard = Bit.pop_bit(bitboard, source_square)

            # Generate black pawns and black king castling moves
            else:
                if board_index == PIECES["p"]:
                    # Loop over black pawns within black pawn bitboard
                    while bitboard:
                        source_square = Bit.get_least_significant_first_bit(bitboard)
                        target_square = source_square + 8

                        # Generate quiet pawn moves
                        if target_square <= SQUARES["h1"] and not Bit.get_bit(
                            occupancies[SIDES["all"]], target_square
                        ):
                            # Pawn promotion
                            if source_square >= SQUARES["a2"] and source_square <= SQUARES["h2"]:
                                print(
                                    f"pawn promotion: {COORDINATES[source_square]}{COORDINATES[target_square]}q"
                                )
                                print(
                                    f"pawn promotion: {COORDINATES[source_square]}{COORDINATES[target_square]}r"
                                )
                                print(
                                    f"pawn promotion: {COORDINATES[source_square]}{COORDINATES[target_square]}b"
                                )
                                print(
                                    f"pawn promotion: {COORDINATES[source_square]}{COORDINATES[target_square]}n"
                                )
                            else:
                                # One square ahead pawn move
                                print(
                                    f"pawn push: {COORDINATES[source_square]}{COORDINATES[target_square]}"
                                )

                                # Two squares ahead pawn move
                                if (
                                    source_square >= SQUARES["a7"] and source_square <= SQUARES["h7"]
                                ) and not Bit.get_bit(occupancies[SIDES["all"]], target_square + 8):
                                    print(
                                        f"double pawn push: {COORDINATES[source_square]}{COORDINATES[target_square + 8]}"
                                    )

                        # Initialize pawn attacks bitboard
                        attacks = pawn_attack_table[side][source_square] & occupancies[SIDES["white"]]

                        # Generate pawn captures
                        while attacks:
                            target_square = Bit.get_least_significant_first_bit(attacks)

                            if source_square >= SQUARES["a2"] and source_square <= SQUARES["h2"]:
                                print(
                                    f"pawn promotion capture: {COORDINATES[source_square]}{COORDINATES[target_square]}q"
                                )
                                print(
                                    f"pawn promotion capture: {COORDINATES[source_square]}{COORDINATES[target_square]}r"
                                )
                                print(
                                    f"pawn promotion capture: {COORDINATES[source_square]}{COORDINATES[target_square]}b"
                                )
                                print(
                                    f"pawn promotion capture: {COORDINATES[source_square]}{COORDINATES[target_square]}n"
                                )
                            else:
                                # One square ahead pawn move
                                print(
                                    f"pawn capture: {COORDINATES[source_square]}{COORDINATES[target_square]}"
                                )

                            attacks = Bit.pop_bit(attacks, target_square)

                        # Enpassant square captures
                        if enpassant != SQUARES["null"]:
                            # Lookup pawn attacks and bitwise and with enpassant square
                            enpassant_attacks = pawn_attack_table[side][source_square] & Bit.left_shift(
                                1, enpassant
                            )

                            if enpassant_attacks:
                                target_enpassant = Bit.get_least_significant_first_bit(enpassant_attacks)
                                print(
                                    f"pawn enpassant capture: {COORDINATES[source_square]}{COORDINATES[target_enpassant]}"
                                )
                        # Pop least significant first bit from bitboard
                        bitboard = Bit.pop_bit(bitboard, source_square)

            # Generate knight moves

            # Generate bishop moves

            # Generate rook moves

            # Generate queen moves

            # Generate king moves
