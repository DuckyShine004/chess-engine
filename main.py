import cProfile
import pstats

from src.app.app import App

from src.constants.file_constants import PROFILE_NAME


def main():
    with cProfile.Profile() as profile:
        app = App()

        app.start_uci()

    stats = pstats.Stats(profile)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename=PROFILE_NAME)


if __name__ == "__main__":
    main()
