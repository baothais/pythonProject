import random


class Practice5:

    @staticmethod
    def show_menu():
        print("PRACTICE 5".center(50, "="))
        print("1. Is the String in Order?")
        print("2. Convert to Decimal Notation")
        print("3. Purge and Organize")
        print("4. Is the Number Symmetrical?")
        print("5. Square Every Digit")
        print("6. \"EdaBit\" Challenge")
        print("7. Count Palindrome Numbers in a Range")
        print("8. Transform into a List with No Duplicates")
        print("9. Get Student Names")
        print("10. Say Hello to Guests")
        print("0. Exit")
        print("".center(50, "="))

    def is_in_order(self, txt):
        for i in range(len(txt) - 1):
            if txt[i] > txt[i + 1]:
                return False
        return True

    def convert_to_decimal(self, perc):
        return [float(perc[i][:-1]) / 100 for i in range(len(perc))]

    def unique_sort(self, lst):
        new_lst = list(dict.fromkeys(lst))
        new_lst.sort()
        return new_lst

    def is_symmetrical(self, num):
        return str(num) == str(num)[::-1]

    def square_digits(self, n):
        return int("".join([str(int(i) ** 2) for i in str(n)]))

    def eda_bit(self, start, end):
        lst_bit = []
        for i in range(start, end + 1):
            if i % 3 == 0:
                if i % 5 == 0:
                    lst_bit.append("EdaBit")
                else:
                    lst_bit.append("Eda")
            elif i % 5 == 0:
                lst_bit.append("Bit")
            else:
                lst_bit.append(i)
        return lst_bit

    def count_palindromes(self, num1, num2):
        count = 0
        for i in range(num1, num2 + 1):
            if i < 10:
                count += 1
            else:
                if str(i) == str(i)[::-1]:
                    count += 1
        return count

    def setify(self, lst):
        return list(dict.fromkeys(lst))

    def get_student_names(self, students):
        lst_students = [students[key] for key in students.keys()]
        lst_students.sort()
        return lst_students

    def greet_people(self, names):
        if names == []:
            return ""
        lst_names = ["Hello " + i for i in names]
        return ", ".join(lst_names)


if __name__=="__main__":
    p = Practice5()
    p.show_menu()
    choose = int(input("Enter your choose: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Is the String in Order?".center(40, "-"))
            txt = "123"
            print("Given txt = {}".format(txt))
            print("Result = {}".format(p.is_in_order(txt)))

        if choose == 2:
            print("Convert to Decimal Notation".center(40, "-"))
            perc = ["33%", "98.1%", "56.44%", "100%"]
            print("Given perc = {}".format(perc))
            print("Result = {}".format(p.convert_to_decimal(perc)))

        if choose == 3:
            print("Purge and Organize".center(40, "-"))
            lst = [1, 4, 4, 4, 4, 4, 3, 2, 1, 2]
            print("Given list = {}".format(lst))
            print("Result = {}".format(p.unique_sort(lst)))

        if choose == 4:
            print("Is the Number Symmetrical?".center(40, "-"))
            num = random.randint(1, 10000)
            print("Given num = {}".format(num))
            print("Result = {}".format(p.is_symmetrical(num)))

        if choose == 5:
            print("Square Every Digit".center(40, "-"))
            n = random.randint(1, 10000)
            print("Given num = {}".format(n))
            print("Result = {}".format(p.square_digits(n)))

        if choose == 6:
            print('"EdaBit" Challenge'.center(40, "-"))
            start, end = [random.randint(1, 4), random.randint(5, 10)]
            print("Given start = {}, end = {}".format(start, end))
            print("Result = {}".format(p.eda_bit(start, end)))

        if choose == 7:
            print("Count Palindrome Numbers in a Range".center(40, "-"))
            num1, num2 = [1, 10]
            print("Given num1 = {}, num2 = {}".format(num1, num2))
            print("Result = {}".format(p.count_palindromes(num1, num2)))

        if choose == 8:
            print("Transform into a List with No Duplicates".center(40, "-"))
            lst = [1, 3, 3, 5, 5, 5]
            print("Given list = {}".format(lst))
            print("Result = {}".format(p.setify(lst)))

        if choose == 9:
            print("Get Student Names")
            students = {
                "Student 1": "Steve",
                "Student 2": "Becky",
                "Student 3": "John"
            }
            print("Given students = {}".format(students))
            print("Result = {}".format(p.get_student_names(students)))

        if choose == 10:
            print("Say Hello to Guests".center(40, "-"))
            names = ["Frank", "Angela", "Joe"]
            print("Given names = {}".format(names))
            print("Result = {}".format(p.greet_people(names)))

        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT".center(50, "="))
