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

        params = MoveParameters(SQUARES["d7"], SQUARES["d8"], PIECES["P"], PIECES["R"], 1, 1, 1, 0)
        move = Serializer.get_encoded_move(params)

        source_square = Deserializer.get_decoded_source_square(move)
        target_square = Deserializer.get_decoded_target_square(move)
        piece = Deserializer.get_decoded_piece(move)
        promoted_piece = Deserializer.get_decoded_promoted_piece(move)
        capture_flag = Deserializer.get_decoded_capture_flag(move)
        double_pawn_push_flag = Deserializer.get_decoded_double_pawn_push_flag(move)
        enpassant_flag = Deserializer.get_decoded_enpassant_flag(move)

        print(f"source square: {COORDINATES[source_square]}")
        print(f"target square: {COORDINATES[target_square]}")
        print(f"piece: {UNICODE_PIECES[piece]}")
        print(f"promoted piece: {UNICODE_PIECES[promoted_piece]}")
        print(f"capture flag: {capture_flag}")
        print(f"double pawn push flag: {double_pawn_push_flag}")
        print(f"enpassant flag: {enpassant_flag}")
