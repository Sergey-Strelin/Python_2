# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


while True:
    try:
        number_dec = int(input("Введите натуральное число : "))
        if number_dec > 0:
            break
        else:
            print("Ошибка: введено отрицательное число!")
            print("Попробуйте ещё раз")
    except ValueError:
        print("Ошибка: введите натуральное число")
        print("Попробуйте ещё раз")

# Получаем ПРОВЕРОЧНОЕ 16тиричное число с помошью встроенной функции
print("У нас ДОЛЖНО получиться: ", hex(number_dec))

digits_hex = "0123456789abcdef"  # Строка с шестнадцатеричными цифрами
number_hex = ""

while number_dec > 0:
    remainder = number_dec % 16
    number_hex = digits_hex[remainder] + number_hex
    number_dec //= 16

print("У нас получилось число:   0х", number_hex, sep="")