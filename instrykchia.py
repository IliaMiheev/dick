import os
import content
import user as us
from peremennie import capitalize_after_space, clear_console

polzovatel = us.user

def instrykchia():
    clear_console()
    print(
f'''
Привет! {polzovatel['name']}
В этой игре ты вводишь имя и фамилию, а программа первые три буквы заменит на "Хуй".
Так как первые три буквы изменит программа, можешь писать имена в нижнем регистре.

Команды:
Введи "стоп" чтобы закончить игру и увидеть результат.
Введи "помощь" чтобы открыть эту инструкцию.
Введи "автор" чтобы узнать о создателе.
''')
    ansver = input('Нажми Enter если всё понял ')
    if ansver == '':
        polzovatel['instruction'] = True
        if polzovatel['name'] == '':
            polzovatel['name'] = capitalize_after_space(input('Тогда введи своё имя '))

        zapis()
        print('Тогда начнём')
        content.content()
    else:
        polzovatel['instruction'] = False
        zapis()
        print('Тогда ничем не могу помочь. :-(')
        print()