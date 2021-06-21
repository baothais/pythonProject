import re

class Practice4:

    @staticmethod
    def show_menu():
        print("PYTHON PROGRAM".center(50, "="))
        print("1. Find the Missing Number")
        print("2. Card Counting (BlackJack)")
        print("3. ATM PIN Code Validation")
        print("4. Compound Interest")
        print("5. Chat Room Status")
        print("6. Western Showdown")
        print("7. List Operation")
        print("8. Simon Says")
        print("9. Secret Society")
        print("10. Is the Word an Isogram?")
        print("0. Exit")
        print("".center(50, "="))

    def missing_num(self, lst):
        j = 1
        while True:
            if j not in lst:
                return j
            if j == 10:
                return False
            j += 1

    def count(self, deck):
        s = 0
        for i in deck:
            if i in [2, 3, 4, 5, 6]:
                s += 1
            elif i in [7, 8, 9]:
                s += 0
            else:
                s += -1
        return s

    def is_valid_PIN(self, pin):
        lst_pin = re.findall("\d", pin)
        if len(lst_pin) == 4 or len(lst_pin) == 6:
            return True
        return False

    def compound_interest(self, p, t, r, n):
        return round((p * (1 + (r / n)) ** (n * t)), 2)

    def chatroom_status(self, users):
        if len(users) == 0:
            return "no one online"
        elif len(users) == 1:
            return f"{users[0]} online"
        elif len(users) == 2:
            return f"{users[0]} and {users[1]} online"
        return f"{users[0]}, {users[1]} and {len(users) - 2} more online"

    def showdown(self, p1, p2):

        """way 1"""
        """count_p1 = 0
        count_p2 = 0
        for i in p1:
            if i.isspace():
                count_p1 += 1
            else:
                break
        for i in p2:
            if i.isspace():
                count_p2 += 1
            else:
                break
        if count_p1 < count_p2:
            return "p1"
        elif count_p1 > count_p2:
            return "p2"
        return "tie"""

        """way 2"""
        index_p1 = p1.find("Bang!")
        index_p2 = p2.find("Bang!")
        if index_p1 < index_p2:
            return "p1"
        elif index_p1 > index_p2:
            return "p2"
        return "tie"

    def list_operation(self, x, y, n):
        return [i for i in range(x, y + 1) if i % n == 0]

    def simon_says(self, lst1, lst2):

        """way 1"""
        """if len(lst1) == len(lst2):
            for i in range(len(lst1) - 1):
                for j in range(i + 1, len(lst2)):
                    if lst1[i] != lst2[j]:
                        return False
                    else:
                        break
        return True"""

        """way 2"""
        return lst1[:-1] == lst2[1:]

    def society_name(self, friends):
        lst_friends = [friends[i][0] for i in range(len(friends))]
        lst_friends.sort()
        return "".join(lst_friends)

    def is_isogram(self, txt):
        copy_txt = txt.lower()
        for i in range(len(copy_txt) - 1):
            for j in range(i+1, len(copy_txt)):
                if copy_txt[i] == copy_txt[j]:
                    return False
        return True


if __name__=="__main__":
    p = Practice4()
    p.show_menu()
    choose = int(input("Enter your choose: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Find the Missing Number".center(40, "-"))
            lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            print("Given list = {}".format(lst))
            print("Result = {}".format(p.missing_num(lst)))

        if choose == 2:
            print("Card Counting (BlackJack)".center(40, "-"))
            deck = [5, 9, 10, 3, "J", "A", 4, 8, 5]
            print("Given list = {}".format(deck))
            print("Result = {}".format(p.count(deck)))

        if choose == 3:
            print("ATM PIN Code Validation".center(40, "-"))
            pin = "12345"
            print("Given pin = {}".format(pin))
            print("Result = {}".format(p.is_valid_PIN(pin)))

        if choose == 4:
            print("Compound Interest".center(40, "-"))
            p1, t, r, n = [100000, 20, 0.15, 365]
            print("Given p = {}, t = {}, r = {}, n = {}".format(p1, t, r, n))
            print("Result = {}".format(p.compound_interest(p1, t, r, n)))

        if choose == 5:
            print("Chat Room Status".center(40, "-"))
            users = ["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"]
            print("Given list = {}".format(users))
            print("Result = {}".format(p.chatroom_status(users)))

        if choose == 6:
            print("Western Showdown".center(40, "-"))
            p1 = "   Bang!        "
            p2 = "        Bang!   "
            print("Given p1 = {}, p2 = {}".format(p1, p2))
            print("Result = {}".format(p.showdown(p1, p2)))

        if choose == 7:
            print("List Operation".center(40, "-"))
            x, y, n = [1, 10, 3]
            print("Given x = {}, y = {}, n = {}".format(x, y, n))
            print("Result = {}".format(p.list_operation(x, y, n)))

        if choose == 8:
            print("Simon Says".center(40, "-"))
            lst1 = [1, 2, 3, 4, 5]
            lst2 = [0, 1, 2, 3, 4]
            print("Given list1 = {}, list2 = {}".format(lst1, lst2))
            print("Result = {}".format(p.simon_says(lst1, lst2)))

        if choose == 9:
            print("Secret Society".center(40, "-"))
            friends = ["Adam", "Sarah", "Malcolm"]
            print("Given friends = {}".format(friends))
            print("Result = {}".format(p.society_name(friends)))

        if choose == 10:
            print("Is the Word an Isogram?".center(40, "-"))
            txt = "Algorism"
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.is_isogram(txt)))

        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT PROGRAM".center(50, "="))