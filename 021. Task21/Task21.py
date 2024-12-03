# Создайте класс Матрица. Добавьте методы для:
# - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц

class Matrix:
    """
    класс Матрица (двумерная), на вход получает матрицу в виде списка
    формирует два дополнительных свойства - размерность матрицы:
    size_x - количество столбцов
    size_y - количество строк
    реализованы следующие методы:
    - сложение матриц одинакового размера;
    - умножение согласованных матриц;
    - проверка матриц однакового размера на равенство и не равенство;
    - __str__  и __repl__
    """
    def __init__(self, matrix: list):
        self.matrix = matrix
        self.size_x = len(self.matrix)
        self.size_y = len(self.matrix[0])

    def __eq__(self, other):
        """
        сравнение матриц на равенство
        предварительно проверяет, что матрицы одинакового размера
        """
        if self.size_x == other.size_x and self.size_y == other.size_y:
            for i in range(self.size_x):
                for j in range(self.size_y):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            return True
        else:
            return 'Матрицы разного размера сравнить нельзя'

    def __gt__(self, other):
        """
        определение какая из двух одинаковых по размеру матриц больше.
        считаем, что первая матрица больше, если сумма всех её элементов больше
        суммы элементов второй матрицы
        """
        if self.size_x == other.size_x and self.size_y == other.size_y:
            result = 0
            for i in range(self.size_x):
                for j in range(self.size_y):
                    result += self.matrix[i][j] - other.matrix[i][j]
            return result > 0
        else:
            return 'Матрицы разного размера сравнивать нельзя'

    def __le__(self, other):
        """
        проверяем, что первая матрица меньше или равно второй
        считаем, что первая матрица меньше, если сумма всех её элементов мешьше или равна
        сумме элементов второй матрицы
        """
        if self.size_x == other.size_x and self.size_y == other.size_y:
            result = 0
            for i in range(self.size_x):
                for j in range(self.size_y):
                    result += self.matrix[i][j] - other.matrix[i][j]
            return result <= 0
        else:
            return 'Матрицы разного размера сравнивать нельзя'

    def __str__(self) -> str:
        """
        Крассивый вывод матрицы для пользователя
        """
        stroka = f'Матрица размером {self.size_y} на {self.size_x}: \n'
        for i in self.matrix:
            stroka += '\t'.join(list(map(str, i))) + '\n'
        return stroka[:-1]

    def __repr__(self) -> str:
        """
        вывод матрицы для разработчика
        """
        return f"matrix = Matrix({self.matrix})"

    def __add__(self, other):
        """
        сложение двух матриц одинакового размера
        предварительно проверяет размер матриц
        если матрицы разного размера - сообщает о невозможности сложить
        """
        if self.size_x == other.size_x and self.size_y == other.size_y:
            add_matrix = [[0] * self.size_y for _ in range(self.size_x)]
            for i in range(self.size_x):
                for j in range(self.size_y):
                    add_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(add_matrix)
        else:
            return "Складывать матрицы разного размера нельзя"

    def __mul__(self, other):
        """
        умножене двух матриц
        предварительно проверяет на соглаванность матриц
        (количество столбцов первой  = количество строк второй)
        если матрицы согласованны возвращает результат
        если матрицы не соглавованы сообщает о невозможности умножения
        """
        if self.size_x == other.size_y:
            mul_matrix = [[0] * other.size_y for _ in range(self.size_x)]
            for i in range(self.size_x):
                for j in range(other.size_y):
                    for k in range(other.size_x):
                        mul_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(mul_matrix)
        else:
            return 'Не согласованные матрицы перемножить нельзя'


if __name__ == '__main__':
    # создаём тестовый набор матриц
    a = Matrix([[1, 2], [2, 3], [3, 4]])
    b = Matrix([[11, 12], [12, 13], [13, 14]])
    c = Matrix([[2, 3], [3, 4]])
    d = Matrix([[1, 2, 3], [1, 2, 3]])
    # выводим все матрицы на экран двумя способами
    print(f'Матрица A \n {a}')
    print(repr(a))
    print(f'Матрица B \n {b}')
    print(repr(b))
    print(f'Матрица C \n {c}')
    print(repr(c))
    print(f'Матрица D \n {d}')
    print(repr(d))
    # сравнение матриц на равенство с первой
    print(f'Матрица A равна B? {a == b}')
    print(f'Матрица A Не равна B? {a != b}')
    print(f'Матрица A равна C? {a == c}')
    print(f'Матрица A равна C? {a == d}')
    # сравнение матриц на больше и меньше и т.п.
    print(f'Матрица A больше B? {a > b}')
    print(f'Матрица A больше или равна B? {a >= b}')
    print(f'Матрица A меньше B? {a < b}')
    print(f'Матрица A меньше или равно B? {a <= b}')
    # сложение первой матицы с всеми
    print(f'Результат сложения матриц A и B: \n {a + b}')
    print(f'Результат сложения матриц A и C: \n {a + c}')
    print(f'Результат сложения матриц A и D: \n {a + d}')
    # умножение первой матрицы на остальные
    print(f'Результат умножения матрицы A на B: \n {a * b}')
    print(f'Результат умножения матрицы A ны C: \n {a * c}')
    print(f'Результат умножения матрицы A на D: \n {a * d}')
    # просмотр документации
    print(f'Документация класса Matrix: {Matrix.__doc__}')
    print(f'Документация метода умножение матриц: {Matrix.__mul__.__doc__}')
