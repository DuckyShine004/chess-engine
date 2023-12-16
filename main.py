from src.lookup.square import square

from src.utilities.bit import Bit
from src.utilities.console import Console


bitboard = 0
bitboard |= 1 << square["e4"]
bitboard |= 1 << square["c3"]
bitboard |= 1 << square["f2"]

bitboard = Bit.pop_bit(bitboard, square["e4"])
# bitboard = Bit.pop_bit(bitboard, square["e4"])

Console.print_bitboard(bitboard)
