import re

def getName(my_str):
    if len(my_str) >= 6 and len(my_str) <= 20:
        if re.search("[a-z]", my_str):
            if re.search("[A-Z]", my_str):
                if re.search("[$, @, &]", my_str):
                    if re.search("[0-9]", my_str):
                        return True
    return False

def getPassWord(my_pw):
    if len(my_pw) >=6 and len(my_pw) <= 20:
        if re.search("[a-z]", my_pw):
            if re.search("[A-Z]", my_pw):
                if re.search("[$, @, &]", my_pw):
                    if re.search("[0-9]", my_pw):
                        return True
    return False

