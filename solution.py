def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    # Ваш алгоритм
    return b ** 2 - 4 * a * c


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    d = discriminant(a, b, c)
    if d < 0:
        return 'корней нет'
    elif d:
        return ' '.join((str((-b + d ** 0.5) / 2 / a), str((-b - d ** 0.5) / 2 / a)))
    else:
        return str(-b / 2 / a)


if __name__ == '__main__':
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)