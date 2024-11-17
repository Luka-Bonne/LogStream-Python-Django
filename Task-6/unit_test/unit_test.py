import unittest
import time

from main import factorial


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("SetUp")

    def test_factorial_0(self):
        # Тест №1. Факториал от 0
        start_time = time.time()
        self.assertEqual(factorial(0), 1)
        end_time = time.time()
        print(f"Время выполнения теста №1: {end_time - start_time:.4f} секунд")

    def test_factorial_1(self):
        # Тест №2. Факториал от 1
        start_time = time.time()
        self.assertEqual(factorial(1), 1)
        end_time = time.time()
        print(f"Время выполнения теста №2: {end_time - start_time:.4f} секунд")

    def test_factorial_other_nums(self):
        # Тест №3. Факториал от любого другого числа (не 0 и не 1)
        start_time = time.time()
        self.assertEqual(factorial(5), 120)
        end_time = time.time()
        print(f"Время выполнения теста №3: {end_time - start_time:.4f} секунд")

    def test_factorial_big(self):
        # Тест №4. Факториал от отрицательного числа
        start_time = time.time()
        self.assertEqual(factorial(20), 2432902008176640000)
        end_time = time.time()
        print(f"Время выполнения теста №4: {end_time - start_time:.4f} секунд")

    def test_factorial_negative(self):
        # Тест №5. Факториал от отрицательного числа
        start_time = time.time()
        self.assertRaises(ValueError, factorial, -2)
        end_time = time.time()
        print(f"Время выполнения теста №5: {end_time - start_time:.4f} секунд")

    def test_factorial_too_big(self):
        # Тест №6. Ошибка. Число-ответ слишком большое для int
        start_time = time.time()
        self.assertRaises(ValueError, factorial, 30)
        end_time = time.time()
        print(f"Время выполнения теста №6: {end_time - start_time:.4f} секунд")

    def tearDown(self) -> None:
        print("tearDown")
