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
        return value & Bit.left_shift(1, position)

    @staticmethod
    def set_bit(value, position):
        return value | Bit.left_shift(1, position)

    @staticmethod
    def pop_bit(value, position):
        bit = Bit.get_bit(value, position)

        return value ^ Bit.left_shift(1, position) if bit else value

    @staticmethod
    def count_bits(bitboard):
        count = 0

        while bitboard:
            bitboard &= bitboard - 1
            count += 1

        return count
