#python3 -m unittest test_unittest.py


import unittest
from who_next import solve
from solution import solution

class TestNext(unittest.TestCase):
    # 3 теста по одному на unitest для программы "Кто дальше?"
    # 1 тест проверяем
    def test_solve_1(self):
        h = [8, 5, 3, 2, 0, 1, 1]
        t = [3, 3, 3, 3, 3, 3, 3]
        expect = "черепаха"

        result = solve(h, t)

        self.assertEqual(expect, result)

    # 2 тест ожидаем ошибку
    @unittest.expectedFailure
    def test_solve_2(self):
        h = [8, 5, 3, 2, 2, 1, 1]
        t = [3, 3, 3, 3, 3, 3, 3]
        expect = "черепаха"

        result = solve(h, t)

        self.assertEqual(expect, result)

    # 3 тест пропускаем
    @unittest.skip
    def test_solve_3(self):
        h = [8, 5, 3, 2, 1, 1, 1]
        t = [3, 3, 3, 3, 3, 3, 3]
        expect = "черепаха"

        result = solve(h, t)

        self.assertEqual(expect, result)

# тесты решения уравнений с параметрами
class TestSolution(unittest.TestCase):
    def test_solution_with_params(self):
        for i, (a, b, c, expected) in enumerate((
            (1, 8, 15, '-3.0 -5.0'),
            (1, -13, 12, '12.0 1.0'),
            (-4, 28, -49, '3.5'), #3.5 - провален
            (1, 1, 1, 'корней нет'),

        )):
            with self.subTest(i):
                result = solution(a, b, c)
                self.assertEqual(result, expected)

