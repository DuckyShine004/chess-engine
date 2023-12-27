from src.routines.codec import Codec

from src.utilities.bit import Bit

from src.constants.piece_constants import SIDES, PIECES, CASTLING_RIGHTS
from src.constants.board_constants import ALL_SIDES, SQUARES, MOVE_TYPES


class MoveManager:
    def __init__(self, manager):
        self.manager = manager

    def set_attributes_to_parameters(self, parameters):
        self.source_square = parameters.source_square
        self.target_square = parameters.target_square
        self.piece = parameters.piece
        self.promotion_piece = parameters.promotion_piece
        self.capture_flag = parameters.capture_flag
        self.double_pawn_push_flag = parameters.double_pawn_push_flag
        self.enpassant_flag = parameters.enpassant_flag
        self.castling_flag = parameters.castling_flag

    def make_move(self, move, move_type):
        # Quiet moves
        if move_type == MOVE_TYPES["all"]:
            self.manager.preserve_attributes()
            move_parameters = Codec.get_decoded_move_parameters(move)
            self.set_attributes_to_parameters(move_parameters)

            # Move the piece
            self.manager.bitboards[self.piece] = Bit.pop_bit(
                self.manager.bitboards[self.piece], self.source_square
            )
            self.manager.bitboards[self.piece] = Bit.set_bit(
                self.manager.bitboards[self.piece], self.target_square
            )

            # Handle captures
            if self.capture_flag:
                start_piece = PIECES["p"] if self.manager.side == SIDES["white"] else PIECES["P"]
                end_piece = PIECES["k"] if self.manager.side == SIDES["white"] else PIECES["K"]

                for piece in range(start_piece, end_piece + 1):
                    # If there is a piece on the target square, we just remove it from the corresponding bitboard
                    if Bit.get_bit(self.manager.bitboards[piece], self.target_square):
                        self.manager.bitboards[piece] = Bit.pop_bit(
                            self.manager.bitboards[piece], self.target_square
                        )
                        break

            # Handle pawn promotion
            if self.promotion_piece:
                pawn_piece = PIECES["P"] if self.manager.side == SIDES["white"] else PIECES["p"]

                # Remove the pawn from the target square
                self.manager.bitboards[pawn_piece] = Bit.pop_bit(
                    self.manager.bitboards[pawn_piece], self.target_square
                )

                # Set the new piece to the promotion piece
                self.manager.bitboards[self.promotion_piece] = Bit.set_bit(
                    self.manager.bitboards[self.promotion_piece], self.target_square
                )

            # Handle enpassant
            if self.enpassant_flag:
                # Remove the pawn depending on side to move
                pawn_piece = PIECES["p"] if self.manager.side == SIDES["white"] else PIECES["P"]
                offset = 8 if self.manager.side == SIDES["white"] else -8
                self.manager.bitboards[pawn_piece] = Bit.pop_bit(
                    self.manager.bitboards[pawn_piece], self.target_square + offset
                )

            self.manager.enpassant = SQUARES["null"]

            # Handle double pawn push
            if self.double_pawn_push_flag:
                if self.manager.side == SIDES["white"]:
                    self.manager.enpassant = self.target_square + 8
                else:
                    self.manager.enpassant = self.target_square - 8

            g1 = SQUARES["g1"]
            c1 = SQUARES["c1"]
            g8 = SQUARES["g8"]
            c8 = SQUARES["c8"]

            # Handle castling moves
            if self.castling_flag:
                match self.target_square:
                    # White king castles king side
                    case square if square == g1:
                        self.manager.bitboards[PIECES["R"]] = Bit.pop_bit(
                            self.manager.bitboards[PIECES["R"]], SQUARES["h1"]
                        )
                        self.manager.bitboards[PIECES["R"]] = Bit.set_bit(
                            self.manager.bitboards[PIECES["R"]], SQUARES["f1"]
                        )

                    # White king castles queen side
                    case square if square == c1:
                        self.manager.bitboards[PIECES["R"]] = Bit.pop_bit(
                            self.manager.bitboards[PIECES["R"]], SQUARES["a1"]
                        )
                        self.manager.bitboards[PIECES["R"]] = Bit.set_bit(
                            self.manager.bitboards[PIECES["R"]], SQUARES["d1"]
                        )

                    # Black king castles king side
                    case square if square == g8:
                        self.manager.bitboards[PIECES["r"]] = Bit.pop_bit(
                            self.manager.bitboards[PIECES["r"]], SQUARES["h8"]
                        )
                        self.manager.bitboards[PIECES["r"]] = Bit.set_bit(
                            self.manager.bitboards[PIECES["r"]], SQUARES["f8"]
                        )

                    # Black king castles queen side
                    case square if square == c8:
                        self.manager.bitboards[PIECES["r"]] = Bit.pop_bit(
                            self.manager.bitboards[PIECES["r"]], SQUARES["a8"]
                        )
                        self.manager.bitboards[PIECES["r"]] = Bit.set_bit(
                            self.manager.bitboards[PIECES["r"]], SQUARES["d8"]
                        )

            # Handle castling rights
            self.manager.castle &= CASTLING_RIGHTS[self.source_square]
            self.manager.castle &= CASTLING_RIGHTS[self.target_square]

            # Handle occupancy bitboards
            self.manager.occupancies = [0] * ALL_SIDES

            # Go through the white piece bitboards
            for piece in range(PIECES["P"], PIECES["K"] + 1):
                # Update white occupancies
                self.manager.occupancies[SIDES["white"]] |= self.manager.bitboards[piece]

            # Go through the black piece bitboards
            for piece in range(PIECES["p"], PIECES["k"] + 1):
                # Update white occupancies
                self.manager.occupancies[SIDES["black"]] |= self.manager.bitboards[piece]

            self.manager.occupancies[SIDES["all"]] = (
                self.manager.occupancies[SIDES["white"]] | self.manager.occupancies[SIDES["black"]]
            )

        # Capture moves
        else:
            # Enusure that the move is a capture
            if Codec.get_decoded_capture_flag(move):
                self.make_move(move, MOVE_TYPES["all"])

            else:
                # Otherwise, the move is not a capture
                return 0
