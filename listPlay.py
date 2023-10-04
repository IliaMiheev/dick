from user import user
from peremennie import printUserKeys
def listPlay(nameList):
    list = []
    count = 0
    userList = printUserKeys()
    if nameList in userList:
        for elements in userList:
            if elements == nameList:
                for key, value in user['arr'][count].items():
                    list = value
            count += 1
        return list
    else:
        return False
    