from src.routines.codec import Codec

from src.utilities.bit import Bit

from src.constants.piece_constants import SIDES, PIECES
from src.constants.board_constants import MOVE_TYPES


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

            if Codec.get_decoded_capture_flag(move):
                start_piece = PIECES["p"] if self.manager.side == SIDES["white"] else PIECES["P"]
                end_piece = PIECES["k"] if self.manager.side == SIDES["white"] else PIECES["K"]

                for piece in range(start_piece, end_piece + 1):
                    # If there is a piece on the target square, we just remove it from the corresponding bitboard
                    if Bit.get_bit(self.manager.bitboards[piece], self.target_square):
                        self.manager.bitboards[piece] = Bit.pop_bit(
                            self.manager.bitboards[piece], self.target_square
                        )
                        break
        # Capture moves
        else:
            # Enusure that the move is a capture
            if Codec.get_decoded_capture_flag(move):
                self.make_move(move, MOVE_TYPES["all"])

            else:
                # Otherwise, the move is not a capture
                return 0
