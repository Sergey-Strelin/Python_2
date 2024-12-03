# В модуль с проверкой даты добавьте возможность
# запуска в терминале с передачей даты на проверку.


from sys import argv


# Проверка года: високосный - True, обычный - False
def check_year(year):
    return year % 4 == 0 or year % 100 == 0 and year % 400 != 0


# проверяем корректность введённого значения даты
def check_date(date: str):
    day, mon, year = map(int, date.split('.'))
    if not(1 <= day <= 31 and 1 <= mon <= 12 and 1 <= year <= 9999):
        return False
    if day > 30 and mon in (4, 6, 9, 11):
        return False
    if mon == 2 and check_year(year) and day > 29:
        return False
    if mon == 2 and not check_year(year) and day > 28:
        return False

    return True


if __name__ == '__main__':
    name, test_date = argv
    print(check_date(test_date))
