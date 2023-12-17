from managers.table_manager import TableManager

from src.lookup.squares import squares
from src.lookup.coordinates import coordinates

from src.utilities.attack import Attack
from src.utilities.bit import Bit
from src.utilities.console import Console

table_manager = TableManager()

tmp = table_manager.bishop_attack_table

# Console.print_bitboard(pawn_attacks(squares["h4"], colors["black"]))
# for i in range(64):
#     Console.print_bitboard(Attack.get_rook_attacks(i))

attack_mask = Attack.get_rook_attacks(squares["d4"])

for rank in range(8):
    for file in range(8):
        square = rank * 8 + file
        print(Bit.get_bit_count(Attack.get_rook_attacks(square)), end=", ")

    print()
# Console.print_bitboard(occupancy)
