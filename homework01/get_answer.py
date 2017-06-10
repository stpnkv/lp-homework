# При помощи функции get_answer() 
# отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”
# Переписать функцию ask_user(), добавив обработку exception-ов
# Добавить перехват ctrl+C и прощание

def get_answer(question):
    answer = {
        'hey': 'Hello!',
        'hello': 'And hello to you!', 
        'how are you?': 'Great, how are you?', 
        'see you soon': 'You too'
    }
    default_answer = ':)'
    return answer.get(question.lower(), default_answer)

def ask_user():
    user_question = input("What is your question? [Bye] ")
    if user_question.lower() == "bye":
        return False
    print(get_answer(user_question))
    return True

if __name__ == "__main__":
while True:
    try:
        if not ask_user():
            print("Bye, bye")
            break
    except KeyboardInterrupt:
        print("\n", "Bye, bye")
        break
