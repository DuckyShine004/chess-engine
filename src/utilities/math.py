from src.utilities.bit import Bit

from src.constants.board_constants import STATE


class Math:
    state = STATE

    @staticmethod
    def get_random_number():
        Math.state ^= Bit.left_shift32(Math.state, 13)
        Math.state ^= Bit.right_shift32(Math.state, 17)
        Math.state ^= Bit.left_shift32(Math.state, 5)

        return Math.state
