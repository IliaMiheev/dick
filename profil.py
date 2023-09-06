import user
from peremennie import capitalize_after_space, zapis
from instrykchia import clear_console
def profil():
    clear_console()
    print(f'имя: {user.user["name"]}')
    newName = input('Введи новое имя если хочешь его изменить, а если хочешь оставить как прежде, то введи "нет"')
    if newName != 'нет':
        user.user['name'] = newName
        zapis()
