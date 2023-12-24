from src.routines.attacked import Attacked

from src.utilities.bit import Bit
from src.utilities.attack import Attack

from src.lookup.board_lookup import SQUARES, COORDINATES
from src.lookup.piece_lookup import SIDES, PIECES, CASTLE

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
        knight_attack_table = app.table_manager.knight_attack_table
        bishop_attack_table = app.table_manager.bishop_attack_table
        bishop_attack_masks = app.table_manager.bishop_attack_masks
        rook_attack_table = app.table_manager.rook_attack_table
        rook_attack_masks = app.table_manager.rook_attack_masks
        attack_tables = (bishop_attack_table, rook_attack_table)
        attack_masks = (bishop_attack_masks, rook_attack_masks)

        enpassant = app.bitboard_manager.enpassant
        castle = app.bitboard_manager.castle

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
                            if SQUARES["a7"] <= source_square <= SQUARES["h7"]:
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}q pawn promotion"
                                )
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}r pawn promotion"
                                )
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}b pawn promotion"
                                )
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}n pawn promotion"
                                )
                            else:
                                # One square ahead pawn move
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]} pawn push"
                                )

                                # Two squares ahead pawn move
                                if (SQUARES["a2"] <= source_square <= SQUARES["h2"]) and not Bit.get_bit(
                                    occupancies[SIDES["all"]], target_square - 8
                                ):
                                    print(
                                        f"{COORDINATES[source_square]}{COORDINATES[target_square - 8]} double pawn push"
                                    )

                        # Initialize pawn attacks bitboard
                        attacks = pawn_attack_table[side][source_square] & occupancies[SIDES["black"]]

                        # Generate pawn captures
                        while attacks:
                            target_square = Bit.get_least_significant_first_bit(attacks)

                            if SQUARES["a7"] <= source_square <= SQUARES["h7"]:
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}q pawn promotion capture"
                                )
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}r pawn promotion capture"
                                )
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}b pawn promotion capture"
                                )
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}n pawn promotion capture"
                                )
                            else:
                                # One square ahead pawn move
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]} pawn capture"
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

                # Castling moves for the white king
                if board_index == PIECES["K"]:
                    # King side castling is available
                    if castle & CASTLE["K"]:
                        # Make sure that there are no pieces in between the king and rook
                        if not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["f1"]) and not Bit.get_bit(
                            occupancies[SIDES["all"]], SQUARES["g1"]
                        ):
                            # Make sure the king and the f1 squares are not under attack
                            if not Attacked.check_squares_attacked(
                                app, SQUARES["e1"], SIDES["black"]
                            ) and not Attacked.check_squares_attacked(
                                app, SQUARES["f1"], SIDES["black"]
                            ):
                                print("e1g1 castling move")

                    # Queen side castling is available
                    if castle & CASTLE["Q"]:
                        if (
                            not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["d1"])
                            and not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["c1"])
                            and not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["b1"])
                        ):
                            # Make sure the king and the f1 squares are not under attack
                            if not Attacked.check_squares_attacked(
                                app, SQUARES["e1"], SIDES["black"]
                            ) and not Attacked.check_squares_attacked(
                                app, SQUARES["d1"], SIDES["black"]
                            ):
                                print("e1c1 castling move")

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
                            if SQUARES["a2"] <= source_square <= SQUARES["h2"]:
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}q pawn promotion"
                                )
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}r pawn promotion"
                                )
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}b pawn promotion"
                                )
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}n pawn promotion"
                                )
                            else:
                                # One square ahead pawn move
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]} pawn push"
                                )

                                # Two squares ahead pawn move
                                if (SQUARES["a7"] <= source_square <= SQUARES["h7"]) and not Bit.get_bit(
                                    occupancies[SIDES["all"]], target_square + 8
                                ):
                                    print(
                                        f"{COORDINATES[source_square]}{COORDINATES[target_square + 8]} double pawn push"
                                    )

                        # Initialize pawn attacks bitboard
                        attacks = pawn_attack_table[side][source_square] & occupancies[SIDES["white"]]

                        # Generate pawn captures
                        while attacks:
                            target_square = Bit.get_least_significant_first_bit(attacks)

                            if SQUARES["a2"] <= source_square <= SQUARES["h2"]:
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}q pawn promotion capture"
                                )
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}r pawn promotion capture"
                                )
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}b pawn promotion capture"
                                )
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]}n pawn promotion capture"
                                )
                            else:
                                # One square ahead pawn move
                                print(
                                    f"{COORDINATES[source_square]}{COORDINATES[target_square]} pawn capture"
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
                                    f"{COORDINATES[source_square]}{COORDINATES[target_enpassant]} pawn enpassant capture"
                                )
                        # Pop least significant first bit from bitboard
                        bitboard = Bit.pop_bit(bitboard, source_square)

                # Castling moves for the black king
                if board_index == PIECES["k"]:
                    # King side castling is available
                    if castle & CASTLE["k"]:
                        # Make sure that there are no pieces in between the king and rook
                        if not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["f8"]) and not Bit.get_bit(
                            occupancies[SIDES["all"]], SQUARES["g8"]
                        ):
                            # Make sure the king and the f1 squares are not under attack
                            if not Attacked.check_squares_attacked(
                                app, SQUARES["e8"], SIDES["white"]
                            ) and not Attacked.check_squares_attacked(
                                app, SQUARES["f8"], SIDES["white"]
                            ):
                                print("e8g8 castling move")

                    # Queen side castling is available
                    if castle & CASTLE["q"]:
                        if (
                            not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["d8"])
                            and not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["c8"])
                            and not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["b8"])
                        ):
                            # Make sure the king and the f8 squares are not under attack
                            if not Attacked.check_squares_attacked(
                                app, SQUARES["e8"], SIDES["white"]
                            ) and not Attacked.check_squares_attacked(
                                app, SQUARES["d8"], SIDES["white"]
                            ):
                                print("e8c8 castling move")

            # Generate knight moves
            if board_index == PIECES["N"] if side == SIDES["white"] else board_index == PIECES["n"]:
                # Loop over source squares of piece bitboard
                while bitboard:
                    source_square = Bit.get_least_significant_first_bit(bitboard)

                    # Initialize piece attacks in order to get the set of target squares
                    attacks = knight_attack_table[source_square] & (
                        ~occupancies[SIDES["white"]]
                        if side == SIDES["white"]
                        else ~occupancies[SIDES["black"]]
                    )

                    # Loop over the target squares available from generated attacks
                    while attacks:
                        target_square = Bit.get_least_significant_first_bit(attacks)

                        # Quiet moves
                        if not Bit.get_bit(
                            occupancies[SIDES["black"]]
                            if side == SIDES["white"]
                            else occupancies[SIDES["white"]],
                            target_square,
                        ):
                            print(
                                f"{COORDINATES[source_square]}{COORDINATES[target_square]} piece quiet move"
                            )

                        # Capture moves
                        else:
                            print(
                                f"{COORDINATES[source_square]}{COORDINATES[target_square]} piece capture"
                            )

                        attacks = Bit.pop_bit(attacks, target_square)

                    bitboard = Bit.pop_bit(bitboard, source_square)

            # Generate bishop moves
            if board_index == PIECES["B"] if side == SIDES["white"] else board_index == PIECES["b"]:
                # Loop over source squares of piece bitboard
                while bitboard:
                    source_square = Bit.get_least_significant_first_bit(bitboard)

                    # Initialize piece attacks in order to get the set of target squares
                    attacks = Attack.get_bishop_attack_masks(
                        source_square,
                        occupancies[SIDES["all"]],
                        bishop_attack_table,
                        bishop_attack_masks,
                    ) & (
                        ~occupancies[SIDES["white"]]
                        if side == SIDES["white"]
                        else ~occupancies[SIDES["black"]]
                    )

                    # Loop over the target squares available from generated attacks
                    while attacks:
                        target_square = Bit.get_least_significant_first_bit(attacks)

                        # Quiet moves
                        if not Bit.get_bit(
                            occupancies[SIDES["black"]]
                            if side == SIDES["white"]
                            else occupancies[SIDES["white"]],
                            target_square,
                        ):
                            print(
                                f"{COORDINATES[source_square]}{COORDINATES[target_square]} piece quiet move"
                            )

                        # Capture moves
                        else:
                            print(
                                f"{COORDINATES[source_square]}{COORDINATES[target_square]} piece capture"
                            )

                        attacks = Bit.pop_bit(attacks, target_square)

                    bitboard = Bit.pop_bit(bitboard, source_square)

            # Generate rook moves
            if board_index == PIECES["R"] if side == SIDES["white"] else board_index == PIECES["r"]:
                # Loop over source squares of piece bitboard
                while bitboard:
                    source_square = Bit.get_least_significant_first_bit(bitboard)

                    # Initialize piece attacks in order to get the set of target squares
                    attacks = Attack.get_rook_attack_masks(
                        source_square,
                        occupancies[SIDES["all"]],
                        rook_attack_table,
                        rook_attack_masks,
                    ) & (
                        ~occupancies[SIDES["white"]]
                        if side == SIDES["white"]
                        else ~occupancies[SIDES["black"]]
                    )

                    # Loop over the target squares available from generated attacks
                    while attacks:
                        target_square = Bit.get_least_significant_first_bit(attacks)

                        # Quiet moves
                        if not Bit.get_bit(
                            occupancies[SIDES["black"]]
                            if side == SIDES["white"]
                            else occupancies[SIDES["white"]],
                            target_square,
                        ):
                            print(
                                f"{COORDINATES[source_square]}{COORDINATES[target_square]} piece quiet move"
                            )

                        # Capture moves
                        else:
                            print(
                                f"{COORDINATES[source_square]}{COORDINATES[target_square]} piece capture"
                            )

                        attacks = Bit.pop_bit(attacks, target_square)

                    bitboard = Bit.pop_bit(bitboard, source_square)

            # Generate queen moves
            if board_index == PIECES["Q"] if side == SIDES["white"] else board_index == PIECES["q"]:
                # Loop over source squares of piece bitboard
                while bitboard:
                    source_square = Bit.get_least_significant_first_bit(bitboard)

                    # Initialize piece attacks in order to get the set of target squares
                    attacks = Attack.get_queen_attack_masks(
                        source_square,
                        occupancies[SIDES["all"]],
                        attack_tables,
                        attack_masks,
                    ) & (
                        ~occupancies[SIDES["white"]]
                        if side == SIDES["white"]
                        else ~occupancies[SIDES["black"]]
                    )

                    # Loop over the target squares available from generated attacks
                    while attacks:
                        target_square = Bit.get_least_significant_first_bit(attacks)

                        # Quiet moves
                        if not Bit.get_bit(
                            occupancies[SIDES["black"]]
                            if side == SIDES["white"]
                            else occupancies[SIDES["white"]],
                            target_square,
                        ):
                            print(
                                f"{COORDINATES[source_square]}{COORDINATES[target_square]} piece quiet move"
                            )

                        # Capture moves
                        else:
                            print(
                                f"{COORDINATES[source_square]}{COORDINATES[target_square]} piece capture"
                            )

                        attacks = Bit.pop_bit(attacks, target_square)

                    bitboard = Bit.pop_bit(bitboard, source_square)

            # Generate king moves
