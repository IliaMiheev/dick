import user
from peremennie import capitalize_after_space, zapis
import content
from instrykchia import clear_console
def profil():
    clear_console()
    print('Данные:')
    for item, value in user.user.items():
        if item != 'instruction':
            print(f'    {item} ——> {str(value)}')
    print()
    newName = capitalize_after_space(input('Введи новое имя если хочешь его изменить, а если хочешь оставить как прежде, то нажми Enter '))
    if newName != '':
        user.user['name'] = newName
        zapis()
    clear_console()
    if newName == '':
        print('Ты оставил себе имя - '+ user.user['name'])
    else:
        print('Новое имя - ' + user.user['name'])
    content.content()