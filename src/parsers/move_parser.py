from src.generator.move_generator import MoveGenerator

from src.routines.codec import Codec

from src.constants.piece_constants import PIECES
from src.constants.board_constants import COORDINATES


class MoveParser:
    def __init__(self, app):
        self.move_generator = MoveGenerator(app)
        self.moves = self.move_generator.get_moves()

    def parse(self, move_string):
        source_square = (ord(move_string[0]) - ord("a")) + (8 - int(move_string[1])) * 8
        target_square = (ord(move_string[2]) - ord("a")) + (8 - int(move_string[3])) * 8

        promotion_piece = 0

        for move_count in range(self.moves.count):
            move = self.moves.moves[move_count]

            # Make sure source square and target square are available within the generated moves
            if source_square == Codec.get_decoded_source_square(
                move
            ) and target_square == Codec.get_decoded_target_square(move):
                promotion_piece = Codec.get_decoded_promotion_piece(move)

                if promotion_piece:
                    if len(move_string) <= 4:
                        return 0

                    if (promotion_piece in (PIECES["Q"], PIECES["q"])) and move_string[4] == "q":
                        return move

                    if (promotion_piece in (PIECES["R"], PIECES["r"])) and move_string[4] == "r":
                        return move

                    if (promotion_piece in (PIECES["B"], PIECES["b"])) and move_string[4] == "b":
                        return move

                    if (promotion_piece in (PIECES["N"], PIECES["n"])) and move_string[4] == "n":
                        return move

                    continue

                # Return legal move
                return move

        # The move is illegal
        return 0
