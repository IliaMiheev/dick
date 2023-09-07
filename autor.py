import os
from instrykchia import clear_console
import content

def autor ():
    clear_console()
    print(
'''
Автор гениален. И сногшибательно красив

Опыт написавния кода на JavaScript: 5
Опыт работы на Python: 4 (пока)
Познания в пентестинге: 3 (пока)
Познания в бизнесе: 3+ (пока)
Имя: смотри на заставке
Место обучения: ГАПОУ ВО ГСК (информационные системы и программирование)
''')
    a = input('Нажми Enter чтобы продолжить ')
    clear_console()
    print('Надеюсь тебе понравилась моя биография.')
    content.content()