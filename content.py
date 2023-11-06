import instrykchia
import autor
import profil
import zapisList
from user import user
import peremennie
import lists
import utilizeList
import reboot

list = []
logo = f'''
Ты не ввёл ни одного слова, так что программа прекращает свою работу. Пока, {user["Имя"]}.
Если захочешь посмеяться, то можешь смело залетать в эту программу ;).
Так что \033[92mдо встречи!!!\033[0m  '''

def word_xyz(word, arr):
    elem = word.split()
    res = ''
    for i in elem:
        try:
            if i[3] in arr == 'ь':
                i = arr[i[3]]['xyz'] + i[5:]
            if i[3] in arr:
                i = arr[i[3]]['xyz'] + i[4:]
            else:
                i = 'Хуй' + i[3:]
        except IndexError:
            i = 'Хуй'
        res += i + ' '
    return res

def content(word = '', bool = False, dopword = []):
    peremennie.clear_console()
    stop = bool
    for elem in dopword:
        list.append(elem)
    if word != '':
        print(f'\033[92m{word}\033[0m')
        print()
    print(peremennie.photo)
    while not stop:
        UserName = input('Введи имя или команду: ')
        list.append(UserName)
        if UserName.lower().replace(" ", "") == '':
            list.pop()
            stop = True
            if len(list) == 0:
                peremennie.clear_console()
                print(logo)
            else:
                print(peremennie.trait)
                for elem in list:
                    print(peremennie.capitalize_after_space(elem) + ' ——> ' + peremennie.capitalize_after_space(word_xyz(elem, peremennie.endings)))
                    print()
                print(peremennie.trait)
        elif  UserName.lower() == 'помощь':
            list.pop()
            stop = True
            instrykchia.instrykchia()
        elif  UserName.lower() == 'автор':
            list.pop()
            stop = True
            autor.autor()
        elif  UserName.lower() == 'профиль':
            list.pop()
            stop = True
            profil.profil('\033[93mВот твой профиль.\033[0m')
        elif  UserName.lower() == 'запись':
            list.pop()
            stop = True
            zapisList.zapisList()
        elif  UserName.lower() == 'удаление списков' or UserName.lower() == 'дел':
            list.pop()
            stop = True
            lists.lists()
        elif  UserName.lower() == 'использовать списки' or UserName.lower() == 'ют':
            list.pop()
            stop = True
            utilizeList.utilizeList()
        elif  UserName.lower() == 'посмотреть список' or UserName.lower() == 'во':
            list.pop()
            stop = True
            text = peremennie.stroka(list)
            if text == '':
                reboot.reboot('Список пуст.')
            else:
                reboot.reboot(f'Твои слова: {text}')
            
        elif  UserName.lower() == 'dell':
            list.pop()
            stop = True
            user['instruction'] = False
            user['arr'] = []
            user["Имя"] = ''
            peremennie.zapis()
            print('''
У тебя из профиля были удалены имя, списки и системные переменные.
Когда ты заново войдёшь в игру, то тебе будет предложено заново зарегистрироваться.
\033[92mДо встречи.\033[0m''')