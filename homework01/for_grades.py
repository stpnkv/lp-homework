# Оценки
# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

from random import randint

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

school_classes = [
    {"name": "10a", "grades": []},
    {"name": "10b", "grades": []},
    {"name": "10c", "grades": []},
    {"name": "11a", "grades": []},
    {"name": "11b", "grades": []},
    {"name": "11c", "grades": []}
]

for i in school_classes:
    random_grades = []
    for j in range(1,11):
        random_grades.append(randint(2,5))
    i["grades"] = random_grades

print("Average grades per class")
for i in school_classes:
    class_name = i.get("name")
    class_grades = i.get("grades")
    print(class_name + ": " + str(class_grades) + ": " + str(mean(class_grades)))

print("Average grade per school")
all_grades = []
for i in school_classes:
    class_grades = i.get("grades")
    all_grades.append(mean(class_grades))
print(str(mean(all_grades)))
