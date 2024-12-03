# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.


from fractions import Fraction


# функция ввода дроби и проверки введённых значений
# возвращает значения числителя и знаменателя
def fraction(order) -> tuple[int, int]:
    while True:
        error = 0
        str_numerator, str_denominator = input("Введите " + order + " дробь в виде a/b : ").split(sep="/")
        try:
            numerator = int(str_numerator)
        except ValueError:
            print("Ошибка: Значение числителя должно быть целым числом")
            error += 1

        try:
            denominator = int(str_denominator)
            if denominator == 0:
                print("Ошибка: Знаменатель не может быть равен нулю")
        except ValueError:
            print("Ошибка: Значение знаменателя должно быть целым числом")
            error += 1

        if error != 0:
            print("Попробуйте ещё раз")
        else:
            if denominator != 0:
                break
    return numerator, denominator


# ищем наибольший общий делитель двух чисел
def nod_func(x, y):
    if (y == 0):
        return x
    else:
        return nod_func(y, x % y)


# сложение дробей
def summa(numerator1, denominator1, numerator2, denominator2):
    numerator = numerator1 * denominator2 + numerator2 * denominator1
    denominator = denominator1 * denominator2
    nod = nod_func(numerator, denominator)
    numerator /= nod
    denominator /= nod
    # выделяем целую часть
    # ну и что, что Fraction этого не умеет
    # за то красиво
    if numerator > denominator:
        whole = numerator // denominator
        numerator = numerator - whole * denominator
        result = str(int(whole)) + " " + str(int(numerator)) + "/" + str(int(denominator))
    else:
        result = str(int(numerator)) + "/" + str(int(denominator))
    return result


# умножение дробей
def composition(numerator1, denominator1, numerator2, denominator2):
    numerator = numerator1 * numerator2
    denominator = denominator1 * denominator2
    nod = nod_func(numerator, denominator)
    numerator /= nod
    denominator /= nod
    if numerator > denominator:
        whole = numerator // denominator
        numerator = numerator - whole * denominator
        result = str(int(whole)) + " " + str(int(numerator)) + "/" + str(int(denominator))
    else:
        result = str(int(numerator)) + "/" + str(int(denominator))
    return result


# начинаем!
numerator_1, denominator_1 = fraction('первую')
numerator_2, denominator_2 = fraction('вторую')
print(f" Первая дробь = {numerator_1}/{denominator_1}")
print(f" Вторая дробь = {numerator_2}/{denominator_2}")
print("Сумма дробей равна:   ", summa(numerator_1, denominator_1, numerator_2, denominator_2))
print("Проверочное значение: ", Fraction(numerator_1, denominator_1) + Fraction(numerator_2, denominator_2))
print("Произведение дробей равно: ", composition(numerator_1, denominator_1, numerator_2, denominator_2))
print("Проверочное значение:      ", Fraction(numerator_1, denominator_1) * Fraction(numerator_2, denominator_2))
