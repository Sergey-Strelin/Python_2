# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


numbers = [1, 2, 9, 4, 5,1, 2, 3, 4, 5,6,7,8,9,0]
result = []

for number in numbers:
    if numbers.count(number) > 1 and result.count(number) == 0:
        result.append(number)

print (result)