__all__ = ['TestName']


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
            raise ValueError(f"В {value} допускаются только буквы!")
        elif not value.istitle():
            raise ValueError(f"В {value} первая буква должна быть Заглавной!")
        else:
            instance.__dict__[self.param_name] = value