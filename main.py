from managers.table_manager import TableManager

from src.lookup.squares import squares
from src.utilities.attack import Attack
from src.utilities.bit import Bit
from src.utilities.console import Console

table_manager = TableManager()

tmp = table_manager.bishop_attack_table

# Console.print_bitboard(pawn_attacks(squares["h4"], colors["black"]))
# for i in range(64):
#     Console.print_bitboard(Attack.get_rook_attacks(i))

block = 0

block = Bit.set_bit(block, squares["d7"])
block = Bit.set_bit(block, squares["d2"])
block = Bit.set_bit(block, squares["d1"])
block = Bit.set_bit(block, squares["b4"])
block = Bit.set_bit(block, squares["g4"])

Console.print_bitboard(block)

Console.print_bitboard(Attack.get_rook_attacks_on_the_fly(squares["d4"], block))
