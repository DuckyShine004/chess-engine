from managers.table_manager import TableManager
from managers.bitboard_manager import BitboardManager

from src.routines.move import Move
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
    INITIAL_BOARD,
)


class App:
    def __init__(self):
        self.table_manager = TableManager(self)
        self.bitboard_manager = BitboardManager(self)

        self.bitboard_manager.parse_fen(
            "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R b KQkq - 0 1 "
        )
        self.bitboard_manager.print_board()
