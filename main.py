import cProfile
import pstats

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
    bitboards = bitboard_manager.bitboards

    piece = PIECES["P"]
    bitboards[piece] = Bit.set_bit(bitboards[piece], SQUARES["e2"])
    Console.print_bitboard(bitboards[piece])
    print("piece:", ASCII_PIECES[piece])
    print("piece:", UNICODE_PIECES[piece])


stats = pstats.Stats(profile)
stats.sort_stats(pstats.SortKey.TIME)
stats.dump_stats(filename=PROFILE_NAME)
