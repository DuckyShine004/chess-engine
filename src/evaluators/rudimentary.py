from src.utilities.bit import Bit

from src.constants.piece_constants import SIDES, PIECES
from src.constants.board_constants import NUMBER_OF_BITBOARDS

from src.constants.evaluation_constants import (
    MATERIAL_SCORES,
    PAWN_SCORES,
    KNIGHT_SCORES,
    BISHOP_SCORES,
    ROOK_SCORES,
    KING_SCORES,
    MIRROR_SCORES,
)


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
                score += MATERIAL_SCORES[piece]

                # score positional piece scores
                match piece:
                    case piece if piece == PIECES["P"]:
                        score += PAWN_SCORES[square]
                    case piece if piece == PIECES["N"]:
                        score += KNIGHT_SCORES[square]
                    case piece if piece == PIECES["B"]:
                        score += BISHOP_SCORES[square]
                    case piece if piece == PIECES["R"]:
                        score += ROOK_SCORES[square]
                    case piece if piece == PIECES["K"]:
                        score += KING_SCORES[square]
                    case piece if piece == PIECES["p"]:
                        score -= PAWN_SCORES[MIRROR_SCORES[square]]
                    case piece if piece == PIECES["n"]:
                        score -= KNIGHT_SCORES[MIRROR_SCORES[square]]
                    case piece if piece == PIECES["b"]:
                        score -= BISHOP_SCORES[MIRROR_SCORES[square]]
                    case piece if piece == PIECES["r"]:
                        score -= ROOK_SCORES[MIRROR_SCORES[square]]
                    case piece if piece == PIECES["k"]:
                        score -= KING_SCORES[MIRROR_SCORES[square]]

                # Decrement least significant first bit
                bitboard = Bit.pop_bit(bitboard, square)

        return score if app.bitboard_manager.side == SIDES["white"] else -score
