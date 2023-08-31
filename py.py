import os
import content
import instrykchia
file = open('text.txt', 'r')
data = file.read()
file.close()

if data == 'True':
    content.content()
else:
    instrykchia.instrykchia()