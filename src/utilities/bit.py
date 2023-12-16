from src.constants.bit_constants import BIT_64_MASK


def convert_to_uint64(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result & BIT_64_MASK

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
    def get_bit_count(bitboard):
        count = 0

        while bitboard:
            bitboard &= bitboard - 1
            count += 1

        return count

    @staticmethod
    def get_least_significant_first_bit(bitboard):
        if bitboard:
            return Bit.get_bit_count((bitboard & -bitboard) - 1)
        else:
            return -1

    @staticmethod
    def set_occupancy(index, bits_in_mask, attack_mask):
        occupancy = 0

        for count in range(bits_in_mask):
            square = Bit.get_least_significant_first_bit(attack_mask)
            attack_mask = Bit.pop_bit(attack_mask, square)

            if Bit.get_bit(index, count):
                occupancy = Bit.set_bit(occupancy, square)

        return occupancy
