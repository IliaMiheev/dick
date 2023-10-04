import content
import instrykchia
import user

if user.user['instruction']:
    content.content('\033[92mДобро пожаловать. Рад тебя снова видеть.\033[0m')
else:
    instrykchia.instrykchia()