import cProfile
import pstats

from src.constants.parser_constants import EMPTY_BOARD, TRICKY_BOARD, DEBUG_BOARD
from managers.table_manager import TableManager
from managers.bitboard_manager import BitboardManager

from src.utilities.bit import Bit

# from src.utilities.attack import Attack
from src.utilities.console import Console
from src.lookup.piece_lookup import PIECES, ASCII_PIECES, UNICODE_PIECES
from src.lookup.board_lookup import SQUARES
from src.constants.file_constants import PROFILE_NAME

with cProfile.Profile() as profile:
    # table_manager = TableManager()
    bitboard_manager = BitboardManager()
    bitboard_manager.parse_fen(TRICKY_BOARD)
    bitboard_manager.print_board()

    Console.print_bitboard(bitboard_manager.occupancies[0])
    Console.print_bitboard(bitboard_manager.occupancies[1])
    Console.print_bitboard(bitboard_manager.occupancies[2])


stats = pstats.Stats(profile)
stats.sort_stats(pstats.SortKey.TIME)
stats.dump_stats(filename=PROFILE_NAME)
