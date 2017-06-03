# Сравнение строк
# Написать функцию, которая принимает на вход две строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3.

def compare_strings(str_1, str_2):
    if len(str_1) == len(str_2):
        return 1
    elif len(str_1) != len(str_2):
        if str_2 == "learn":
            return 3
        elif len(str_1) > len(str_2):
            return 2

while True:
    str_1 = input("1st string: ")
    str_2 = input("2nd string: ")
    print(compare_strings(str_1, str_2))
