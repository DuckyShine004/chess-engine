from src.lookup.square import square

from src.utilities.bit import Bit
from src.utilities.console import Console


bitboard = 0
bitboard |= 1 << square["e2"]

Console.print_bitboard(bitboard)
