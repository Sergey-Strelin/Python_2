# Создать класс - уравнение, который
# принимает входные параметры и возвращает ответ
# взависимости от количества переданных параметров


class Equations:
    # Получаем коэффициенты уравнения ax**2 + bx + c = 0
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def decision(self):
        if self.a == 0 and self.b != 0 and self.c != 0:
            print(f'Решенем уравнения {self.b} * x + {self.c} = 0 будет \n х = {-self.c/self.b}  ')
        elif self.a == 0 and self.b != 0 and self.c == 0:
            print(f'Решенем уравнения {self.b} * x = 0 будет \nх = 0')
        elif self.a != 0 and self.b == 0 and self.c == 0:
            print(f'Решенем уравнения {self.a} * x**2 = 0 будет \nх = 0')
        elif self.a == 0 and self.b == 0 and self.c == 0:
            print('Решением уравнения, у которого все коэффициенты равны нулю, будет любое число!')
        elif self.a == 0 and self.b == 0 and self.c != 0:
            print('При коэффициентах а и b равных нулю уравнение не имеет ни одного решения')
        else:
            discriminant = self.b**2 - 4 * self.a * self.c
            if discriminant == 0:
                print(f'Уравнение {self.a} * x**2 + {self.b} * x + {self.c} = 0 имеет один корень')
                print(f'x = {-self.b / (2 * self.a)}')
            elif discriminant > 0:
                print(f'Уравнение {self.a} * x **2 + {self.b} * x + {self.c} = 0 имеет два кореня')
                x1 = (-self.b + discriminant ** 0.5) / (2 * self.a)
                x2 = (-self.b - discriminant ** 0.5) / (2 * self.a)
                print(f'{x1 = } \n{x2 = }')
            elif discriminant < 0:
                print(f'Уравнение {self.a} * x **2 + {self.b} * x + {self.c} = 0 имеет два комплексных кореня')
                discriminant = (-discriminant) ** 0.5
                x = -self.b / (2 * self.a)
                y = discriminant / (2 * self.a)
                if y > 0:   # подавдяем лишние знаки если мнимая часть отрицательная
                    print(f'x1 = {x} + i * {y}')
                    print(f'x1 = {x} - i * {y}')
                else:
                    print(f'x1 = {x} + i * {-y}')
                    print(f'x1 = {x} - i * {-y}')


if __name__ == '__main__':
    g1 = Equations(4, 2, 5)
    g2 = Equations(-1, 2, 3)
    g3 = Equations(1, 2, 4)
    g4 = Equations(0, 0, 0)
    g5 = Equations(0, 5, 2)
    g6 = Equations(5, 2, 0)
    g7 = Equations(6, 0, 0)
    g1.decision()
    g2.decision()
    g3.decision()
    g4.decision()
    g5.decision()
    g6.decision()
    g7.decision()
