# Простой генератор рассановок ферзей на КВАДРАТНОЙ доске

__all__ = ['gen_queen']

import random as rnd

_QUEEN_COUNT: int = 8  # кол-во ферзей на доске, должно быть не больше размера доски
_SIZE_BOARD: int = 8  # размер КВАДРАТНОЙ доски


def gen_queen() -> list[tuple[int, int]]:
    result = []
    # генерируем по одному ферзю на одну горизонталь доски
    for i in range(_QUEEN_COUNT):
        result.append((i, rnd.randint(0, _SIZE_BOARD - 1)))
    return result


if __name__ == '__main__':
    print(gen_queen())
