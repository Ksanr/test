def solve(hare_distances: list, turtle_distances: list):
    hare_all = 0 # подсчитайте общую дистанцию зайца
    for i in hare_distances:
        hare_all += i
    turtle_all = 0 # подсчитайте общую дистанцию черепахи
    for i in turtle_distances:
        turtle_all += i
    # определите, кто из двоих прошел бОльшую дистанцию
    if hare_all > turtle_all:
        result = "заяц"
    elif hare_all < turtle_all:
        result = "черепаха"
    else:
        result = "одинаково"
    return result

if __name__ == '__main__':
    # Этот код менять не надо
    result = solve([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3])
    assert result == "черепаха", f"Победитель определен неверно: {result}"
    print(f"Победитель: {result}")
    result = solve([8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3])
    assert result == "заяц", f"Победитель определен неверно: {result}"
    print(f"Победитель: {result}")
    result = solve([8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3])
    assert result == "одинаково", f"Победитель определен неверно: {result}"
    print(f"Победитель: {result}")