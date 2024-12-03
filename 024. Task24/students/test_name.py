__all__ = ['TestName']

from exception.except_user import NotLetters, NotTitle


class TestName:
    """Проверка правильности ввода ФИО - должны быть только буквами и начинаться с заглавных."""

    def __set_name__(self, owner, name):
        """Установить имя проверяемого атрибута."""
        self.param_name = name

    def __get__(self, instance, owner):
        """Вернуть значение атрибута."""
        return instance.__dict__[self.param_name]

    def __set__(self, instance, value: str):
        """Установить значение атрибута."""
        if not value.isalpha():
            raise NotLetters(value)
        elif not value.istitle():
            raise NotTitle(value)
        else:
            instance.__dict__[self.param_name] = value
