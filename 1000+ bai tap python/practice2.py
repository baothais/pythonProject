import datetime
import math
import random
import re

class Practice2:

    @staticmethod
    def show_menu():
        print("PYTHON PROGRAM".center(50, "="))
        print("1. Vowel Replacer")
        print("2. Xs and Os, Nobody Knows")
        print("3. How Heavy Is It?")
        print("4. Hiding the Card Number")
        print("5. Filter out Strings from an Array")
        print("6. The Reverser!")
        print("7. Is it Time for Milk and Cookies?")
        print("8. Sum of Evenly Divisible Numbers from a Range")
        print("9. Hamming Distance")
        print("10. Count Ones in Binary Representation of Integer")
        print("11. Shuffle the Name")
        print("0. Exit")
        print("".center(50, "="))

    def replace_vowels(self, txt, ch):
        x = ""
        for i in txt:
            if i in ["u", "e", "o", "a", "i"]:
                i = ch
                x += i
            else:
                x += i
        return x

    def XO(self, txt):
        count_x = 0
        count_o = 0
        for i in txt.lower():
            if i == "x":
                count_x += 1
            if i == "o":
                count_o += 1
        return count_x == count_o

    def weight(self, r, h):
        return round((math.pi * (r ** 2) * h) / (10 ** 3), 2)

    def card_hide(self, card):
        return (len(card) - 4) * "*" + card[-4:]

    def filter_list(self, lst):
        new_lst = []
        for i in lst:
            if type(i) == int:
                new_lst.append(i)
        return new_lst

    def reverse(self, txt):
        return txt[::-1].swapcase()

    def time_for_milk_and_cookies(self, date):
        return (date.month == 12 and date.day == 24)

    def evenly_divisible(self, a, b, c):
        return sum([i for i in range(a, b + 1) if i % c == 0])

    def hamming_distance(self, txt1, txt2):
        count = 0
        for i in range(len(txt1)):
            for j in range(i, len(txt2)):
                if txt1[i] != txt2[j]:
                    count += 1
                break
        return count

    def count_ones(self, num):
        lst_binary = []
        while num != 0:
            a = num % 2
            num = num // 2
            lst_binary.append(a)
        return lst_binary.count(1)

    def name_shuffle(self, txt):
        lst_name = txt.split()
        return " ".join(lst_name[::-1])


if __name__=="__main__":
    p = Practice2()
    p.show_menu()
    choose = int(input("Enter your choose: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Vowel Replacer".center(40, "-"))
            txt = input("Enter txt: ")
            ch = input("Enter char: ")
            print("Given txt = \"{}\", char = \"{}\"".format(txt, ch))
            print("Result = {}".format(p.replace_vowels(txt, ch)))

        if choose == 2:
            print("Xs and Os, Nobody Knows".center(40, "-"))
            txt = input("Enter txt: ")
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.XO(txt)))

        if choose == 3:
            print("How Heavy Is It?".center(40, "-"))
            r = int(input("Enter radius: "))
            h = int(input("Enter height: "))
            print("Given radius = {}, height = {}".format(r, h))
            print("Result = {}".format(p.weight(r, h)))

        if choose == 4:
            print("Hiding the Card Number".center(40, "-"))
            card = input("Enter card: ")
            print("Given card = {}".format(card))
            print("Result = {}".format(p.card_hide(card)))

        if choose == 5:
            print("Filter out Strings from an Array".center(40, "-"))
            lst = [1, "a", "b", 0, 15]
            print("Given lst = {}".format(lst))
            print("Result = {}".format(p.filter_list(lst)))

        if choose == 6:
            print("The Reverser!".center(40, "-"))
            txt = input("Enter txt: ")
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.reverse(txt)))

        if choose == 7:
            print("Is it Time for Milk and Cookies?".center(40, "-"))
            date = datetime.date(2013, 12, 24)
            print("Given date = {}".format(date))
            print("Result = {}".format(p.time_for_milk_and_cookies(date)))

        if choose == 8:
            print("Sum of Evenly Divisible Numbers from a Range".center(40, "-"))
            a, b, c = random.sample(range(1, 20), 3)
            print("Given a = {}, b = {}, c = {}".format(a, b, c))
            print("Result = {}".format(p.evenly_divisible(a, b, c)))

        if choose == 9:
            print("Hamming Distance".center(40, "-"))
            txt1 = input("Enter txt1: ")
            txt2 = input("Enter txt2: ")
            print("Given txt1 = {}\nGiven txt2 = {}".format(txt1, txt2))
            print("Result = {}".format(p.hamming_distance(txt1, txt2)))

        if choose == 10:
            print("Count Ones in Binary Representation of Integer".center(40, "-"))
            # num = random.randint(1, 100)
            num = 999
            print("Given num = {}".format(num))
            print("Result = {}".format(p.count_ones(num)))

        if choose == 11:
            print("Shuffle the Name".center(40, "-"))
            txt = input("Enter txt: ")
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.name_shuffle(txt)))

        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT".center(50, "="))