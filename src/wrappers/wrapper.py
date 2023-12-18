from src.constants.bit_constants import BIT_32_MASK, BIT_64_MASK


class Wrapper:
    @staticmethod
    def uint32(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            return result & BIT_32_MASK

        return wrapper

    @staticmethod
    def uint64(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            return result & BIT_64_MASK

        return wrapper
