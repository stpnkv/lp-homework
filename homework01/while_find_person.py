# Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] 
# пока не встретите имя "Валера". Когда найдете напишите "Валера нашелся". 
# Подсказка: используйте метод list.pop()

def find_person(names, find_name):
    while len(names) > 0:
        name = names.pop()
        if name == find_name:
            return "{} нашелся!".format(name)
            break

names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

a = find_person(names, 'Валера')
print(a)