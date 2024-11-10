import os
import random
import calendar
import re


from datetime import datetime


# Вариант 1
print("Вариант 1\n")
# Встроенные модули
# 1)
n1 = random.randint(1, 100)
if n1 % 2 == 0:
    print(f'Чётное число {n1}!')
else:
    print(f'Нечётное число {n1}!')

# 2)
dir_name = datetime.now().strftime('%d.%m.%Y')
file_name = "new_empty.txt"
file_path = './' + dir_name + '/' + file_name
new_dir_path = './' + dir_name + '/' + "new_dir"
new_file_path = new_dir_path + '/' + file_name

os.mkdir(dir_name)
with open(file_path, 'w') as file:
    pass
os.mkdir(new_dir_path)
os.rename(file_path, new_file_path)


# Сторонние библиотеки

# python -m venv venv
# путь_до_папки\venv\Scripts\activate.ps1
# pip install pygame
# pip install -r requirements.txt


# Вариант 2
print("\nВариант 2\n")
# Встроенные модули
# 1)
def func2_1(lst):
    return random.choices(lst, k=2)


list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]
print(func2_1(list_el))

# 2)
def func2_2(date):
    reg = r'^\d{4}-\d\d$'
    if re.match(reg, date):
        yy = int(date[:4])
        mm = int(date[-2:])
        return calendar.month(yy, mm)
    else:
        return "Неверный формат даты."


print(func2_2("2922-09"))
reg_numb = r'^\+7\d{10}$|^7\d{10}$|^8\d{10}$'
tel_namb = '76460979103'
if re.match(reg_numb, tel_namb):
    print(f'Номер "{tel_namb}" введён верно.')
else:
    print(f'Номер "{tel_namb}" введён неверно.')


# Сторонние библиотеки
# python -m venv venv
# путь_до_папки\venv\Scripts\activate.ps1
# pip install pygame
# pip install numpy
# pip install -r requirements.txt


# Вариант 3
print("\nВариант 3\n")
# Встроенные модули
# 1)
def fun3_1(lst):
    return random.shuffle(lst)


print(list_el)
fun3_1(list_el)
print(list_el)

# 2)



# Сторонние библиотеки

