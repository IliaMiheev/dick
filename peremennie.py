trait = '\033[92m——————————————————————————————————————————————————————————————————————————————————————————————————\033[0m'

photo = '''
####..##........####.....###.............##.....##..####..##.....##..########..########..##.....##
.##...##.........##.....##.##............###...###...##...##.....##..##........##........##.....##
.##...##.........##....##...##...........####.####...##...##.....##..##........##........##.....##
.##...##.........##...##.....##..........##.###.##...##...#########..######....######....##.....##
.##...##.........##...#########..........##.....##...##...##.....##..##........##.........##...##.
.##...##.........##...##.....##..........##.....##...##...##.....##..##........##..........##.##..
####..########..####..##.....##..........##.....##..####..##.....##..########..########.....###...
'''

endings = {
    'ы': {
        'xyz': 'Хуй',
        'bykva': 4,
    },
    'е': {
        'xyz': 'Хуе',
        'bykva': 4,
    },
    'о': {
        'xyz': 'Хуё',
        'bykva': 4,
    },
    'у': {
        'xyz': 'Хую',
        'bykva': 4,
    },
    'ь': {
        'xyz': 'Хуй',
        'bykva': 4,
    },
    'а': {
        'xyz': 'Хуя',
        'bykva': 4,
    },
    'ё': {
        'xyz': 'Хуё',
        'bykva': 4,
    },
    'и': {
        'xyz': 'Хуи',
        'bykva': 4,
    },
    'я': {
        'xyz': 'Хуя',
        'bykva': 4,
    }
}
a = '''
┌──(kali㉿kali)-[~]
└─
'''
def capitalize_after_space(word):
    count = 0
    elem = " ".join(word.replace(" ", " ").split()).capitalize()
    for bykva in elem:
        count += 1
        if bykva == ' ':
            elem = elem[:count] + elem[count].upper() + elem[count+1:]
    return elem

def clear_console():
    import os
    operating_system = os.name
    if operating_system == 'posix':
        _ = os.system('clear')
    elif operating_system == 'nt' or operating_system == 'dos':
        _ = os.system('cls')
    else:
        print("Очистка консоли не поддерживается на данной операционной системе.")

def zapis(bool = True):
    import user
    word = f"user = {str(user.user)}"
    with open('user.py', 'w', encoding="utf-8") as file:
        file.write(word)
    if bool == True:
        clear_console()

def stroka(spisok):
    def get_keys(list_of_dicts):
        keys = []
        for dictionary in list_of_dicts:
            keys.extend(dictionary.keys())
        return keys

    if isinstance(spisok, list):
        count = 0
        string = ''
        for elem in spisok:
            if isinstance(elem, str or int):
                string += str(elem) + ', '
            elif isinstance(elem, dict) and count == 0:
                arr = get_keys(spisok)
                for e in arr:
                    string += str(e) + ', '
                count += 1
        if string != '':
            string = string[:-2] + '.'
        return string
def printUserKeys():
    from user import user
    list = []
    for element in user['arr']:
        for key in element:
            list.append(key)
    return list
    