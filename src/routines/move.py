from src.data_structures.moves import Moves
from src.data.parameters.move_parameters import MoveParameters

from src.routines.codec import Codec
from src.routines.attacked import Attacked

from src.utilities.bit import Bit
from src.utilities.attack import Attack

from src.constants.piece_constants import SIDES, PIECES, CASTLE
from src.constants.board_constants import NUMBER_OF_BITBOARDS, SQUARES, COORDINATES


class Move:
    # def __init__(self, bitboards):
    #     self.bitboards = bitboards

    @staticmethod
    def get_moves(app):
        moves = Moves()

        bitboards = app.bitboard_manager.bitboards
        occupancies = app.bitboard_manager.occupancies
        side = app.bitboard_manager.side
        pawn_attack_table = app.table_manager.pawn_attack_table
        knight_attack_table = app.table_manager.knight_attack_table
        bishop_attack_table = app.table_manager.bishop_attack_table
        bishop_attack_masks = app.table_manager.bishop_attack_masks
        rook_attack_table = app.table_manager.rook_attack_table
        rook_attack_masks = app.table_manager.rook_attack_masks
        king_attack_table = app.table_manager.king_attack_table
        attack_tables = (bishop_attack_table, rook_attack_table)
        attack_masks = (bishop_attack_masks, rook_attack_masks)

        enpassant = app.bitboard_manager.enpassant
        castle = app.bitboard_manager.castle

        for piece in range(NUMBER_OF_BITBOARDS):
            bitboard = bitboards[piece]
            # Generate white pawns and white king castling move
            # if side == SIDES["white"]:
            #     if piece == PIECES["P"]:
            #         # Loop over white pawns within white pawn bitboard
            #         while bitboard:
            #             source_square = Bit.get_least_significant_first_bit(bitboard)
            #             target_square = source_square - 8

            #             # Generate quiet pawn moves
            #             if target_square >= SQUARES["a8"] and not Bit.get_bit(
            #                 occupancies[SIDES["all"]], target_square
            #             ):
            #                 # Pawn promotion
            #                 if SQUARES["a7"] <= source_square <= SQUARES["h7"]:
            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["Q"], 0, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["R"], 0, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["B"], 0, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["N"], 0, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))
            #                 else:
            #                     # One square ahead pawn move
            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, 0, 0, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     # Two squares ahead pawn move
            #                     if (SQUARES["a2"] <= source_square <= SQUARES["h2"]) and not Bit.get_bit(
            #                         occupancies[SIDES["all"]], target_square - 8
            #                     ):
            #                         move_parameters = MoveParameters(
            #                             source_square, target_square - 8, piece, 0, 0, 1, 0, 0
            #                         )

            #                         moves.add_move(Codec.get_encoded_move(move_parameters))

            #             # Initialize pawn attacks bitboard
            #             attacks = pawn_attack_table[side][source_square] & occupancies[SIDES["black"]]

            #             # Generate pawn captures
            #             while attacks:
            #                 target_square = Bit.get_least_significant_first_bit(attacks)

            #                 # Pawn promotion captures
            #                 if SQUARES["a7"] <= source_square <= SQUARES["h7"]:
            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["Q"], 1, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["R"], 1, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["B"], 1, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["N"], 1, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))
            #                 else:
            #                     # One square ahead pawn move
            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, 0, 1, 0, 0, 0
            #                     )
            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                 attacks = Bit.pop_bit(attacks, target_square)

            #             # Enpassant square captures
            #             if enpassant != SQUARES["null"]:
            #                 # Lookup pawn attacks and bitwise and with enpassant square
            #                 enpassant_attacks = pawn_attack_table[side][source_square] & Bit.left_shift(
            #                     1, enpassant
            #                 )

            #                 if enpassant_attacks:
            #                     enpassant_square = Bit.get_least_significant_first_bit(enpassant_attacks)
            #                     move_parameters = MoveParameters(
            #                         source_square, enpassant_square, piece, 0, 1, 0, 1, 0
            #                     )
            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #             # Pop least significant first bit from bitboard
            #             bitboard = Bit.pop_bit(bitboard, source_square)

            #     # Castling moves for the white king
            #     if piece == PIECES["K"]:
            #         # King side castling is available
            #         if castle & CASTLE["K"]:
            #             # Make sure that there are no pieces in between the king and rook
            #             if not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["f1"]) and not Bit.get_bit(
            #                 occupancies[SIDES["all"]], SQUARES["g1"]
            #             ):
            #                 # Make sure the king and the f1 squares are not under attack
            #                 if not Attacked.check_squares_attacked(
            #                     app, SQUARES["e1"], SIDES["black"]
            #                 ) and not Attacked.check_squares_attacked(
            #                     app, SQUARES["f1"], SIDES["black"]
            #                 ):
            #                     move_parameters = MoveParameters(
            #                         SQUARES["e1"], SQUARES["g1"], piece, 0, 0, 0, 0, 1
            #                     )
            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #         # Queen side castling is available
            #         if castle & CASTLE["Q"]:
            #             if (
            #                 not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["d1"])
            #                 and not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["c1"])
            #                 and not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["b1"])
            #             ):
            #                 # Make sure the king and the f1 squares are not under attack
            #                 if not Attacked.check_squares_attacked(
            #                     app, SQUARES["e1"], SIDES["black"]
            #                 ) and not Attacked.check_squares_attacked(
            #                     app, SQUARES["d1"], SIDES["black"]
            #                 ):
            #                     move_parameters = MoveParameters(
            #                         SQUARES["e1"], SQUARES["c1"], piece, 0, 0, 0, 0, 1
            #                     )
            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            # # Generate black pawns and black king castling moves
            # else:
            #     if piece == PIECES["p"]:
            #         # Loop over black pawns within black pawn bitboard
            #         while bitboard:
            #             source_square = Bit.get_least_significant_first_bit(bitboard)
            #             target_square = source_square + 8

            #             # Generate quiet pawn moves
            #             if target_square <= SQUARES["h1"] and not Bit.get_bit(
            #                 occupancies[SIDES["all"]], target_square
            #             ):
            #                 # Pawn promotion
            #                 if SQUARES["a2"] <= source_square <= SQUARES["h2"]:
            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["q"], 0, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["r"], 0, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["b"], 0, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["n"], 0, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))
            #                 else:
            #                     # One square ahead pawn move
            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, 0, 0, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     # Two squares ahead pawn move
            #                     if (SQUARES["a7"] <= source_square <= SQUARES["h7"]) and not Bit.get_bit(
            #                         occupancies[SIDES["all"]], target_square + 8
            #                     ):
            #                         move_parameters = MoveParameters(
            #                             source_square, target_square + 8, piece, 0, 0, 1, 0, 0
            #                         )

            #                         moves.add_move(Codec.get_encoded_move(move_parameters))

            #             # Initialize pawn attacks bitboard
            #             attacks = pawn_attack_table[side][source_square] & occupancies[SIDES["white"]]

            #             # Generate pawn captures
            #             while attacks:
            #                 target_square = Bit.get_least_significant_first_bit(attacks)

            #                 if SQUARES["a2"] <= source_square <= SQUARES["h2"]:
            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["q"], 1, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["r"], 1, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["b"], 1, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, PIECES["n"], 1, 0, 0, 0
            #                     )

            #                     moves.add_move(Codec.get_encoded_move(move_parameters))
            #                 else:
            #                     # One square ahead pawn move
            #                     move_parameters = MoveParameters(
            #                         source_square, target_square, piece, 0, 1, 0, 0, 0
            #                     )
            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #                 attacks = Bit.pop_bit(attacks, target_square)

            #             # Enpassant square captures
            #             if enpassant != SQUARES["null"]:
            #                 # Lookup pawn attacks and bitwise and with enpassant square
            #                 enpassant_attacks = pawn_attack_table[side][source_square] & Bit.left_shift(
            #                     1, enpassant
            #                 )

            #                 if enpassant_attacks:
            #                     enpassant_square = Bit.get_least_significant_first_bit(enpassant_attacks)
            #                     move_parameters = MoveParameters(
            #                         source_square, enpassant_square, piece, 0, 1, 0, 1, 0
            #                     )
            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #             # Pop least significant first bit from bitboard
            #             bitboard = Bit.pop_bit(bitboard, source_square)

            #     # Castling moves for the black king
            #     if piece == PIECES["k"]:
            #         # King side castling is available
            #         if castle & CASTLE["k"]:
            #             # Make sure that there are no pieces in between the king and rook
            #             if not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["f8"]) and not Bit.get_bit(
            #                 occupancies[SIDES["all"]], SQUARES["g8"]
            #             ):
            #                 # Make sure the king and the f1 squares are not under attack
            #                 if not Attacked.check_squares_attacked(
            #                     app, SQUARES["e8"], SIDES["white"]
            #                 ) and not Attacked.check_squares_attacked(
            #                     app, SQUARES["f8"], SIDES["white"]
            #                 ):
            #                     move_parameters = MoveParameters(
            #                         SQUARES["e8"], SQUARES["g8"], piece, 0, 0, 0, 0, 1
            #                     )
            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            #         # Queen side castling is available
            #         if castle & CASTLE["q"]:
            #             if (
            #                 not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["d8"])
            #                 and not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["c8"])
            #                 and not Bit.get_bit(occupancies[SIDES["all"]], SQUARES["b8"])
            #             ):
            #                 # Make sure the king and the f8 squares are not under attack
            #                 if not Attacked.check_squares_attacked(
            #                     app, SQUARES["e8"], SIDES["white"]
            #                 ) and not Attacked.check_squares_attacked(
            #                     app, SQUARES["d8"], SIDES["white"]
            #                 ):
            #                     move_parameters = MoveParameters(
            #                         SQUARES["e8"], SQUARES["c8"], piece, 0, 0, 0, 0, 1
            #                     )
            #                     moves.add_move(Codec.get_encoded_move(move_parameters))

            # # Generate knight moves
            # if piece == PIECES["N"] if side == SIDES["white"] else piece == PIECES["n"]:
            #     # Loop over source squares of piece bitboard
            #     while bitboard:
            #         source_square = Bit.get_least_significant_first_bit(bitboard)

            #         # Initialize piece attacks in order to get the set of target squares
            #         attacks = knight_attack_table[source_square] & (
            #             ~occupancies[SIDES["white"]]
            #             if side == SIDES["white"]
            #             else ~occupancies[SIDES["black"]]
            #         )

            #         # Loop over the target squares available from generated attacks
            #         while attacks:
            #             target_square = Bit.get_least_significant_first_bit(attacks)

            #             # Quiet moves
            #             if not Bit.get_bit(
            #                 occupancies[SIDES["black"]]
            #                 if side == SIDES["white"]
            #                 else occupancies[SIDES["white"]],
            #                 target_square,
            #             ):
            #                 move_parameters = MoveParameters(
            #                     source_square, target_square, piece, 0, 0, 0, 0, 0
            #                 )
            #                 moves.add_move(Codec.get_encoded_move(move_parameters))

            #             # Capture moves
            #             else:
            #                 move_parameters = MoveParameters(
            #                     source_square, target_square, piece, 0, 1, 0, 0, 0
            #                 )
            #                 moves.add_move(Codec.get_encoded_move(move_parameters))

            #             attacks = Bit.pop_bit(attacks, target_square)

            #         bitboard = Bit.pop_bit(bitboard, source_square)

            # # Generate bishop moves
            # if piece == PIECES["B"] if side == SIDES["white"] else piece == PIECES["b"]:
            #     # Loop over source squares of piece bitboard
            #     while bitboard:
            #         source_square = Bit.get_least_significant_first_bit(bitboard)

            #         # Initialize piece attacks in order to get the set of target squares
            #         attacks = Attack.get_bishop_attack_masks(
            #             source_square,
            #             occupancies[SIDES["all"]],
            #             bishop_attack_table,
            #             bishop_attack_masks,
            #         ) & (
            #             ~occupancies[SIDES["white"]]
            #             if side == SIDES["white"]
            #             else ~occupancies[SIDES["black"]]
            #         )

            #         # Loop over the target squares available from generated attacks
            #         while attacks:
            #             target_square = Bit.get_least_significant_first_bit(attacks)

            #             # Quiet moves
            #             if not Bit.get_bit(
            #                 occupancies[SIDES["black"]]
            #                 if side == SIDES["white"]
            #                 else occupancies[SIDES["white"]],
            #                 target_square,
            #             ):
            #                 move_parameters = MoveParameters(
            #                     source_square, target_square, piece, 0, 0, 0, 0, 0
            #                 )
            #                 moves.add_move(Codec.get_encoded_move(move_parameters))

            #             # Capture moves
            #             else:
            #                 move_parameters = MoveParameters(
            #                     source_square, target_square, piece, 0, 1, 0, 0, 0
            #                 )
            #                 moves.add_move(Codec.get_encoded_move(move_parameters))

            #             attacks = Bit.pop_bit(attacks, target_square)

            #         bitboard = Bit.pop_bit(bitboard, source_square)

            # Generate rook moves
            if piece == PIECES["R"] if side == SIDES["white"] else piece == PIECES["r"]:
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
                            move_parameters = MoveParameters(
                                source_square, target_square, piece, 0, 0, 0, 0, 0
                            )
                            moves.add_move(Codec.get_encoded_move(move_parameters))

                        # Capture moves
                        else:
                            move_parameters = MoveParameters(
                                source_square, target_square, piece, 0, 1, 0, 0, 0
                            )
                            moves.add_move(Codec.get_encoded_move(move_parameters))

                        attacks = Bit.pop_bit(attacks, target_square)

                    bitboard = Bit.pop_bit(bitboard, source_square)

            # # Generate queen moves
            # if piece == PIECES["Q"] if side == SIDES["white"] else piece == PIECES["q"]:
            #     # Loop over source squares of piece bitboard
            #     while bitboard:
            #         source_square = Bit.get_least_significant_first_bit(bitboard)

            #         # Initialize piece attacks in order to get the set of target squares
            #         attacks = Attack.get_queen_attack_masks(
            #             source_square,
            #             occupancies[SIDES["all"]],
            #             attack_tables,
            #             attack_masks,
            #         ) & (
            #             ~occupancies[SIDES["white"]]
            #             if side == SIDES["white"]
            #             else ~occupancies[SIDES["black"]]
            #         )

            #         # Loop over the target squares available from generated attacks
            #         while attacks:
            #             target_square = Bit.get_least_significant_first_bit(attacks)

            #             # Quiet moves
            #             if not Bit.get_bit(
            #                 occupancies[SIDES["black"]]
            #                 if side == SIDES["white"]
            #                 else occupancies[SIDES["white"]],
            #                 target_square,
            #             ):
            #                 move_parameters = MoveParameters(
            #                     source_square, target_square, piece, 0, 0, 0, 0, 0
            #                 )
            #                 moves.add_move(Codec.get_encoded_move(move_parameters))

            #             # Capture moves
            #             else:
            #                 move_parameters = MoveParameters(
            #                     source_square, target_square, piece, 0, 1, 0, 0, 0
            #                 )
            #                 moves.add_move(Codec.get_encoded_move(move_parameters))

            #             attacks = Bit.pop_bit(attacks, target_square)

            #         bitboard = Bit.pop_bit(bitboard, source_square)

            # # Generate king moves
            # if piece == PIECES["K"] if side == SIDES["white"] else piece == PIECES["k"]:
            #     # Loop over source squares of piece bitboard
            #     while bitboard:
            #         source_square = Bit.get_least_significant_first_bit(bitboard)

            #         # Initialize piece attacks in order to get the set of target squares
            #         attacks = king_attack_table[source_square] & (
            #             ~occupancies[SIDES["white"]]
            #             if side == SIDES["white"]
            #             else ~occupancies[SIDES["black"]]
            #         )

            #         # Loop over the target squares available from generated attacks
            #         while attacks:
            #             target_square = Bit.get_least_significant_first_bit(attacks)

            #             # Quiet moves
            #             if not Bit.get_bit(
            #                 occupancies[SIDES["black"]]
            #                 if side == SIDES["white"]
            #                 else occupancies[SIDES["white"]],
            #                 target_square,
            #             ):
            #                 move_parameters = MoveParameters(
            #                     source_square, target_square, piece, 0, 0, 0, 0, 0
            #                 )
            #                 moves.add_move(Codec.get_encoded_move(move_parameters))

            #             # Capture moves
            #             else:
            #                 move_parameters = MoveParameters(
            #                     source_square, target_square, piece, 0, 1, 0, 0, 0
            #                 )
            #                 moves.add_move(Codec.get_encoded_move(move_parameters))

            #             attacks = Bit.pop_bit(attacks, target_square)

            #         bitboard = Bit.pop_bit(bitboard, source_square)

        return moves
