from src.lookup.piece_lookup import SIDES, PIECES


class Attacked:
    @staticmethod
    def check_squares_attacked(app, square, side):
        if Attacked.check_leaper_squares_attacked(app, square, side):
            return True

        if Attacked.check_slider_squares_attacked(app, square, side):
            return True

        return False

    @staticmethod
    def check_leaper_squares_attacked(app, square, side):
        if Attacked.check_squares_attacked_by_leaper_pieces(app, square, side, "P"):
            return True

        if Attacked.check_squares_attacked_by_leaper_pieces(app, square, side, "N"):
            return True

        if Attacked.check_squares_attacked_by_leaper_pieces(app, square, side, "K"):
            return True

        return False

    @staticmethod
    def check_slider_squares_attacked(app, square, side):
        if Attacked.check_squares_attacked_by_bishops(app, square, side):
            return True

        if Attacked.check_squares_attacked_by_rooks(app, square, side):
            return True

        if Attacked.check_squares_attacked_by_queens(app, square, side):
            return True

        return False

    @staticmethod
    def check_squares_attacked_by_leaper_pieces(app, square, side, piece):
        attack_mask = Attacked.get_attack_mask(app, square, side)
        bitboard = Attacked.get_bitboard(app, side, piece)

        return attack_mask & bitboard

    @staticmethod
    def check_squares_attacked_by_bishops(app, square, side):
        ...

    @staticmethod
    def get_attack_mask(app, square, side):
        return app.table_manager.pawn_attack_table[side][square]

    @staticmethod
    def get_bitboard(app, side, piece):
        if side == SIDES["white"]:
            return app.bitboard_manager.bitboards[PIECES[piece]]

        piece = piece.lower()

        return app.bitboard_manager.bitboards[PIECES[piece]]
