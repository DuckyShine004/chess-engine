import cProfile
import pstats

from managers.table_manager import TableManager

from src.constants.file_constants import PROFILE_NAME

with cProfile.Profile() as profile:
    table_manager = TableManager()

    tmp = table_manager.bishop_attack_table

    stats = pstats.Stats(profile)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename=PROFILE_NAME)
