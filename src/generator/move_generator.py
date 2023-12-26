from src.generator.pieces.pawn import Pawn
from src.generator.pieces.king import King
from src.generator.pieces.rook import Rook
from src.generator.pieces.knight import Knight
from src.generator.pieces.bishop import Bishop

from src.data_structures.moves import Moves
from src.data.parameters.move_parameters import MoveParameters

from src.constants.piece_constants import SIDES, PIECES
from src.constants.board_constants import NUMBER_OF_BITBOARDS


class MoveGenerator:
    def __init__(self, app):
        self.app = app

        self.bitboards = app.bitboard_manager.bitboards
        self.side = app.bitboard_manager.side

        self.moves = Moves()
        self.move_parameters = MoveParameters(0, 0, 0, 0, 0, 0, 0, 0)

        self.pawn = Pawn(self, app)
        self.king = King(self, app)
        self.rook = Rook(self, app)
        self.knight = Knight(self, app)
        self.bishop = Bishop(self, app)

    def get_moves(self):
        for piece in range(NUMBER_OF_BITBOARDS):
            bitboard = self.bitboards[piece]

            self.move_parameters.piece = piece

            # self.get_pawn_moves(bitboard, piece)
            # self.get_king_moves(bitboard, piece)
            self.get_rook_moves(bitboard, piece)
            # self.get_knight_moves(bitboard, piece)
            # self.get_bishop_moves(bitboard, piece)

        return self.moves

    def get_pawn_moves(self, bitboard, piece):
        if piece == PIECES["P"] if self.side == SIDES["white"] else piece == PIECES["p"]:
            self.pawn.generate_moves(bitboard)

    def get_king_moves(self, bitboard, piece):
        if piece == PIECES["K"] if self.side == SIDES["white"] else piece == PIECES["k"]:
            self.king.generate_moves(bitboard)

    def get_rook_moves(self, bitboard, piece):
        if piece == PIECES["R"] if self.side == SIDES["white"] else piece == PIECES["r"]:
            self.rook.generate_moves(bitboard)

    def get_knight_moves(self, bitboard, piece):
        if piece == PIECES["N"] if self.side == SIDES["white"] else piece == PIECES["n"]:
            self.knight.generate_moves(bitboard)

    def get_bishop_moves(self, bitboard, piece):
        if piece == PIECES["B"] if self.side == SIDES["white"] else piece == PIECES["b"]:
            self.bishop.generate_moves(bitboard)
