from src.utilities.bit import Bit
from src.utilities.console import Console

from src.lookup.piece_lookup import PIECES, SIDES, CASTLE
from src.lookup.board_lookup import SQUARES

from src.constants.board_constants import NUMBER_OF_BITBOARDS


class BitboardManager:
    def __init__(self):
        self.reset()

    def reset(self):
        self.bitboards = [0] * 12
        self.occupancies = [0] * 3
        self.side = 0
        self.enpassant = SQUARES["NULL_SQUARE"]
        self.castle = 0

    def parse_fen(self, fen):
        self.reset()
        idx = 0

        # Parse bit pieces
        for rank in range(8):
            file = 0

            while file < 8:
                square = file + rank * 8

                if fen[idx].isalpha():
                    self.set_bitboard(square, fen[idx])
                    idx += 1

                if fen[idx].isdigit():
                    offset = ord(fen[idx]) - ord("0")
                    piece = -1

                    for bitboard_piece in range(NUMBER_OF_BITBOARDS):
                        if Bit.get_bit(self.bitboards[bitboard_piece], square):
                            piece = bitboard_piece

                    if piece == -1:
                        file -= 1

                    file += offset
                    idx += 1

                if fen[idx] == "/":
                    idx += 1

                file += 1

        # Parse the side to move
        idx += 1
        self.side = fen[idx] == "b"

        # Parse castling rights
        idx += 2
        while fen[idx] != ' ':
            match (fen[idx]):
                case 'K':
                    self.castle |= CASTLE["white_king_side"]
                case 'Q':
                    self.castle |= CASTLE["white_queen_side"]
                case 'k':
                    self.castle |= CASTLE["black_king_side"]
                case 'q':
                    self.castle |= CASTLE["black_queen_side"]

            idx += 1

        # Parse enpassant square
        idx += 1
        if fen[idx] != '-':
            file = ord(fen[idx]) - ord('a')
            rank = 8 - (ord(fen[idx + 1]) - ord('0'))

            self.enpassant = file + rank * 8
        else:
            self.enpassant = SQUARES["NULL_SQUARE"]

    def set_bitboard(self, square, ascii_piece):
        piece = PIECES[ascii_piece]
        self.bitboards[piece] = Bit.set_bit(self.bitboards[piece], square)

    def print_board(self):
        Console.print_board(self.bitboards, self.enpassant, self.castle, self.side)
