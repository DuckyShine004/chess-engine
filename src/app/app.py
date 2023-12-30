import getch
from src.data.states.board_states import BoardStates

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

from src.parsers.move_parser import MoveParser
from src.parsers.position_parser import PositionParser

from src.generator.move_generator import MoveGenerator

from src.constants.piece_constants import PIECES, SIDES, UNICODE_PIECES
from src.constants.board_constants import SQUARES, COORDINATES, MOVE_TYPES
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

        # move = self.move_parser.parse("e2e4")
        # self.move_manager.make_move(move, MOVE_TYPES["all"])

        self.position_parser = PositionParser(self)
        self.position_parser.parse("position startpos moves e2e4 e7e5 g1f3 e8e7 e1e2")
        self.bitboard_manager.print_board()
