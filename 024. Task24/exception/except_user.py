class MainException(Exception):
    """Базовое пользовательское исключение."""
    pass


class NotLetters(MainException):
    """Исключение:
    в ФИО используются не только буквы.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'В "{self.value}" допускаются только буквы!'


class NotTitle(MainException):
    """Исключение:
    первый символ в ФИО не заглавная буква.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'В "{self.value}" первая буква должна быть Заглавной!'


class RangeNotInt(MainException):
    """Исключение:
    - оценка и результаты теста должны быть целыми числами.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Оценка "{self.value}" должна быть целым числом!'


class RangeNotLimit(MainException):
    """Исключение:
    - оценка и результаты теста должны быть целыми числами.
    """

    def __init__(self, value, min_value, max_value):
        self.value = value
        self.min_value = min_value
        self.max_value = max_value

    def __str__(self):
        return f"Оценка {self.value} вне допустимого диапазона [{self.min_value}, {self.max_value}]"


class DisciplineNo(MainException):
    """
    Исключение:
    - дисциплины нет в списке
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Дисциплины "{self.name}" нет в файле discipline.csv!'


class DisciplineFindStudent(MainException):
    """
    Исключение:
    - дисциплина уже есть у студента
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Дисциплины "{self.name}" уже есть у студента!'
