import user
from peremennie import capitalize_after_space, zapis, trait, stroka
import content
from instrykchia import clear_console
def profil(word = ''):
    clear_console()
    if word != '':
        print(f"\033[93m{word}\033[0m")
        print()
    print("\033[93mДанные:\033[0m")
    for item, value in user.user.items():
        if item != 'instruction' and item != 'arr':
            print(f"\033[94m    {item} ——> {str(value)}.\033[0m")
        if item == 'arr':
            if user.user['arr'] == []:
                print("\033[91m    Списки ——> Здесь пусто\033[0m")
            else:
                print("\033[91m    Списки:\033[0m")
                # print(f"    {trait}")
                for el in user.user['arr']:
                    for elem, value in el.items():
                        print(f"\033[91m        {elem} ——> {stroka(value)}\033[0m")
                        # print(f"    {trait}")
            
    print()
    newName = capitalize_after_space(input("\033[93mВведи новое имя если хочешь его изменить, а если хочешь оставить как прежде, то нажми Enter \033[0m"))
    if newName != '':
        user.user['Имя'] = newName
        zapis()
    clear_console()
    logo = ''
    if newName.replace(" ", "") == '':
        logo = f'\033[93mТы оставил себе имя: {user.user["Имя"]}\033[0m'
    else:
        logo = f'\033[93mНовое имя: {user.user["Имя"]}\033[0m'
    content.content(f'\033[93m{logo}\033[0m')