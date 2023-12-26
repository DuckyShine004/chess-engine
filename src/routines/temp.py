from src.data_structures.moves import Moves
from src.data.parameters.move_parameters import MoveParameters

from src.routines.codec import Codec
from src.routines.attacked import Attacked

from src.utilities.bit import Bit
from src.utilities.attack import Attack

from src.constants.piece_constants import SIDES, PIECES, CASTLE
from src.constants.board_constants import NUMBER_OF_BITBOARDS, SQUARES, COORDINATES


class Move:
    # def __init__(self, bitboards):
    #     self.bitboards = bitboards
    def __init__(self, app):
        # TODO annotate class
        self.app = app

        self.moves = Moves()
        self.move_parameters = MoveParameters()

        self.initialize_manager_attributes()

    def initialize_manager_attributes(self):
        self.initialize_bitboard_manager_attributes()
        self.initialize_table_manager_attributes()

    def initialize_bitboard_manager_attributes(self):
        self.bitboard_manager = self.app.bitboard_manager

        self.bitboards = self.app.bitboard_manager.bitboards
        self.occupancies = self.app.bitboard_manager.occupancies
        self.side = self.app.bitboard_manager.side
        self.enpassant = self.app.bitboard_manager.enpassant
        self.castle = self.app.bitboard_manager.castle

    def initialize_table_manager_attributes(self):
        self.table_manager = self.app.table_manager

        self.pawn_attack_table = self.app.table_manager.pawn_attack_table
        self.knight_attack_table = self.app.table_manager.knight_attack_table
        self.bishop_attack_table = self.app.table_manager.bishop_attack_table
        self.bishop_attack_masks = self.app.table_manager.bishop_attack_masks
        self.rook_attack_table = self.app.table_manager.rook_attack_table
        self.rook_attack_masks = self.app.table_manager.rook_attack_masks
        self.king_attack_table = self.app.table_manager.king_attack_table

        self.attack_tables = (self.bishop_attack_table, self.rook_attack_table)
        self.attack_masks = (self.bishop_attack_masks, self.rook_attack_masks)

    def get_moves(self):
        for piece in range(NUMBER_OF_BITBOARDS):
            bitboard = self.bitboards[piece]

            self.move_parameters.piece = piece

            self.add_quiet_pawn_moves(piece, bitboard)

        return self.moves

    def add_quiet_pawn_moves(self, piece, bitboard):
        if self.side == "white" and piece == "P":
            self.add_quiet_white_pawn_moves(bitboard)

        if self.side == "black" and piece == "p":
            self.add_quiet_black_pawn_moves(bitboard)

    def add_quiet_white_pawn_moves(self, bitboard):
        while bitboard:
            source_square = Bit.get_least_significant_first_bit(bitboard)
            target_square = source_square - 8

            self.move_parameters.source_square = source_square
            self.move_parameters.target_square = target_square

            self.generate_white_pawn_promotion_moves(source_square, target_square)
            self.generate_white_pawn_capture_moves(source_square)
            self.generate_white_pawn_enpassant_moves(source_square)

            bitboard = Bit.pop_bit(bitboard, source_square)

    def add_single_white_pawn_push_move(self):
        self.moves.add_move(Codec.get_encoded_move(self.move_parameters))

    def add_double_white_pawn_push_move(self, source_square, target_square):
        if not SQUARES["a2"] <= source_square <= SQUARES["h2"]:
            return

        if Bit.get_bit(self.occupancies[SIDES["all"]], target_square):
            return

        self.move_parameters.target_square = target_square
        self.move_parameters.double_pawn_push_flag = 1
        self.moves.add_move(Codec.get_encoded_move(self.move_parameters))

        self.reset_move_parameters()

    def add_white_pawn_capture_move(self):
        self.move_parameters.capture_flag = 1
        self.moves.add_move(Codec.get_encoded_move(self.move_parameters))

        self.reset_move_parameters()

    def add_white_pawn_promotion_move(self, promotion_piece):
        self.move_parameters.promotion_piece = promotion_piece
        self.moves.add_move(Codec.get_encoded_move(self.move_parameters))

        self.reset_move_parameters()

    def add_white_pawn_promotion_capture_move(self, promotion_piece):
        self.move_parameters.promotion_piece = promotion_piece
        self.move_parameters.capture_flag = 1
        self.moves.add_move(Codec.get_encoded_move(self.move_parameters))

        self.reset_move_parameters()

    def add_white_pawn_enpassant_move(self, enpassant_square):
        self.move_parameters.target_square = enpassant_square
        self.move_parameters.capture_flag = 1
        self.move_parameters.enpassant_flag = 1
        self.moves.add_move(Codec.get_encoded_move(self.move_parameters))

        self.reset_move_parameters()

    def generate_white_pawn_promotion_moves(self, source_square, target_square):
        if target_square < SQUARES["a8"]:
            return

        if Bit.get_bit(self.occupancies[SIDES["all"]], target_square):
            return

        if SQUARES["a7"] <= source_square <= SQUARES["h7"]:
            self.add_white_pawn_promotion_move(PIECES["Q"])
            self.add_white_pawn_promotion_move(PIECES["R"])
            self.add_white_pawn_promotion_move(PIECES["B"])
            self.add_white_pawn_promotion_move(PIECES["N"])
        else:
            self.add_single_white_pawn_push_move()
            self.add_double_white_pawn_push_move(source_square, target_square - 8)

    def generate_white_pawn_capture_moves(self, source_square):
        # self.side ^ 1
        attacks = self.pawn_attack_table[self.side][source_square] & self.occupancies[SIDES["black"]]

        while attacks:
            target_square = Bit.get_least_significant_first_bit(attacks)

            self.move_parameters.target_square = target_square

            self.generate_white_pawn_promotion_capture_moves(source_square, target_square)

            attacks = Bit.pop_bit(attacks, target_square)

    def generate_white_pawn_promotion_capture_moves(self, source_square, target_square):
        if SQUARES["a7"] <= source_square <= SQUARES["h7"]:
            self.add_white_pawn_promotion_capture_move(PIECES["Q"])
            self.add_white_pawn_promotion_capture_move(PIECES["R"])
            self.add_white_pawn_promotion_capture_move(PIECES["B"])
            self.add_white_pawn_promotion_capture_move(PIECES["N"])
        else:
            self.add_white_pawn_capture_move()

    def generate_white_pawn_enpassant_moves(self, source_square):
        if self.enpassant == SQUARES["null"]:
            return

        offset = Bit.left_shift(1, self.enpassant)
        enpassant_attacks = self.pawn_attack_table[self.side][source_square] & offset

        if not enpassant_attacks:
            return

        enpassant_square = Bit.get_least_significant_first_bit(enpassant_attacks)

        self.add_white_pawn_enpassant_move(enpassant_square)

    def reset_move_parameters(self):
        self.move_parameters.promotion_piece = 0
        self.move_parameters.capture_flag = 0
        self.move_parameters.double_pawn_push_flag = 0
        self.move_parameters.enpassant_flag = 0
        self.move_parameters.castling_flag = 0
