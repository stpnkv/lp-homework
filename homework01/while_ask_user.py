# Написать функцию ask_user() 
# чтобы помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”

def ask_user():
    while True:
        user_input = input("How are you? [Great?] ")
        if user_input == "Great":
            break
ask_user()