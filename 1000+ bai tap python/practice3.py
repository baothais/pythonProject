import random
import re


class Practice3:

    @staticmethod
    def show_menu():
        print("PYTHONG PROGRAM".center(50, "="))
        print("1. Characters in Shapes")
        print("2. Moving to the End")
        print("3. Repeating Letters")
        print("4. Flip the Boolean")
        print("5. Folding a Piece of Paper")
        print("6. Return the Index of All Capital Letters")
        print("7. Filter Strings from Array")
        print("8. Add the Index")
        print("9. Probabilities")
        print("10. Triangular Number Sequence")
        print("0. Exit")
        print("".center(50, "="))

    def count_characters(self, lst):
        s = 0
        for i in range(len(lst)):
            s += len(lst[i])
        return s

    def move_to_end(self, lst, el):
        for i in lst:
            if el == i:
                lst.remove(i)
                lst.append(i)
        return lst

    def double_char(self, txt):
        s = ""
        for i in txt:
            s += i * 2
        return s

    def reverse(self, arg):
        return not arg

    def num_layers(self, n):
        return f"{2 ** n * 0.0005}m"

    def index_of_caps(self, word):
        lst_index = []
        for i in range(len(word)):
            if word[i].isupper():
                lst_index.append(i)
        return lst_index

    def filter_list(self, lst):
        lst_num = []
        for i in lst:
            if type(i) == int:
                lst_num.append(i)
        lst_num.sort()
        return lst_num

    def add_indexes(self, lst):
        return [(i + lst[i]) for i in range(len(lst))]

    def probability(self, lst, n):
        lst_bigger = [i for i in lst if i >= n]
        return round((len(lst_bigger) / len(lst)) * 100, 1)

    def triangle(self, n):
        i = 1
        j = 1
        s = 0
        while i <= n:
            s += j
            i += 1
            j += 1
        return s

if __name__=="__main__":
    p = Practice3()
    p.show_menu()
    choose = int(input("Enter your choose: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Characters in Shapes".center(40, "-"))
            lst = ['22222222', '22222222']
            print("lst = {}".format(lst))
            print("Result = {}".format(p.count_characters(lst)))

        if choose == 2:
            print("Moving to the End".center(40, "-"))
            lst = [1, 3, 2, 4, 4, 1]
            el = 1
            print("Given lst = {}, el = {}".format(lst, el))
            print("Result = {}".format(p.move_to_end(lst, el)))

        if choose == 3:
            print("Repeating Letters".center(40, "-"))
            txt = "Hello World!"
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.double_char(txt)))

        if choose == 4:
            print("Flip the Boolean".center(40, "-"))
            arg = {}
            print("Given arg = {}".format(arg))
            print("Result = {}".format(p.reverse(arg)))

        if choose == 5:
            print("Folding a Piece of Paper".center(40, "-"))
            n = random.randint(0, 21)
            print("Given n = {}".format(n))
            print("Result = {}".format(p.num_layers(n)))

        if choose == 6:
            print("Return the Index of All Capital Letters".center(40, "-"))
            word = "eDaBiT"
            print("Given word = {}".format(word))
            print("Result = {}".format(p.index_of_caps(word)))

        if choose == 7:
            print("Filter Strings from Array".center(40, "-"))
            lst = [1, 2, 3, "a", "b", 4]
            print("Given lst = {}".format(lst))
            print("Result = {}".format(p.filter_list(lst)))

        if choose == 8:
            print("Add the Index".center(40, "-"))
            lst = [1, 2, 3, 4, 5]
            print("Given lst = {}".format(lst))
            print("Result = {}".format(p.add_indexes(lst)))

        if choose == 9:
            print("Probabilities".center(40, "-"))
            lst, n = [[7, 4, 17, 14, 12, 3], 16]
            print("Given lst = {}, num = {}".format(lst, n))
            print("Result = {}".format(p.probability(lst, n)))

        if choose == 10:
            print("Triangular Number Sequenc".center(40, "-"))
            n = random.randint(1, 100)
            print("Given num = {}".format(n))
            print("Result = {}".format(p.triangle(n)))

        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT PROGRAM".center(50, "="))

