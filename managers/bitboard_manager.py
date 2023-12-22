from src.utilities.bit import Bit
from src.utilities.console import Console

from src.parsers.fen_parser import FenParser

from src.lookup.board_lookup import SQUARES
from src.lookup.piece_lookup import PIECES, SIDES


class BitboardManager:
    def __init__(self):
        self.reset()

    def reset(self):
        self.bitboards = [0] * 12
        self.occupancies = [0] * 3
        self.side = 0
        self.enpassant = SQUARES["null"]
        self.castle = 0

    def parse_fen(self, fen):
        parser = FenParser(self)
        parser.parse(fen)

    def set_bitboard(self, square, ascii_piece):
        board_index = PIECES[ascii_piece]
        self.bitboards[board_index] = Bit.set_bit(self.bitboards[board_index], square)

    def initialize_occupancies(self):
        for board_index in range(PIECES["P"], PIECES["K"] + 1):
            self.occupancies[SIDES["white"]] |= self.bitboards[board_index]

        for board_index in range(PIECES["p"], PIECES["k"] + 1):
            self.occupancies[SIDES["black"]] |= self.bitboards[board_index]

        self.occupancies[SIDES["all"]] |= self.occupancies[SIDES["white"]]
        self.occupancies[SIDES["all"]] |= self.occupancies[SIDES["black"]]

    def print_board(self):
        Console.print_board(self.bitboards, self.enpassant, self.castle, self.side)
