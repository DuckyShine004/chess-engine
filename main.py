import cProfile
import pstats

from managers.table_manager import TableManager

# from src.utilities.bit import Bit
# from src.utilities.attack import Attack
# from src.utilities.console import Console
# from src.lookup.squares import squares
from src.constants.file_constants import PROFILE_NAME

with cProfile.Profile() as profile:
    table_manager = TableManager()


stats = pstats.Stats(profile)
stats.sort_stats(pstats.SortKey.TIME)
stats.dump_stats(filename=PROFILE_NAME)
