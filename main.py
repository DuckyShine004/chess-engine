import cProfile
import pstats

from managers.table_manager import TableManager
from src.utilities.bit import Bit
from src.utilities.attack import Attack
from src.utilities.console import Console
from src.lookup.squares import squares
from src.constants.file_constants import PROFILE_NAME

with cProfile.Profile() as profile:
    table_manager = TableManager()

    occupancy = 0

    occupancy = Bit.set_bit(occupancy, squares["c5"])
    occupancy = Bit.set_bit(occupancy, squares["f2"])
    occupancy = Bit.set_bit(occupancy, squares["g7"])
    occupancy = Bit.set_bit(occupancy, squares["b2"])
    occupancy = Bit.set_bit(occupancy, squares["g5"])
    occupancy = Bit.set_bit(occupancy, squares["e2"])
    occupancy = Bit.set_bit(occupancy, squares["e7"])

    Console.print_bitboard(
        Attack.get_rook_attack_masks(
            squares["e5"],
            occupancy,
            table_manager.rook_attack_table,
            table_manager.rook_attack_masks,
        )
    )

stats = pstats.Stats(profile)
stats.sort_stats(pstats.SortKey.TIME)
stats.dump_stats(filename=PROFILE_NAME)
