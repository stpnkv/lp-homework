# Возраст
# Попросить пользователя ввести возраст.
# По возрасту определить, чем он должен заниматься: учиться в детском саду, школе, ВУЗе или работать.
# Вывести занятие на экран.

def where_to_go(age):
    if  age < 0:
        print("You haven't been born yet!")
    elif   0 <= age < 3:
        print("Go to sleep!")
    elif 3 <= age < 7:
        print("Go to the kindergarten!")
    elif 7 <= age < 17:
        print("Go to School!")
    elif age == 17:
        answer =input("Have you finished school? ")
        if answer.upper() == 'YES':
            print("Go to the University!")
        else:
            print("Try to finish school first!")
    elif 18 <= age < 21:
        print("Go to the University!")
    else:
        answer =input("Have you finished the University? ")
        if answer.upper() == 'YES':
            print("Go to work!")
        else:
            print("Try to finish the University first!")

while True:   
    try:
        age = int(input("Your age: "))
    except KeyboardInterrupt:
        print("Bye, bye")
        break
    except ValueError:
        print("Please, enter a number")
    where_to_go(age)

