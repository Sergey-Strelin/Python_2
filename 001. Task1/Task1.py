# Запрашиваем длины сторон треугольника
# проверяем, что введёное значение является числом
# и больше нуля
# Три стороны - три запроса


while True:
    try:
        side_a = float(input("Введите длинну стороны 'а': "))
        if side_a > 0:
            break
        else:
            print("Ошибка: длинна стороны должна быть больше нуля!")
            print("Попробуйте ещё раз")
    except ValueError:
        print("Ошибка: введите число")
        print("Попробуйте ещё раз")

while True:
    try:
        side_b = float(input("Введите длинну стороны 'b': "))
        if side_b > 0:
            break
        else:
            print("Ошибка: длинна стороны должна быть больше нуля!")
            print("Попробуйте ещё раз")
    except ValueError:
        print("Ошибка: введите число")
        print("Попробуйте ещё раз")

while True:
    try:
        side_c = float(input("Введите длинну стороны 'с': "))
        if side_c > 0:
            break
        else:
            print("Ошибка: длинна стороны должна быть больше нуля!")
            print("Попробуйте ещё раз")
    except ValueError:
        print("Ошибка: введите число")
        print("Попробуйте ещё раз")

# проверяем, что треугольник существует + на равнобедренность и равносторонность
if side_a + side_b > side_c and side_b + side_c > side_a and side_a + side_c > side_b:
    print("Треугольник существует!")
    if side_a == side_b == side_c:
        print("Заданный треугольник равносторонний!")
    elif side_a == side_b and side_a != side_c:
        print("Заданный треугольник равнобедренный!")
    elif side_a == side_c and side_a != side_b:
        print("Заданный треугольник равнобедренный!")
    elif side_b == side_c and side_b != side_a:
        print("Заданный треугольник равнобедренный!")
    else:
        print("У Вас получился обычный треугольник.")
else:
    print("Треугольник с такими длинами сторон не существует!")