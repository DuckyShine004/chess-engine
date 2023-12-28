from src.generator.move_generator import MoveGenerator

from src.routines.codec import Codec

from src.constants.piece_constants import PIECES
from src.constants.board_constants import COORDINATES


class MoveParser:
    def __init__(self, app):
        self.move_generator = MoveGenerator(app)
        self.moves = self.move_generator.get_moves()

        self.source_square = 0
        self.target_square = 0

    def parse(self, move_string):
        self.parse_squares(move_string)

        for move_count in range(self.moves.count):
            move = self.moves.moves[move_count]

            if not self.check_valid_move(move, move_string):
                continue

            return move

        return 0

    def parse_squares(self, move_string):
        self.source_square = (ord(move_string[0]) - ord("a")) + (8 - int(move_string[1])) * 8
        self.target_square = (ord(move_string[2]) - ord("a")) + (8 - int(move_string[3])) * 8

    def check_valid_source_square(self, move):
        return self.source_square == Codec.get_decoded_source_square(move)

    def check_valid_target_square(self, move):
        return self.target_square == Codec.get_decoded_target_square(move)

    def check_valid_squares(self, move):
        if not self.check_valid_source_square(move):
            return False

        if not self.check_valid_target_square(move):
            return False

        return True

    def check_valid_promotion_move(self, move, move_string):
        promotion_piece = Codec.get_decoded_promotion_piece(move)

        if not promotion_piece:
            return True

        if len(move_string) <= 4:
            return False

        return self.check_valid_promotion_piece(promotion_piece, move_string[4])

    def check_valid_promotion_piece(self, promotion_piece, promotion_character):
        if (promotion_piece in (PIECES["Q"], PIECES["q"])) and promotion_character == "q":
            return True

        if (promotion_piece in (PIECES["R"], PIECES["r"])) and promotion_character == "r":
            return True

        if (promotion_piece in (PIECES["B"], PIECES["b"])) and promotion_character == "b":
            return True

        if (promotion_piece in (PIECES["N"], PIECES["n"])) and promotion_character == "n":
            return True

        return False

    def check_valid_move(self, move, move_string):
        return self.check_valid_squares(move) & self.check_valid_promotion_move(move, move_string)
