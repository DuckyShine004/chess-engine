from src.utilities.bit import Bit

from src.lookup.piece_lookup import CASTLE
from src.lookup.board_lookup import SQUARES

from src.constants.board_constants import NUMBER_OF_BITBOARDS


class FenParser:
    def __init__(self, bitboard_manager):
        self.manager = bitboard_manager

    def parse(self, fen):
        self.manager.reset()

        position = self.parse_pieces(fen)
        position = self.parse_side_to_move(fen, position)

        # Parse castling rights
        position += 2
        while fen[position] != " ":
            self.manager.castle |= CASTLE[fen[position]]
            position += 1

        # Parse enpassant square
        position += 1
        if fen[position] != "-":
            file = int(fen[position])
            rank = 8 - int(fen[position + 1])

            self.manager.enpassant = file + rank * 8
        else:
            self.manager.enpassant = SQUARES["null"]

        # fen_position = self.parse_castling_rights(fen, fen_position)
        # self.parse_enpassant_square(fen, fen_position)

    def parse_pieces(self, fen):
        position = 0

        for rank in range(8):
            file = 0

            while file < 8:
                square = file + rank * 8
                file, position = self.handle_fen_position(fen, square, file, position)

        return position

    def parse_side_to_move(self, fen, position):
        position += 1
        self.manager.side = fen[position] == "b"

        return position

    def parse_castling_rights(self, fen, position):
        position += 2
        while fen[position] != " ":
            self.manager.castle |= CASTLE[fen[position]]
            position += 1

        return fen_position + 1

    def parse_enpassant_square(self, fen, fen_position):
        if fen[fen_position] != "-":
            file = ord(fen[fen_position]) - ord("a")
            rank = 8 - (ord(fen[fen_position + 1]) - ord("0"))
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
        position = self.handle_fen_rank_break(fen, square, position)

        return file + 1, position

    def handle_fen_alpha(self, fen, square, position):
        if not fen[position].isalpha():
            return position

        self.manager.set_bitboard(square, fen[position])

        return position + 1

    def handle_fen_digit(self, fen, square, file, position):
        if not fen[position].isdigit():
            return file, position

        offset = int(fen[position])

        if self.check_empty_square(square):
            file -= 1

        file += offset

        return file, position + 1

    def handle_fen_rank_break(self, fen, square, position):
        if not fen[position] == "/":
            return position

        return position + 1
