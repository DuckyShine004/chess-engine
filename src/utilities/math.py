from src.utilities.bit import Bit

from src.constants.bit_constants import BIT_16_MASK
from src.constants.board_constants import STATE


class Math:
    state = STATE

    @staticmethod
    def get_random_uint32():
        Math.state ^= Bit.left_shift32(Math.state, 13)
        Math.state ^= Bit.right_shift32(Math.state, 17)
        Math.state ^= Bit.left_shift32(Math.state, 5)

        return Math.state

    @staticmethod
    def get_random_uint64():
        w = Math.get_random_uint32() & BIT_16_MASK
        x = Math.get_random_uint32() & BIT_16_MASK
        y = Math.get_random_uint32() & BIT_16_MASK
        z = Math.get_random_uint32() & BIT_16_MASK

        return w | Bit.left_shift(x, 16) | Bit.left_shift(y, 32) | Bit.left_shift(z, 48)
