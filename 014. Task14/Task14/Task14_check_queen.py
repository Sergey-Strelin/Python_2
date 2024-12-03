# модуль проверки расстановки ферзей на КВАДРАТНОЙ доске любого размера

__all__ = ['check_queen']

_QUEEN_COUNT: int = 8  # расставленное кол-во ферзей на доске
_SIZE_BOARD: int = 8  # размер КВАДРАТНОЙ доски


def check_queen(positions: list[tuple]) -> bool:
    result = True
    for i in range(_QUEEN_COUNT - 1):  # берем ферзей по списку, исключая последнего (сам себя бить не может)
        if not result:
            break
        row_1, col_1 = positions[i]
        for j in range(i + 1, _QUEEN_COUNT):  # проверяем со следующими до конца списка
            row_2, col_2 = positions[j]
            if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                result = False
                break
    return result


if __name__ == '__main__':
    queens_positions = [
        [(0, 5), (1, 2), (4, 3), (2, 2), (7, 6), (5, 1), (2, 7), (3, 4)],
        [(0, 2), (1, 5), (2, 3), (3, 0), (4, 7), (5, 4), (6, 6), (7, 1)],
    ]
    for position in queens_positions:
        print(f"В расстановке: ", position)
        if check_queen(position):
            print("Ферзи не бьют друг друга")
        else:
            print("Есть ферзи под ударом")
