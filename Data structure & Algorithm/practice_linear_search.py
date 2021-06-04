import random


class LinearSearch:

    def __init__(self):
        self.__numbers = []

    @staticmethod
    def show_menu():
        print("PRACTICE LINEAR SEARCH".center(50, "="))
        print("1. Add Array")
        print("2. Print Array")
        print("3. Count Occurrences")
        print("4. Search max of even array")
        print("5. Search min of odd array")
        print("".center(50, "="))

    def add_array(self):
        self.__numbers = random.sample(range(1, 10), 5)
        # for i in range(random.randint(5, 10)):
        #     self.__numbers.append(int(input("numbers[{}] = ".format(i))))

    def print_array(self):
        return self.__numbers

    def count_occurrences(self, target):
        count = 0
        for i in range(len(self.__numbers)):
            if target == self.__numbers[i]:
                count += 1
        if count > 0:
            return "target in array\ntarget appears {} times".format(count)
        return "target not in array"

    def search_max_even(self):
        max = 0
        for i in range(len(self.__numbers)):
            if self.__numbers[max] < self.__numbers[i] and self.__numbers[i] % 2 ==0:
                max = i
        if self.__numbers[max] % 2 == 0:
            return "max of even numbers is {}".format(self.__numbers[max])
        return "no even number in array"

    def search_min_odd(self):
        min = self.__numbers[0]
        for i in range(len(self.__numbers)):
            if min > self.__numbers[i] and self.__numbers[i] % 2 != 0:
                min = self.__numbers[i]
        if min % 2 != 0:
            return "min of odd numbers is {}".format(min)
        return "not odd number in array"

if __name__=="__main__":
    l = LinearSearch()
    l.show_menu()
    choose = int(input("Enter your choose: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Add Array".center(40, "-"))
            l.add_array()

        if choose == 2:
            print("Print Array".center(40, "-"))
            print("==> array = {}".format(l.print_array()))

        if choose == 3:
            print("Count Occurrences".center(40, "-"))
            print(l.count_occurrences(target=int(input("Enter target: "))))

        if choose == 4:
            print("Search max of even array".center(40, "-"))
            print(l.search_max_even())

        if choose == 5:
            print("Search min of odd array".center(40, "-"))
            print(l.search_min_odd())

        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT PRACTICE".center(50, "="))

