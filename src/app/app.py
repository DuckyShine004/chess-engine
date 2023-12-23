from managers.table_manager import TableManager
from managers.bitboard_manager import BitboardManager

from src.utilities.bit import Bit
from src.utilities.attack import Attack
from src.utilities.console import Console

from src.lookup.piece_lookup import PIECES, SIDES
from src.lookup.board_lookup import SQUARES

from src.constants.parser_constants import (
    EMPTY_BOARD,
    TRICKY_BOARD,
    DEBUG_BOARD,
    KILLER_BOARD,
)


class App:
    def __init__(self):
        self.table_manager = TableManager(self)
        self.bitboard_manager = BitboardManager(self)

        self.bitboard_manager.parse_fen("8/8/8/3k4/8/8/8/8 w - - ")
        self.bitboard_manager.print_board()
        Console.print_attacked_squares(self, SIDES["black"])
