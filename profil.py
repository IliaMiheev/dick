import user
from peremennie import capitalize_after_space, zapis, trait, stroka, clear_console
import content
def profil(word = ''):
    clear_console()
    if word != '':
        print(f"\033[93m{word}\033[0m")
        print()
    print("\033[93mДанные:\033[0m")
    for item, value in user.user.items():
        if item != 'instruction' and item != 'arr':
            print(f"\033[91m    {item} ——> {str(value)}.\033[0m")
            print()
        if item == 'arr':
            if user.user['arr'] == []:
                print("\033[91m    Списки ——> Здесь пусто\033[0m")
                print()
            else:
                print("\033[91m    Списки:\033[0m")
                for el in user.user['arr']:
                    for elem, value in el.items():
                        print(f"\033[91m        {elem} ——> {stroka(value)}\033[0m")
                        print()
    newName = input("\033[93mВведи новое имя если хочешь его изменить, а чтобы продолжить нажми Enter \033[0m")
    if newName.replace(" ", "") != '':
        user.user['Имя'] = capitalize_after_space(newName)
        zapis()
    clear_console()
    logo = ''
    if newName.replace(" ", "") != '':
        logo = f'\033[93mНовое имя: {user.user["Имя"]}\033[0m'
    content.content(f'{logo}')