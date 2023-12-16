from src.constants.bit_constants import BIT_64_MASK


def convert_to_uint64(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result & 0xFFFFFFFFFFFFFFFF

    return wrapper


class Bit:
    @convert_to_uint64
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def get_bit(value, position):
        return value & (1 << position)
