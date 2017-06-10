# Возьмите словарь с ответами из функции get_answer
# Запишите его содержимое в формате csv в формате: "ключ"; "значение". 
# Каждая пара ключ-значение должна располагаться на отдельной строке

import csv

answer = {
    'hey': 'Hello!',
    'hello': 'And hello to you!', 
    'how are you?': 'Great, how are you?', 
    'see you soon': 'You too'
}

answers_list = []
for key, value in answer.items():
    answer_dict_item = {}
    answer_dict_item["question"] = key.lower()
    answer_dict_item["answer"] = value.lower()
    answers_list.append(answer_dict_item)

with open('answers.csv', 'w', encoding='utf-8') as f:
    fields = ['question', 'answer']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for item in answers_list:
        writer.writerow(item)
        