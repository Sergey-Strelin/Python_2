# Запрашиваем число и проверяем, что это число
# и оно в диапазоне от 1 до 100 000


while True:
    try:
        num = int(input("Введите целое число от 1 до 100 000: "))
        if 0 < num < 100000:
            break
        else:
            print("Число не в заданном диапазоне")
            print("Попробуйте ещё раз!")
    except ValueError:
        print("Ошибка: введите целое число")
        print("Попробуйте ещё раз!")

res = 0
if num == 1:
    res = 1
elif num % 2 == 0:
    res = 2
else:
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            res = 2

if res == 0:
    print(f"Число {num} является простым")
elif res == 1:
    print(f"Число {num} НЕ является простым или составным")
else:
    print(f"Число {num} является составным")