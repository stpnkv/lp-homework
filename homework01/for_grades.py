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

for school_class in school_classes:
    random_grades = []
    for _ in range(10):
        random_grades.append(randint(3,5))
    school_class["grades"] = random_grades

print("Average grades per class")
all_grades = []
for school_class in school_classes:
    class_name = school_class.get("name")
    class_grades = school_class.get("grades")
    all_grades.append(mean(class_grades))
    print("{}: {}: {:.2f}".format(class_name, class_grades, mean(class_grades)))

print("Average grade per school")
print("{:.2f}".format(mean(all_grades)))

