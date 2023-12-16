from src.constants.bit_constants import BIT_64_MASK


def convert_to_uint64(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result & 0xFFFFFFFFFFFFFFFF

    return wrapper


class Bit:
    @convert_to_uint64
    @staticmethod
    def left_shift(value, offset):
        return value << offset

    @convert_to_uint64
    @staticmethod
    def right_shift(value, offset):
        return value >> offset

    @staticmethod
    def get_bit(value, position):
        return value & (1 << position)

    @staticmethod
    def set_bit(value, position):
        return value | (1 << position)

    @staticmethod
    def pop_bit(value, position):
        return value ^ (1 << position) if Bit.get_bit(value, position) else value
