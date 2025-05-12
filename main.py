"""Решение квадратного уравнения"""


def treesome(a: int, b:int, c:int ):
    """Функция для вычисления корней квадратного уровнения"""
    d = b**2-4*(a*c)
    if d > 0:
        return d, ((-b - d ** (0.5)) / (a * 2)), ((-b + d ** (0.5)) / (a * 2))

    if d == 0:
        return d, (-b / (a * 2))

    return d, "Корней нет"


if __name__ == '__main__':
    A = float(input('Введите а: '))
    B = float(input('Введите b: '))
    C = float(input('Введите c: '))
    print(treesome(A, B, C))
