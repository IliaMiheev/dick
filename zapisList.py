from peremennie import clear_console, zapis, photo, trait, stroka
from user import user as us
import profil

def zapisList():
    stop = False
    def proverka(word):
        res = False
        for element in us['arr']:
            for key in element:
                if key.lower() == word.lower():
                    res = True
        return res
    
    def lowTrait(word):
        count = 0
        for bykva in word:
            if bykva == ' ':
                word = word[:count]  + '_' +  word[count+1:]
            count += 1
        return word
    
    list = []
    clear_console()
    print(trait, end='')
    print(photo, end='')
    print(trait)
    if stroka(us['arr']) == '':
        print('\033[91mУ тебя нет списков.\033[0m')
    else:
        print(f"Твои списки: \033[91m{stroka(us['arr'])}\033[0m")
        
    print('''
Все пробелы в названии списка будут заменены на нижнее подчёркивание. Это сделано для коректной работы программы.
Чтобы выйти из этого режима любом поле для ввода нажми Enter.
''')
    name = lowTrait(input("Введи название списка: "))
    if name.replace(" ", "") == '':
        stop = True
        profil.profil('\033[91mВ списки ничего не было добавленно.\033[0m')
    else:
        while proverka(name):
            name = lowTrait(input("У тебя уже есть список с таким названием, придумай другое: "))
        print()
        while not stop:
            value = input("Введи элемент списка: ")
            list.append(value)
            if value == '':
                stop = True
                list.pop()
                if list == []:
                    profil.profil('В списки ничего не было добавленно.')
                else:
                    list.sort()
                    new_dict = {name: list}
                    us['arr'].append(new_dict)
                    zapis()
                    clear_console()
                    profil.profil(f'Теперь у тебя есть список: {name}.')
        return new_dict