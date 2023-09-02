import os
import content
import user as us

user = us.user

def instrykchia():
    os.system('cls')
    print(
'''
Привет! 
В этой игре ты вводишь имя и фамилию, а программа первые три буквы заменит на "Хуй".
Так как первые три буквы изменит программа, можешь писать имена в нижнем регистре.

Команды:
Введи "стоп" чтобы закончить игру и увидеть результат.
Введи "помощь" чтобы открыть эту инструкцию.
Введи "автор" чтобы узнать о создателе.
''')
    ansver = input('Нажми Enter если всё понял ')
    word = f"user = {{\n    'instruction': {user['instruction']},\n    'name':  '{user['name']}',\n}}"
    # word = word.replace("'", "\n'")
    if ansver == '':
        user['instruction'] = True
        with open('user.py', 'w') as file:
            file.write(word)
        os.system('cls')
        print('Тогда начнём')
        content.content()
    else:
        user['instruction'] = False
        with open('user.py', 'w') as file:
            file.write(word)
        os.system('cls')
        print('Тогда ничем не могу помочь. :-(')
        print(user)
        print()