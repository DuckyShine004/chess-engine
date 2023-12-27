import getch

from managers.table_manager import TableManager
from managers.bitboard_manager import BitboardManager
from managers.move_manager import MoveManager

from src.data.parameters.move_parameters import MoveParameters
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
        self.move_manager = MoveManager(self, self.bitboard_manager)

        print("tables initialized")

        self.bitboard_manager.parse_fen(
            "r3k2r/p1ppRpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R b KQkq - 0 1 "
        )
        self.bitboard_manager.print_board()

        self.move_generator = MoveGenerator(self)
        moves = self.move_generator.get_moves()

        for move_count in range(moves.count):
            move = moves.moves[move_count]

            self.bitboard_manager.preserve_attributes()
            if not self.move_manager.make_move(move, 0):
                continue

            self.bitboard_manager.print_board()
            getch.getch()

            self.bitboard_manager.set_attributes()
            self.bitboard_manager.print_board()
            getch.getch()
