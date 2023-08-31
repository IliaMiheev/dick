import os
import content

def instrykchia():
    os.system('cls')
    print(
'''
Привет! 
В этой игре ты вводишь имя и фамилию, а программа первые три буквы заменит на "Хуй".
Можно писать имена в нижнем регистре.

Команды:
Введи "стоп" чтобы закончить игру и увидеть результат.
Введи "помощь" чтобы открыть эту инструкцию.
Введи "автор" чтобы узнать о создателе.
''')
    ansver = input('Нажми Enter если всё понял ')
    if ansver == '':
        file = open('text.txt', 'w')
        file.write('True')
        file.close()
        os.system('cls')
        print('Тогда начнём')
        content.content()
    else:
        file = open('text.txt', 'w')
        file.write('False')
        file.close()
        os.system('cls')
        print('Тогда ничем не могу помочь. :-(')
        print()