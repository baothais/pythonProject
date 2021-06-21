import practice4

p = practice4.Practice4()

def test_missing_num():
    assert (p.missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) == 5)
    assert (p.missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) == 10)
    assert (p.missing_num([7, 2, 3, 9, 4, 5, 6, 8, 10]) == 1)
    assert (p.missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) == 7)
    assert (p.missing_num([1, 7, 2, 4, 8, 10, 5, 6, 9]) == 3)

def test_is_valid_PIN():
    assert (p.is_valid_PIN("1234") == True)
    assert (p.is_valid_PIN("12345") == False)
    assert (p.is_valid_PIN("a234") == False)
    assert (p.is_valid_PIN("") == False)
    assert (p.is_valid_PIN("%234") == False)
    assert (p.is_valid_PIN("`234") == False)
    assert (p.is_valid_PIN("@234") == False)
    assert (p.is_valid_PIN("#234") == False)
    assert (p.is_valid_PIN("$234") == False)
    assert (p.is_valid_PIN("*234") == False)
    assert (p.is_valid_PIN("5678") == True)
    assert (p.is_valid_PIN("^234") == False)
    assert (p.is_valid_PIN("(234") == False)
    assert (p.is_valid_PIN(")234") == False)
    assert (p.is_valid_PIN("123456") == True)
    assert (p.is_valid_PIN("-234") == False)
    assert (p.is_valid_PIN("_234") == False)
    assert (p.is_valid_PIN("+234") == False)
    assert (p.is_valid_PIN("=234") == False)
    assert (p.is_valid_PIN("?234") == False)

def test_chatroom_status():
    assert (p.chatroom_status([]) == "no one online")
    assert (p.chatroom_status(["becky325"]) == "becky325 online")
    assert (p.chatroom_status(["becky325", "malcolm888"]) == "becky325 and malcolm888 online")
    assert (p.chatroom_status(["becky325", "malcolm888", "fah32fa"]) == "becky325, malcolm888 and 1 more online")
    assert (p.chatroom_status(["paRIE_to"]) == "paRIE_to online")
    assert (p.chatroom_status(["s234f", "mailbox2"]) == "s234f and mailbox2 online")
    assert (p.chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"]) == "pap_ier44, townieBOY and 4 more online")

def test_showdown():
    assert(p.showdown(
        "   Bang!        ",
        "        Bang!   "
    ) == "p1")

    assert(p.showdown(
        "               Bang! ",
        "             Bang!   "
    ) == "p2")

    assert(p.showdown(
        "  Bang!   ",
        "Bang!     "
    ) == "p2")

    assert(p.showdown(
        "     Bang!   ",
        "     Bang!   "
    ) == "tie")

    assert(p.showdown("  Bang!     ", "     Bang!  ") == "p1")
    assert(p.showdown(" Bang!  ", "  Bang! ") == "p1")
    assert(p.showdown("          Bang!       ", "       Bang!          ") == "p2")
    assert(p.showdown("    Bang!    ", "    Bang!    ") == "tie")
    assert(p.showdown("       Bang!       ", "       Bang!       ") == "tie")
    assert(p.showdown(" Bang!      ", "      Bang! ") == "p1")
    assert(p.showdown(" Bang!  ", "  Bang! ") == "p1")
    assert(p.showdown("       Bang!      ", "      Bang!       ") == "p2")

def test_list_operation():
    assert (p.list_operation(1, 10, 3) == [3, 6, 9])
    assert (p.list_operation(7, 9, 2) == [8])
    assert (p.list_operation(15, 20, 7) == [])
    assert (p.list_operation(10, 50, 10) == [10, 20, 30, 40, 50])
    assert (p.list_operation(1, 10, 2) == [2, 4, 6, 8, 10])
    assert (p.list_operation(1, 100, 17) == [17, 34, 51, 68, 85])
    assert (p.list_operation(15, 20, 5) == [15, 20])

def test_simon_says():
    assert (p.simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) == True)
    assert (p.simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) == False)
    assert (p.simon_says([1, 2], [5, 1]) == True)
    assert (p.simon_says([1, 2], [5, 5]) == False)
    assert (p.simon_says([1, 2, 3], [0, 1, 2]) == True)

def test_society_name():
    assert (p.society_name(['Adam', 'Sarah', 'Malcolm']) == 'AMS')
    assert (p.society_name(['Phoebe', 'Chandler', 'Rachel', 'Ross', 'Monica', 'Joey']) == 'CJMPRR')
    assert (p.society_name(['Harry', 'Newt', 'Luna', 'Cho']) == 'CHLN')
    assert (p.society_name(['Sherlock', 'Irene', 'John']) == 'IJS')
    assert (p.society_name(['Sheldon', 'Amy', 'Penny', 'Howard', 'Raj']) == 'AHPRS')

def test_is_isogram():
    assert (p.is_isogram("Algorism") == True)
    assert (p.is_isogram("PasSword") == False)
    assert (p.is_isogram("Dermatoglyphics") == True)
    assert (p.is_isogram("Cat") == True)
    assert (p.is_isogram("Filmography") == True)
    assert (p.is_isogram("Consecutive") == False)
    assert (p.is_isogram("Bankruptcies") == True)
    assert (p.is_isogram("Unforgivable") == True)
    assert (p.is_isogram("Unpredictably") == True)
    assert (p.is_isogram("Moose") == False)