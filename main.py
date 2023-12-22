import cProfile
import pstats

from src.constants.parser_constants import (
    EMPTY_BOARD,
    TRICKY_BOARD,
    DEBUG_BOARD,
    KILLER_BOARD,
)
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

    occupancy = 0

    occupancy = Bit.set_bit(occupancy, SQUARES["c5"])
    occupancy = Bit.set_bit(occupancy, SQUARES["f2"])
    occupancy = Bit.set_bit(occupancy, SQUARES["g7"])
    occupancy = Bit.set_bit(occupancy, SQUARES["b2"])
    occupancy = Bit.set_bit(occupancy, SQUARES["g5"])
    occupancy = Bit.set_bit(occupancy, SQUARES["e2"])
    occupancy = Bit.set_bit(occupancy, SQUARES["e7"])

    Console.print_bitboard(occupancy)

    bishop_attack_table = table_manager.bishop_attack_table
    bishop_attack_mask = table_manager.bishop_attack_masks
    Console.print_bitboard(
        Attack.get_bishop_attack_masks(
            SQUARES["d4"], occupancy, bishop_attack_table, bishop_attack_mask
        )
    )

    # bitboard_manager = BitboardManager()

    # bitboard_manager.parse_fen(KILLER_BOARD)
    # bitboard_manager.print_board()


stats = pstats.Stats(profile)
stats.sort_stats(pstats.SortKey.TIME)
stats.dump_stats(filename=PROFILE_NAME)
