# Задание №1
print("№1")
while True:
    number1 = input("Введите число: ")
    if (number1 == "exit"): break

    if (all([letter.isnumeric() for letter in number1])):
        print("Длина числа =", len(number1))
    else:
        print("Введено не число.")


# Задание №2
print("№2")
number2 = int(input("Введите число: "))
sum1 = 0
sum2 = 0
for i in range(-number2, number2 + 1):
    if (i < 0): sum1 += i
    else: sum2 += i
    print(i)

print("Сумма отрицательных чисел =", sum1)
print("Сумма положительных чисел =", sum2)


# Задание №3
print("№3")
number3 = input("Введите трёхзначное число с уникальными цифрами: ")
while True:
    if ((len(number3) == 3) and (len(set(number3)) == 3)):
        break
    if (len(number3) != 3):
        print("Число не трёхзначное.")
    elif (len(set(number3)) != 3):
        print("В числе есть повторяющиеся цифры.")
    number3 = input("Введите трёхзначное число с уникальными цифрами: ")

for x in number3:
    for y in number3:
        for z in number3:
            if (x != y and y != z and x != z):
                print(x, y, z, sep="")


# Задание №4
# 1)
print("№4.1")
ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
shoot = input()
if (shoot.lower() in ship.lower()): print("Попал!")
else: print("Мимо!")


# 2)
print("№4.2")
name = input("Введие имя: ")
surname = input("Введие фамилию: ")
age = input("Введие возраст: ")
print('Ваше имя: {0}, Фамилия: {1}, Возраст: {2} лет.'.format(name, surname, age))
print(f'Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет.')
