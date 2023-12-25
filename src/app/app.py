from managers.table_manager import TableManager
from managers.bitboard_manager import BitboardManager

from src.data.parameters.move_parameters import MoveParameters
from src.routines.move import Move

from src.routines.deserializer import Deserializer
from src.routines.serializer import Serializer

from src.utilities.bit import Bit
from src.utilities.attack import Attack
from src.utilities.console import Console

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

        params = MoveParameters(SQUARES["d7"], SQUARES["e8"], PIECES["P"], PIECES["Q"], 0, 0, 0, 0)
        move = Serializer.get_encoded_move(params)

        Console.print_move(move)
