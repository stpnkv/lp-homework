# При помощи функции get_answer() 
# отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

def get_answer(question):
    answer = {
        'hey': 'Hello!'
        'hello': 'And hello to you!', 
        'how are you?': 'Great, how are you?', 
        'see you soon': 'You too'
    }
    default_answer = ':)'
    return answer.get(question.lower(), default_answer)

def ask_user():
    while True:
        user_question = input("What is your question? [Bye] ")
        if user_question.lower() == "bye":
            break
        print(get_answer(user_question))

ask_user()