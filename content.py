import instrykchia
import autor
import profil
import zapisList
import user
import peremennie
from listPlay import listPlay
import lists
def printList():
    if peremennie.stroka(list) == '':
        print('\033[91mСписок пуст\033[0m')
    else:
        print(f'''
Введённые слова: "{peremennie.stroka(list)}"
    ''')
list = []
logo = f'''
Ты не ввёл ни одного слова, так что программа прекращает свою работу. Пока, {user.user["Имя"]}.
Если захочешь посмеяться, то можешь смело залетать в эту программу ;).
Так что \033[91mдо встречи!!!\033[0m  '''
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

def content(word = ''):
    peremennie.clear_console()
    stop = False
    if word != '':
        print(word)
    print(peremennie.trait, end='')
    print(peremennie.photo, end='')
    print(peremennie.trait)
    while not stop:
        UserName = input('Введи имя или команду: ')
        list.append(UserName)

        if UserName == '':
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
        elif  UserName == 'помощь':
            list.pop()
            stop = True
            instrykchia.instrykchia()
        elif  UserName == 'автор':
            list.pop()
            stop = True
            autor.autor()
        elif  UserName == 'профиль':
            list.pop()
            stop = True
            profil.profil('\033[91mВот твой профиль.\033[0m')
        elif  UserName == 'запись':
            list.pop()
            stop = True
            zapisList.zapisList()
        elif  UserName == 'удаление списков':
            list.pop()
            stop = True
            lists.lists()
        elif  UserName == 'использовать списки':
            list.pop()
            peremennie.clear_console()
            print(peremennie.trait, end='')
            print(peremennie.photo, end='')
            print(peremennie.trait)
            count = 0
            res = True
            ansver = []
            print(f"Твои списки: \033[91m{peremennie.stroka(user.user['arr'])}\033[0m")
            nameList = input('Веди название списка который хочешь использовать: ')
            while res:
                if listPlay(nameList) != False:
                    ansver = listPlay(nameList)
                    for elem in ansver:
                        if count != 1:
                            list.append(elem)
                        count +=1
                    print('Список добавлен.')
                    printList()
                    break
                else:
                    print('Такого списка нет.')
                    printList()
                    break
        elif  UserName == 'посмотреть список':
            list.pop()
            printList()