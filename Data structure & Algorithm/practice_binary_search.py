import random


class Practice_Binary_Search:

    def __init__(self):
        self.__numbers = []

    @staticmethod
    def show_menu():
        print("PRACTICE BINARY SEARCH".center(50, "="))
        print("1. Add Descending Array")
        print("2. Print Array")
        print("3. Binary Search")
        # print("4. Search Max Of Prime In Array")
        # print("5. Search Min Of Prime In Array")
        print("".center(50, "="))

    def add_descending_array(self):
        # self.__numbers = random.sample(range(1, 10000), 8)
        for i in range(random.randint(5, 5)):
            self.__numbers.append(int(input("numbers[{}] = ".format(i))))
        self.__numbers.sort(reverse=True)

    def print_array(self):
        return "array = {}".format(self.__numbers)

    def is_prime(self, prime):
        if prime < 2:
            return False
        return all(prime % i != 0 for i in range(2, int(pow(prime, 0.5)) + 1))

    def binary_search(self, target):
        left = 0
        right = len(self.__numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == self.__numbers[mid]:
                return "target in array"
            elif target > self.__numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return "target not in array"

    # def search_max_prime(self):
    #     max = -1
    #     left = 0
    #     right = len(self.__numbers) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if max < self.__numbers[mid] and self.is_prime(self.__numbers[mid]):
    #             max = self.__numbers[mid]
    #         elif max > self.__numbers[mid]:
    #             right = mid - 1
    #         elif max < self.__numbers[mid]:
    #             left = mid + 1
    #     if self.is_prime(max):
    #         return max
    #     return "not have prime in array"

if __name__=="__main__":
    b = Practice_Binary_Search()
    b.show_menu()
    choose = int(input("Enter your choose: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Add Descending Array".center(40, "-"))
            b.add_descending_array()
        if choose == 2:
            print("Print Array".center(40, "-"))
            print(b.print_array())
        if choose == 3:
            print("Binary Search".center(40, "-"))
            print(b.binary_search(target=int(input("Enter target: "))))

        # if choose == 4:
        #     print("Search Max Of Prime In Array".center(40, "-"))
        #     print(b.search_max_prime())

        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT PRACTICE".center(50, "="))
