#Задание №1
print("Задание №1")
m1 = int(input("Введите степень возведения: "))
n1 = int(input("Введите количество элементов массива: "))
arr1 = []
print("Введите элементы массива: ")
for i in range(n1):
    x = input(f"Элемент №{i} = ")
    if (x.isdigit()):
        arr1.append(int(x) ** m1)
    elif (x[0] == "-" and x[1:].isdigit()):
        arr1.append(int(x) ** m1)
    else:
        arr1.append(x * m1)
print(arr1)


# Задание №2
print("\nЗадание №2")
s2 = input("Введите слово: ").lower()
all_symb = list(set(s2))
dict = {x: s2.count(x) for x in all_symb}
print(dict)


# Задание №3
print("\nЗадание №3")
dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
keys = set(dct.keys())
value = set(dct.values())
print(keys)
print(value)
print(keys | value)



# Задание №1*
print("\nЗадание №1*")
dictionary = {
    "Имя": ["Андрей", "Кирилл", "Анна", "Евгений", "Евгений", "Александр", "Татьяна", "Аркадий", "Игорь", "Кирилл"],
    "Фамилия": ["Иванов", "Лазарев", "Петрова", "Надобников", "Никитин", "Иванов", "Никитина", "Лихачев", "Никитин", "Левашев"],
    "Город проживания": ["Москва", "Омск", "Псков", "Псков", "Москва", "Псков", "Москва", "Омск", "Псков", "Москва"],
    "Год рождения": [2000, 1987, 2003, 1993, 2001, 2001, 1976, 1957, 1969, 1999],
    "Месяц рождения": [6, 4, 11, 12, 9, 9, 5, 2, 3, 6],
    "Число рождения": [11, 25, 5, 3, 27, 31, 13, 12, 28, 24],
    "Статус": ["Студент", "Работает", "Школьница", "Работает", "Студент", "Студент", "Работает", "Пенсия", "Работает", "Студент"]
}

for i in range(len(dictionary["Имя"])):
    if (dictionary["Имя"][i] == "Кирилл"):
        dictionary["Имя"][i] += "л"

for i in range(len(dictionary["Фамилия"])):
    if ("Никитин" in dictionary["Фамилия"][i] and dictionary["Город проживания"][i] == "Москва"):
        dictionary["Город проживания"][i] = "Махачкала"

for i in range(len(dictionary["Фамилия"])):
    if (dictionary["Фамилия"][i] == "Иванов" and dictionary["Имя"][i] == "Александр"):
        dictionary["Статус"][i] = "Работает"
        break

ind = -1
for i in range(len(dictionary["Фамилия"])):
    if (dictionary["Фамилия"][i] == "Лихачев" and dictionary["Имя"][i] == "Аркадий"):
        ind = i
        break
for key in dictionary.keys():
    dictionary[key].remove(dictionary[key][ind])

surname = [x.upper() for x in dictionary["Фамилия"]]
year = list(map(str, dictionary["Год рождения"]))
month = []
for x in list(map(str, dictionary["Месяц рождения"])):
    if (len(x) != 2):
        month.append("0" + x)
    else:
        month.append(x)
day = []
for x in list(map(str, dictionary["Число рождения"])):
    if (len(x) != 2):
        day.append("0" + x)
    else:
        day.append(x)
year_month = list(map("-".join, zip(year, month)))

dictionary_new = {
    "Фамилия Имя": list(map("--".join, zip(surname, dictionary["Имя"]))),
    "Дата рождения": list(map("-".join, zip(year_month, day))),
    "Город проживания": dictionary["Город проживания"],
    "Статус": dictionary["Статус"]
}
print(dictionary_new)


# Задание №2*
print("\nЗадание №2*")
set1 = {6, 31, 14, 25, 19, 3, 55}
set2 = {30, 22, 6, 79, 25}
set3 = {9, 1, 22, 19, 30}

set12 = set1 | set2
set123 = set12 | set3

print("Объединение множеств 1 и 2:", set12)
set01, set02 = set1.copy(), set2.copy()
for x in set12:
    if (x in set01):
        set01.remove(x)
    elif (x in set02):
        set02.remove(x)
not_in_set12 = list(set01) + list(set02)
print("Не вошедшее в set123:", not_in_set12)

print("Объединение множеств 1-2 и 3:", set123)
set01, set02, set03 = set1.copy(), set2.copy(), set3.copy()
for x in set123:
    if (x in set01):
        set01.remove(x)
    elif (x in set02):
        set02.remove(x)
    elif (x in set03):
        set03.remove(x)
not_in_set123 = list(set01) + list(set02) + list(set03)
print("Не вошедшее в set123:", not_in_set123)
