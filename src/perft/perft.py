import time


class Perft:
    @staticmethod
    def get_time():
        return int(time.perf_counter() * 1000)
