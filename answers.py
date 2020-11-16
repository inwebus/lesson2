# Передаем имя в функцию
# Функция ищет в своем списке переданное имя
# Если находит - печатает "Имя найдено"
# Если нет - "Имя не найдено"

def find_person(name):
    names = ["Сергей",
            "Владимир",
            "Кирилл",
            "Вася",
            "Маша",
            "Петя",
            "Валера",
            "Саша",
            "Даша"]
    while True:
        
        if names.pop() == name:
            print("{} найден".format(name))
            break
        elif names == []: 
            print("{} не найден".format(name))
            break
        else: print("Ищем...")

# name_for_find = input("Введите имя для поиска: ")
# find_person(name_for_find)

# функция ask_user
# задаем вопрос "Как дела"
# ответил "Хорошо" - заканчивает функцию
# если нет - повторно спрашивать "Как дела"

def get_answer():
    questions = {"Как дела?": "Хорошо",
                "Что делаешь?": "Программирую",
                "Как отсюда выйти?": "Введи слово Пока"
                }
    flag = True
    while flag:
        ask = input("Введите вопрос: ")
        for question in questions:
            if ask == question:
                print(questions[question])
                break
            elif ask == "Пока":
                flag = False    
                break      
            else:
                print("Ответа не в базе. Попробуйте ещё раз.")
                break

get_answer()