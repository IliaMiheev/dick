from peremennie import clear_console, trait, photo, zapis, stroka, printUserKeys
from profil import profil
import content
import user
def lists():
    string = stroka(user.user['arr'])
    if string.replace(" ", "") == '':
        content.content('У тебя нет списков. Удалять нечего.')
    else:
        clear_console()
        print(f'Твои списки: \033[91m{string}\033[0m')
        print(photo)
        print('''
Введи название списка который ты хочешь удалить.
Если хочешь удалить несколько списков, то пиши их названия через пробел.
Нажми Enter чтобы выйти из режима удаления списков.
Введи "э" чтобы удалить все списки.
    ''')
        remuveElement = input("Названия: ")
        user_ansver = remuveElement.split()
        if user_ansver == []:
            content.content('Ты вышел из режима удаления списков.')
        elif remuveElement.replace(' ', '') == 'э':
            user.user['arr'] = []
            zapis()
            profil('Все списки очищенны.')
        else:
            notDell = []
            dell = []
            for item in user.user['arr']:
                for elem in item:
                    if elem in user_ansver:
                        dell.append(elem)
                        user.user['arr'].remove(item)
            zapis()
            for elements in user_ansver:
                if elements not in dell:
                    notDell.append(elements)
            firstLogo = ''
            secondLogo = ''
            logo = ''
            if stroka(dell)[:-1] != '':
                firstLogo = f'В корзине: \033[91m"{stroka(dell)[:-1]}"\033[0m'
            if stroka(notDell)[:-1] != '':
                secondLogo = f', и не удалено "\033[91m{stroka(notDell)[:-1]}\033[0m"'
            if firstLogo == '':
                logo = f'Ничего не было удалено, так как (\033[91m{remuveElement}\033[93m) нет в списке.\033[0m'
            else:
                logo = firstLogo + secondLogo
            profil(logo)    