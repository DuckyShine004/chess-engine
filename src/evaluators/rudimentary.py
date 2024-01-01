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
    def get_evaluation(app):
        score = 0

        for piece in range(NUMBER_OF_BITBOARDS):
            bitboard = app.bitboard_manager.bitboards[piece]
            score = Rudimentary.evaluate_board(bitboard, piece, score)

        return score if app.bitboard_manager.side == SIDES["white"] else -score

    @staticmethod
    def evaluate_board(bitboard, piece, score):
        while bitboard:
            square = Bit.get_least_significant_first_bit(bitboard)

            score = Rudimentary.evaluate_material(piece, score)
            score = Rudimentary.evaluate_position(square, piece, score)

            bitboard = Bit.pop_bit(bitboard, square)

        return score

    @staticmethod
    def evaluate_material(piece, score):
        return score + MATERIAL_SCORES[piece]

    @staticmethod
    def evaluate_position(square, piece, score):
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

        return score
