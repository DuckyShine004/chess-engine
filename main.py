import cProfile
import pstats

from src.constants.parser_constants import EMPTY_BOARD, TRICKY_BOARD, DEBUG_BOARD
from managers.table_manager import TableManager
from managers.bitboard_manager import BitboardManager

from src.utilities.bit import Bit

from src.utilities.attack import Attack
from src.utilities.console import Console
from src.lookup.piece_lookup import PIECES, ASCII_PIECES, UNICODE_PIECES
from src.lookup.board_lookup import SQUARES
from src.constants.file_constants import PROFILE_NAME

with cProfile.Profile() as profile:
    table_manager = TableManager()
    bitboard_manager = BitboardManager()
    attack_tables = (
        table_manager.bishop_attack_table,
        table_manager.rook_attack_table,
    )
    attack_masks = (
        table_manager.bishop_attack_masks,
        table_manager.rook_attack_masks,
    )
    occupancy = 0
    occupancy = Bit.set_bit(occupancy, SQUARES["b6"])
    occupancy = Bit.set_bit(occupancy, SQUARES["d6"])
    occupancy = Bit.set_bit(occupancy, SQUARES["f6"])
    occupancy = Bit.set_bit(occupancy, SQUARES["b4"])
    occupancy = Bit.set_bit(occupancy, SQUARES["g4"])
    occupancy = Bit.set_bit(occupancy, SQUARES["c3"])
    occupancy = Bit.set_bit(occupancy, SQUARES["d3"])
    occupancy = Bit.set_bit(occupancy, SQUARES["e3"])
    Console.print_bitboard(occupancy)
    Console.print_bitboard(
        Attack.get_queen_attack_masks(
            SQUARES["d4"], occupancy, attack_tables, attack_masks
        )
    )


stats = pstats.Stats(profile)
stats.sort_stats(pstats.SortKey.TIME)
stats.dump_stats(filename=PROFILE_NAME)
