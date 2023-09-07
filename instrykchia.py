import os
import content
import user as us
from peremennie import capitalize_after_space, clear_console, zapis

polzovatel = us.user

def instrykchia():
    clear_console()
    if polzovatel['name'] == '':
        print('Привет!', end='')
    else:
        print(f"Привет! {polzovatel['name']}.", end='')
    print(
f'''
В этой игре ты вводишь имя, а программа первые три буквы заменит на "Хуй".
У всех слов, что ты введёшь, первая буква будет в верхнем регистре, так что можешь забыть про Shift и погрузиться в игру.

Команды:
Введи "стоп" чтобы закончить игру и увидеть результат.
Введи "помощь" чтобы открыть эту инструкцию.
Введи "автор" чтобы узнать о создателе.
Введи "профиль" чтобы узнать узнать текущее имя и сменить его.
''')
    ansver = input('Нажми Enter если всё понял ')
    if ansver == '':
        polzovatel['instruction'] = True
        if polzovatel['name'] == '':
            polzovatel['name'] = capitalize_after_space(input('Тогда введи своё имя для профиля '))
        zapis()
        print(f'Тогда, {polzovatel["name"]}, начинай вводить имена.')
        content.content()
    else:
        polzovatel['instruction'] = False
        zapis()
        print('Тогда ничем не могу помочь. :-(')
        print()