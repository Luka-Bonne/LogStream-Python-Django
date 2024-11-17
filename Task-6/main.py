import sys
import unittest


# Задание №1
def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)


# Тест №1. С int списком
assert average_num([1, 2, 3, 4]) == 2.5
# Тест №2. С float списком
assert average_num([1.5, 2.5, 3.5]) == 2.5
# Тест №3. С одним int значением в списке
assert average_num([5]) == 5.0
# Тест №4. С одним float значением в списке
assert average_num([6.0]) == 6.0
# Тест №5. Со смешанними int/float значениями в списке
assert average_num([1, 2, 3, 4, 2.6, 5.7]) == 3.05
# Тест №6. С int значениями в виде трок
assert average_num(['1', '2', '3', '4']) == 2.5
# Тест №7. С float значениями в виде строк
assert average_num(['1.5', '2.5', '3.5']) == "Bad request"
# Тест №8. С различными значениями, не являющимися ни int, ни float
assert average_num([{8, 9}, [], 'jkj;', '9.o']) == "Bad request"
# Тест №9. Без asset, но с проверкой на пустой список => деление на 0
try:
    average_num([])
except ZeroDivisionError:
    print("The divisor is zero")


# Задание №2
def merge_and_write(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1:
            data1 = file1.read().strip()

        with open(file2_path, 'r') as file2:
            data2 = file2.read().strip()

        merged_data = data1 + ' ' + data2

        with open(output_file_path, 'w') as output_file:
            output_file.write(merged_data)

        with open(output_file_path, 'r') as output_file:
            data = output_file.read()
        return data
    except FileNotFoundError:
        return "Один из файлов не найден"


# Задание №3
def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result
