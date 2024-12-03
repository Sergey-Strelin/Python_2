# Создайте словарь со списком вещей для похода
# в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав
# его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.


things = {'кружка':0.2,
          'ложка':0.1,
          'спальник':5,
          'коврик':2,
          'вода':3,
          'фонарь':0.5,
          'еда':4,
          'дождевик':1,
          'аптечка':2,
          }

while True:
    try:
        capacity = float(input("Введите грузоподьёмность рюкзака в кг (больше 1 кг) : "))
        if capacity > 0:
            break
        else:
            print("Ошибка: грузоподьёмность рюкзака должна быть больше нуля!")
            print("Попробуйте ещё раз")
    except ValueError:
        print("Ошибка: введите число")
        print("Попробуйте ещё раз")

result = []
while len(things) > 0:
    max_weight_thing = max(things.values())
    max_weight_thing_key = max(things, key = things.get)
    if capacity >= max_weight_thing:
        result.append(max_weight_thing_key)
        capacity -= max_weight_thing
    things.pop(max_weight_thing_key)

print (result)