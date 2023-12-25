from src.utilities.bit import Bit
from src.utilities.console import Console

from src.parsers.fen_parser import FenParser

from src.constants.piece_constants import PIECES
from src.constants.board_constants import ALL_SIDES, NUMBER_OF_BITBOARDS, SQUARES


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

    def parse_fen(self, fen):
        parser = FenParser(self)
        parser.parse(fen)

    def set_bitboard(self, square, piece_index):
        board_index = PIECES[piece_index]
        self.bitboards[board_index] = Bit.set_bit(self.bitboards[board_index], square)

    def print_board(self):
        Console.print_board(self.bitboards, self.enpassant, self.castle, self.side)
