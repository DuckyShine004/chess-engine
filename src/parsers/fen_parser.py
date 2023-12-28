from src.utilities.bit import Bit

from src.constants.piece_constants import CASTLE, PIECES, SIDES
from src.constants.board_constants import NUMBER_OF_BITBOARDS, SQUARES


class FenParser:
    def __init__(self, manager):
        self.manager = manager

    def initialize_occupancies(self):
        for board_index in range(PIECES["P"], PIECES["K"] + 1):
            self.manager.occupancies[SIDES["white"]] |= self.manager.bitboards[board_index]

        for board_index in range(PIECES["p"], PIECES["k"] + 1):
            self.manager.occupancies[SIDES["black"]] |= self.manager.bitboards[board_index]

        self.manager.occupancies[SIDES["all"]] |= self.manager.occupancies[SIDES["white"]]
        self.manager.occupancies[SIDES["all"]] |= self.manager.occupancies[SIDES["black"]]

    def parse(self, fen):
        self.manager.reset()

        position = self.parse_pieces(fen)
        position = self.parse_side_to_move(fen, position)
        position = self.parse_castling_rights(fen, position)

        self.parse_enpassant_square(fen, position)
        self.initialize_occupancies()

    def parse_pieces(self, fen):
        position = 0

        for rank in range(8):
            file = 0

            while file < 8:
                square = file + rank * 8
                file, position = self.handle_fen_position(fen, square, file, position)

        return position + 1

    def parse_side_to_move(self, fen, position):
        self.manager.side = fen[position] == "b"

        return position + 2

    def parse_castling_rights(self, fen, position):
        while fen[position] != " ":
            self.manager.castle |= CASTLE.get(fen[position], 0)
            position += 1

        return position + 1

    def parse_enpassant_square(self, fen, position):
        if fen[position] != "-":
            file = ord(fen[position]) - ord("a")
            rank = 8 - int(fen[position + 1])
            self.manager.enpassant = file + rank * 8
        else:
            self.manager.enpassant = SQUARES["null"]

    def check_empty_square(self, square):
        for board_index in range(NUMBER_OF_BITBOARDS):
            if Bit.get_bit(self.manager.bitboards[board_index], square):
                return False

        return True

    def handle_fen_position(self, fen, square, file, position):
        position = self.handle_fen_alpha(fen, square, position)
        file, position = self.handle_fen_digit(fen, square, file, position)
        position = self.handle_fen_rank_break(fen, position)

        return file + 1, position

    def handle_fen_alpha(self, fen, square, position):
        if not fen[position].isalpha():
            return position

        self.manager.set_bitboard(square, fen[position])

        return position + 1

    def handle_fen_digit(self, fen, square, file, position):
        if not fen[position].isdigit():
            return file, position

        file_offset = int(fen[position])

        if self.check_empty_square(square):
            file -= 1

        file += file_offset

        return file, position + 1

    def handle_fen_rank_break(self, fen, position):
        if not fen[position] == "/":
            return position

        return position + 1
