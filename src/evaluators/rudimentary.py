from src.utilities.bit import Bit

from src.constants.piece_constants import SIDES, MATERIAL_SCORE
from src.constants.board_constants import NUMBER_OF_BITBOARDS


class Rudimentary:
    @staticmethod
    def evaluate(app):
        score = 0

        for piece in range(NUMBER_OF_BITBOARDS):
            bitboard = app.bitboard_manager.bitboards[piece]

            # Loop over the pieces within a bitboard
            while bitboard:
                square = Bit.get_least_significant_first_bit(bitboard)

                # Get the current material's score
                score += MATERIAL_SCORE[piece]

                # Decrement least significant first bit
                bitboard = Bit.pop_bit(bitboard, square)

        return score if app.bitboard_manager.side == SIDES["white"] else -score
