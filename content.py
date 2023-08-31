import instrykchia
import autor
import os
list = []

def content():
    trait = '—————————————————————————————————————————————————————————————————————————————————————————————————————'
    def word_xyz(word):
        for i in list:
            try:
                if word[3] in endings == 'ь':
                    word = endings[word[3]]['xyz'] + word[5:]
                if word[3] in endings:
                    word = endings[word[3]]['xyz'] + word[4:]
                else:
                    word = 'Хуй' + word[3:]
            except IndexError:
                pass
            return word

    stop = False
    count = 0
    endings = {
    'е': {
        'xyz': 'Хуе',
    },
    'о': {
        'xyz': 'Хуё',
    },
    'у': {
        'xyz': 'Хую',
    },
    'ь': {
        'xyz': 'Ху',
    },
    'а': {
        'xyz': 'Хуя',
    },
    'ё': {
        'xyz': 'Хуё',
    },
    'и': {
        'xyz': 'Хуи',
    },
    'я': {
        'xyz': 'Хуя',
    }
    }
    photo = '''
|.####..##........####.....###.............##.....##..####..##.....##..########..########..##.....##|
|..##...##.........##.....##.##............###...###...##...##.....##..##........##........##.....##|
|..##...##.........##....##...##...........####.####...##...##.....##..##........##........##.....##|
|..##...##.........##...##.....##..........##.###.##...##...#########..######....######....##.....##|
|..##...##.........##...#########..........##.....##...##...##.....##..##........##.........##...##.|
|..##...##.........##...##.....##..........##.....##...##...##.....##..##........##..........##.##..|
|.####..########..####..##.....##..........##.....##..####..##.....##..########..########.....###...|
'''
    print(trait, end='')
    print(photo, end='')
    print(trait)
    while stop == False:
        UserName = input('''Введи своё имя: ''')
        list.append(UserName)
        if UserName == 'стоп':
            stop = True
            arr = ['автор','помощь','стоп', '']
            for el1 in arr:
                for el2 in list:
                    if el1 == el2:
                        list.remove(el2)
            if len(list) == 0:
                pass
            else:
                print(trait)
                for i in list:
                    first_name_xyz = ''
                    last_name_xyz = ''
                    try:
                        first_name_xyz, last_name_xyz = i.split()
                    except ValueError:
                        first_name_xyz = i
                    first_name2 = first_name_xyz.capitalize()
                    last_name2 = last_name_xyz.capitalize()
                    count += 1
                    first_name_xyz = word_xyz(first_name_xyz)
                    last_name_xyz = word_xyz(last_name_xyz)
                    if last_name2 == '':
                        print(count, ')' + first_name2 + ' - ' + first_name_xyz)
                    else:
                        print(count, ')', first_name2, last_name2,' - ', first_name_xyz, last_name_xyz)
                    # print(list)
                print(trait, end='')
        if UserName == 'помощь':
            stop = True
            instrykchia.instrykchia()
        if UserName == 'автор':
            stop = True
            autor.autor()