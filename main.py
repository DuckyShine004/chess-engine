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
    bitboards[piece] = Bit.set_bit(bitboards[piece], SQUARES["a2"])
    bitboards[piece] = Bit.set_bit(bitboards[piece], SQUARES["b2"])
    bitboards[piece] = Bit.set_bit(bitboards[piece], SQUARES["c2"])
    bitboards[piece] = Bit.set_bit(bitboards[piece], SQUARES["d2"])
    bitboards[piece] = Bit.set_bit(bitboards[piece], SQUARES["e2"])
    bitboards[piece] = Bit.set_bit(bitboards[piece], SQUARES["f2"])
    bitboards[piece] = Bit.set_bit(bitboards[piece], SQUARES["g2"])
    bitboards[piece] = Bit.set_bit(bitboards[piece], SQUARES["h2"])
    Console.print_bitboard(bitboards[piece])
    Console.print_board(bitboards, 64, bitboard_manager.castle, 1)


stats = pstats.Stats(profile)
stats.sort_stats(pstats.SortKey.TIME)
stats.dump_stats(filename=PROFILE_NAME)
