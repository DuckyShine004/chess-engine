from src.lookup.piece_lookup import SIDES, PIECES


class Attacked:
    @staticmethod
    def check_square_attacked(app, square, side):
        if Attacked.check_leaper_squares_attacked(app, square, side):
            return True

        if Attacked.check_slider_squares_attacked(app, square, side):
            return True

        return False

    @staticmethod
    def check_leaper_squares_attacked(app, square, side):
        if Attacked.check_square_attacked_by_pawns(app, square, side):
            return True

        return False

    @staticmethod
    def check_slider_squares_attacked(app, square, side):
        ...

    @staticmethod
    def check_square_attacked_by_pawns(app, square, side):
        attack_mask = 0
        bitboard = 0

        if side == SIDES["white"]:
            attack_mask = app.table_manager.pawn_attack_table[SIDES["white"]][square]
            bitboard = app.bitboard_manager.bitboards[PIECES["P"]]
        else:
            attack_mask = app.table_manager.pawn_attack_table[SIDES["black"]][square]
            bitboard = app.bitboard_manager.bitboards[PIECES["p"]]

        return attack_mask & bitboard
