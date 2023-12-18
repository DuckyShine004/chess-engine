from src.lookup.board_lookup import SQUARES


class BitboardManager:
    def __init__(self):
        self.bitboards = [0] * 12
        self.occupancies = [0] * 3
        self.side = -1
        self.enpassant = SQUARES["NULL_SQUARE"]
        self.castle = 15
