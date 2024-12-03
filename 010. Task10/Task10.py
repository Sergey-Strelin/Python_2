# Возьмите задачу о банкомате.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


# Pin код
PIN = "1234"
# Процент за снятие
PERCENT_PULL = 0.015
# Кол-во последовательных операция для начисления %
OPERATION_ADDED = 3
# Размер начисляемых процентов за каждую OPERATION_ADDED операцию пополнения карты
PERCENT_ADD = 0.03
# Минимальная сумма комиссии за снятие
MIN_PERCENTAGE = 30
# Максимальная сумма комиссии за снятие
MAX_PERCENTAGE = 600
# Кратность купюр
MIN_BANKNOTE = 50
# сумма с которой берут налог на богатых
MIN_TAX = 5_000_000
# Ставка налогообложения богатых
PERCENT_TAX = 0.1

# список журнала операций
operation_log = []


# добавление записи в журнал
def logging(operation: str):
    operation_log.append(operation)


# вывод журнала операций на экран
def show_log():
    print("-- ЖУРНАЛ ОПЕРАЦИЙ --")
    for o in operation_log:
        print(o)


# Удержание налога на богатых
def tax_pay(summ: float) -> float:
    tax = summ * PERCENT_TAX
    print(f"Удержан налог на богатых: {tax:.2f}")
    summ -= tax
    logging(f"Удержан налог на богатых: {tax:.2f}")
    return summ


# Пополнение счёта, если надо - удержание налога
def push_cash(balance: float) -> (bool, float):
    summ = float(input("Введите сумму пополнения: "))
    logging(f"Пополняем баланс на {summ}")
    result = False

    # Удерживаю налог на богатых
    if balance > MIN_TAX:
        balance = tax_pay(balance)

    # проверяю сумму
    if summ % 50 == 0:
        balance += summ
        print(f"Баланс увеличен: {summ:.2f}")
        logging(f"Успешно! Баланс увеличен: {summ:.2f}")
        result = True
    else:
        print("Сумма должна быть кратной 50!")
        logging("Отмена! Сумма должна быть кратной 50!")

    show_balance(balance)
    return result, balance


# Снятие денег со счета, запрашивает снимаемую сумму
def pull_cash(balance: float) -> (bool, float):
    result = False
    show_balance(balance)
    summ = float(input("Введите сумму для снятия: "))
    logging(f"Попытка снятия - {summ}")
    # удерживаем налог на богатых
    if balance > MIN_TAX:
        balance = tax_pay(balance)

    # проверяю сумму
    if summ % 50 == 0:
        percent_summ = summ * PERCENT_PULL

        if percent_summ > MAX_PERCENTAGE:
            percent_summ = MAX_PERCENTAGE
        if percent_summ < MIN_PERCENTAGE:
            percent_summ = MIN_PERCENTAGE

        if balance - summ - percent_summ < 0:
            print("Недостаточно средств!")
            logging("Отмена! Недостаточно средств!")
        else:
            balance -= (summ + percent_summ)
            print(f"Выдано {summ:.2f}, комиссия {percent_summ:.2f}")
            logging(f"Успешно! Выдано {summ:.2f}, комиссия {percent_summ:.2f}")
            result = True
    else:
        print("Сумма должна быть кратной 50!")
        logging("Отмена! Сумма должна быть кратной 50!")

    show_balance(balance)

    return result, balance


# показываем текущий баланс
def show_balance(summ: float):
    print(f"Текущий баланс : {summ:.2f}")


# Показываем меню, возвращаем выборранный пункт
# если ввели не верное значение или 0 - возвращаем 0
def show_menu(menu: dict[int, str]) -> int:
    for k, v in menu.items():
        print(f"{k} - {v}")
    result = int(input("> "))
    return result if result in menu.keys() else 0


# задаём начальный баланс
balance: float = 0
# устанавливаем счетчик операций для начисления процентов
operation_counter = 0
# меню банкомата
menu_bank: dict = {
    1: "снять",
    2: "пополнить",
    3: "баланс",
    0: "выход",
}


# запрос пин-кода
authorized = PIN == (input("Введите PIN: "))

while authorized:
    action = show_menu(menu_bank)
    match action:
        # Снятие средств.
        case 1:
            success, balance = pull_cash(balance)
            if success:
                operation_counter += 1
        # Пополнение карты.
        case 2:
            success, balance = push_cash(balance)
            if success:
                operation_counter += 1
        # Просмотр баланса.
        case 3:
            show_balance(balance)
        # Выход
        case 0:
            print("До встречи!")
            break

    if operation_counter == OPERATION_ADDED:
        operation_counter = 0
        summ_add = balance * PERCENT_ADD
        print(f"Начисление %: {summ_add:.2f}")
        logging(f"Начисление %: {summ_add:.2f}")
        balance += summ_add
        show_balance(balance)
else:
    print("Неверный пин-код!")

show_log()