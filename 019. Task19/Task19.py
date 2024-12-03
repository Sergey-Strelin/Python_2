# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из
# созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе
# переданного типа и верните его из класса-фабрики.


# класс животное
class Animal:
    def __init__(self, name: str, age: int, weight: int, breed: str):
        self.name = name  # кличка
        self.age = age  # возраст
        self.weight = weight  # вес
        self.breed = breed  # порода

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

    def get_weight(self):
        print(self.weight)

    def get_breed(self):
        print(self.breed)

    def get_unique(self):
        pass

    def get_print(self):
        pass


# класс собака
class Dog(Animal):
    def __init__(self, name: str, age: int, weight: int, breed: str, title: str):
        super().__init__(name, age, weight, breed)
        self.title = title  # титул с выставки

    def get_unique(self):
        print(self.title)

    def get_print(self):
        print(f'Собака по кличке: {self.name},'
              f'возраст: {self.age}, '
              f'вес: {self.weight}, ' 
              f'порода: {self.breed} , '
              f'титул: {self.title}')


# класс кошка
class Cat(Animal):
    def __init__(self, name: str, age: int, weight: int, breed: str, type_cat: str):
        super().__init__(name, age, weight, breed)
        self.type_cat = type_cat  # тип кошки (домашняя, уличная.. ещё какая-то выстовачная?)

    def get_unique(self):
        print(self.type_cat)

    def get_print(self):
        print(f'Кошка по кличке: {self.name}, '
              f'возраст: {self.age}, '
              f'вес: {self.weight}, '
              f'порода: {self.breed} , '
              f'тип: {self.type_cat}')


# класс лошадь
class Horse(Animal):
    def __init__(self, name: str, age: int, weight: int, breed: str, exterior: str):
        super().__init__(name, age, weight, breed)
        self.exterior = exterior  # экстерьер

    def get_unique(self):
        print(self.exterior)

    def get_print(self):
        print(f'Лошадь по кличке: {self.name}, '
              f'возраст: {self.age}, '
              f'вес: {self.weight}, '
              f'порода: {self.breed} , '
              f'экстерьер: {self.exterior}')


# класс фабрика
class Factory(Animal):
    def __init__(self, name: str, age: int, weight: int, breed: str, option: str, type_animal: str):
        super().__init__(name, age, weight, breed)
        self.option = option            # дополнительное свойство животного
        self.type_animal = type_animal  # вид животного (собака, кошка, лошадь)

    @staticmethod
    def gen_animal(name: str, age: int, weight: int, breed: str, option: str, type_animal: str) -> Animal:
        animal = None
        match type_animal.lower():
            case 'dog':
                animal = Factory.gen_dog(name, age, weight, breed, option)
            case 'cat':
                animal = Factory.gen_cat(name, age, weight, breed, option)
            case 'horse':
                animal = Factory.gen_horse(name, age, weight, breed, option)

        return animal

    @staticmethod
    def gen_dog(name, age, weight, breed, option):
        return Dog(name, age, weight, breed, option)

    @staticmethod
    def gen_cat(name, age, weight, breed, option):
        return Cat(name, age, weight, breed, option)

    @staticmethod
    def gen_horse(name, age, weight, breed, option):
        return Horse(name, age, weight, breed, option)


if __name__ == '__main__':
    # создаём 3и объекта - животное, по одному каждого видов
    d = Factory.gen_animal('Верный', 10, 2, 'Овчарка', 'Чемпион', 'Dog')
    c = Factory.gen_animal('Мурка', 4, 3, 'Вислоухая', 'домашняя', 'CAT')
    h = Factory.gen_animal('Быстрый', 5, 450, 'Вороная', 'соответствует породе', 'horse')
    # проверяем результат и тип созданного объекта - животное
    d.get_print()
    print(f'В переменной "d" хранится объект класса -  {type(d)}')
    c.get_print()
    print(f'В переменной "c" хранится объект класса -  {type(c)}')
    h.get_print()
    print(f'В переменной "h" хранится объект класса -  {type(h)}')
