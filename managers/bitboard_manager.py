from src.routines.codec import Codec

from src.utilities.bit import Bit
from src.utilities.console import Console

from src.parsers.fen_parser import FenParser

from src.constants.piece_constants import PIECES
from src.constants.board_constants import ALL_SIDES, NUMBER_OF_BITBOARDS, SQUARES, MOVE_TYPES


class BitboardManager:
    def __init__(self, app):
        self.app = app

        self.reset()

    def reset(self):
        self.bitboards = [0] * NUMBER_OF_BITBOARDS
        self.occupancies = [0] * ALL_SIDES
        self.side = 0
        self.enpassant = SQUARES["null"]
        self.castle = 0

    def make_move(self, move, move_type):
        # Quiet moves
        if move_type == MOVE_TYPES["all"]:
            self.preserve_attributes()
            move_parameters = Codec.get_decoded_move_parameters(move)

            # Move the piece
            self.bitboards[move_parameters.piece] = Bit.pop_bit(
                self.bitboards[move_parameters.piece], move_parameters.source_square
            )
            self.bitboards[move_parameters.piece] = Bit.set_bit(
                self.bitboards[move_parameters.piece], move_parameters.target_square
            )
        # Capture moves
        else:
            # Enusure that the move is a capture
            if Codec.get_decoded_capture_flag(move):
                self.make_move(move, MOVE_TYPES["all"])

            else:
                # Otherwise, the move is not a capture
                return 0

    def preserve_attributes(self):
        self.preserved_bitboards = list(self.bitboards)
        self.preserved_occupancies = list(self.occupancies)
        self.preserved_side = self.side
        self.preserved_enpassant = self.enpassant
        self.preserved_castle = self.castle

    def set_attributes(self):
        self.bitboards = list(self.preserved_bitboards)
        self.occupancies = list(self.preserved_occupancies)
        self.side = self.preserved_side
        self.enpassant = self.preserved_enpassant
        self.castle = self.preserved_castle

    def parse_fen(self, fen):
        parser = FenParser(self)
        parser.parse(fen)

    def set_bitboard(self, square, piece_index):
        board_index = PIECES[piece_index]
        self.bitboards[board_index] = Bit.set_bit(self.bitboards[board_index], square)

    def print_board(self):
        Console.print_board(self.bitboards, self.enpassant, self.castle, self.side)
