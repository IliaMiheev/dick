import instrykchia
import autor
import profil
import user
import peremennie
list = []

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

def content():
    stop = False
    count = 0
    print(peremennie.trait, end='')
    print(peremennie.photo, end='')
    print(peremennie.trait)
    while not stop:
        UserName = input('Введи имя или команду: ')
        list.append(UserName)
        if UserName == 'стоп':
            stop = True
            arr = ['автор', 'помощь', 'стоп', '', 'профиль']
            for el1 in arr:
                for el2 in list:
                    if el1 == el2:
                        list.remove(el2)
            if len(list) == 0:
                peremennie.clear_console()
                print(
f'''
Ты не ввёл ни одного имени, так что программа прекращает свою работу. Пока, {user.user["name"]}.
Если захочешь посмеяться, то можешь смело залетать в эту программу ;).
Так что до встречи!!!
''')
            else:
                print(peremennie.trait)
                for elem in list:
                    print(peremennie.capitalize_after_space(elem) + ' - ' + word_xyz(elem, peremennie.endings))
                print(peremennie.trait)
        # for key, value in peremennie.comands.items():
        if UserName == 'помощь':
            stop = True
            instrykchia.instrykchia()
        if UserName == 'автор':
            stop = True
            autor.autor()
        if UserName == 'профиль':
            stop = True
            profil.profil()