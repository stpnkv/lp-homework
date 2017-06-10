# Написать функцию ask_user() 
# чтобы помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”

def ask_user():
    exit_word = "Great"
    while True:
        user_input = input("How are you? [{}?] ".format(exit_word))
        if user_input.upper() == exit_word.upper():
            break
ask_user()