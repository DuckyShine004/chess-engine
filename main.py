import random

from managers.table_manager import TableManager

from src.lookup.squares import squares
from src.lookup.coordinates import coordinates

from src.utilities.attack import Attack
from src.utilities.bit import Bit
from src.utilities.console import Console
from src.utilities.math import Math

table_manager = TableManager()

tmp = table_manager.bishop_attack_table

# Console.print_bitboard(pawn_attacks(squares["h4"], colors["black"]))
# for i in range(64):
#     Console.print_bitboard(Attack.get_rook_attacks(i))

attack_mask = Attack.get_rook_attacks(squares["d4"])

Console.print_bitboard(Math.get_random_uint32())
Console.print_bitboard(Math.get_random_uint32() & 0xFFFF)
Console.print_bitboard(Math.get_random_uint64())
Console.print_bitboard(
    Math.get_random_uint64() & Math.get_random_uint64() & Math.get_random_uint64()
)
