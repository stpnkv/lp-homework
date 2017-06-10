# Скачайте файл по ссылке
# Прочитайте его и подсчитайте количество слов в тексте

def word_count(text):
    str = text.replace("\n", " ") + " "
    word = ""
    words = []
    for i in str:
        if i != " ":
            word = word + i
        else:
            if len(word) > 0:
                words.append(word)
                word = ""
    return(len(words))

with open('referat.txt', 'r', encoding='utf-8') as f:
    n = 0
    for line in f:
        n = n + word_count(line)
    print("Word count: " + str(n))
