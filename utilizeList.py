from peremennie import clear_console, stroka, photo, listPlay
import content
from user import user
def utilizeList(mess = ''):
    clear_console()
    if mess != '':
        print(mess)
    if stroka(user['arr']) != '':
        count = 0
        print(f"Твои списки: \033[91m{stroka(user['arr'])}\033[0m")
        print(photo)
        nameList = input('Веди название списка который хочешь использовать: ')
        while 1:
            if listPlay(nameList) != False:
                res = []
                list = []
                for elem in listPlay(nameList):
                    list.append(elem)
                    res.append(elem)
                content.content(f'Новые слова: {stroka(res)}',dopword=res)
                break
            else:
                if count == 2:
                    content.content('Ни один список не был использован.')
                    break
                else:
                    count += 1
                    nameList = input('Такого списка нет, попробуй её раз: ')
    else:
        content.content('У тебя нет списков, использовать нечего.')