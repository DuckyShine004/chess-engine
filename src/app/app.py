from managers.table_manager import TableManager
from managers.bitboard_manager import BitboardManager

from src.data.parameters.move_parameters import MoveParameters
from src.routines.move import Move
from src.data_structures.moves import Moves

from src.routines.codec import Codec

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

        self.bitboard_manager.parse_fen(
            "r3k2r/pPppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1 "
        )
        self.bitboard_manager.print_board()

        move_generator = MoveGenerator(self)
        # moves = move_generator.get_moves()
        moves = Move.get_moves(self)

        Console.print_moves(moves)
