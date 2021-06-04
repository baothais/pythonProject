import account

def test_username():
    assert account.getName(my_str="Esd$123d") == True

def test_password():
    assert account.getPassWord(my_pw="aaaaaaaa") == False
