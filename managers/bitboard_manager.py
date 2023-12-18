from src.lookup.colors import colors
from src.lookup.squares import squares


class BitboardManager:
    def __init__(self):
        self.bitboards = [0] * 12
        self.occupancies = [0] * 3
        self.side_to_move = -1
        self.enpassant = squares["NULL_SQUARE"]
