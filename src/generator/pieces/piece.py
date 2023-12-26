from src.routines.codec import Codec


class Piece:
    def __init__(self, move_generator, app):
        self.app = app
        self.move_generator = move_generator
        self.moves = move_generator.moves
        self.move_parameters = move_generator.move_parameters

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

    def add_move(self):
        self.moves.add_move(Codec.get_encoded_move(self.move_parameters))

    def reset_move_parameters(self):
        self.move_parameters.promotion_piece = 0
        self.move_parameters.capture_flag = 0
        self.move_parameters.double_pawn_push_flag = 0
        self.move_parameters.enpassant_flag = 0
        self.move_parameters.castling_flag = 0
