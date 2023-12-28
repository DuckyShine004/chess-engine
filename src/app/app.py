import getch

from managers.table_manager import TableManager
from managers.bitboard_manager import BitboardManager
from managers.move_manager import MoveManager

from src.data.parameters.move_parameters import MoveParameters
from src.data_structures.moves import Moves

from src.routines.codec import Codec
from src.perft.perft import Perft

from src.utilities.bit import Bit
from src.utilities.attack import Attack
from src.utilities.console import Console

from src.generator.move_generator import MoveGenerator

from src.constants.piece_constants import PIECES, SIDES, UNICODE_PIECES
from src.constants.board_constants import SQUARES, COORDINATES
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
        self.move_manager = MoveManager(self)

        print("Tables initialized")

        self.bitboard_manager.parse_fen(INITIAL_BOARD)
        self.bitboard_manager.print_board()

        start = Perft.get_time()
        nodes = Perft.get_perft(self, 4)

        print(f"Time taken to execute: {Perft.get_time() - start} ms")
        print(f"Nodes: {nodes}")
