import content
import instrykchia
import user

# if user.user['instruction'] or user.user['имя']:
#     content.content('''Добро пожаловать. Рад тебя снова видеть.''')
# else:
#     instrykchia.instrykchia()

if not user.user['instruction'] or user.user['Имя'] == '':
    instrykchia.instrykchia()
else:
    content.content('''Добро пожаловать. Рад тебя снова видеть.''')