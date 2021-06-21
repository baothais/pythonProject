import math


class Practice8:

    @staticmethod
    def show_menu():
        print("PYTHON PROGRAMING".center(50, "="))
        print("1. Tính S(n) = 1 + 2 + 3 + … + n")
        print("2. Tính S(n) = 1^2 + 2^2 + … + n^2")
        print("3. Tính S(n) = 1 + ½ + 1/3 + … + 1/n")
        print("4. Tính S(n) = ½ + ¼ + … + 1/2n")
        print("5. Liệt kê tất cả các “ước số” của số nguyên dương n")
        print("6. Tính tổng tất cả các “ ước số” của số nguyên dương n")
        print("7. Tính tích tất cả các “ước số” của số nguyên dương n")
        print("8. Đếm số lượng “ước số” của số nguyên dương n")
        print("9. Liệt kê tất cả các “ước số lẻ” của số nguyên dương n")
        print("10. Tính tổng tất cả các “ước số chẵn” của số nguyên dương n")
        print("11. Tính tích tất cả các “ước số lẻ” của số nguyên dương n")
        print("12. Đếm số lượng “ước số chẵn” của số nguyên dương n")
        print("13. Tìm ước số lẻ lớn nhất của số nguyên dương n. Ví dụ n = 100 ước lẻ lớn nhất là 25")
        print("14. Kiểm tra xem n có phải là số hoàn thiện hay không")
        print("15. Kiểm tra xem n có phải là số chính phương hay không")
        print("16. Kiểm tra xem n có phải là số nguyên tố hay không")
        print("17. Tính S(n) = CanBac2(2+CanBac2(2+….+CanBac2(2 + CanBac2(2)))) có n dấu căn")
        print("18. Tính S(n) = CanBac2(n+CanBac2(n – 1 + CanBac2( n – 2 + … + CanBac2(2 + CanBac2(1)  có n dấu căn")
        print("19. Tính S(n) = CanBac2(n! + CanBac2((n-1)! +CanBac2((n – 2)! + … + CanBac2(2!) + CanBac2(1!)))) có n dấu căn")
        print("0. Exit")
        print("".center(50, "="))

    def input_number(self):
        number = int(input("Enter number: "))
        return number

    def exercise1(self, number):
        if number <= 0:
            return 0
        return number + self.exercise1(number - 1)

    def exercise2(self, number):
        if number <=0:
            return 0
        return number**2 + self.exercise2(number - 1)

    def exercise3(self, number):
        if number <= 0:
            return 0
        return 1 / number + self.exercise3(number - 1)

    def exercise4(self, number):
        if number <= 0:
            return 0
        return 1 / (2 * number) + self.exercise4(number - 1)

    def get_divisor(self, number):
        return [i for i in range(1, number + 1) if number % i == 0]

    def exercise5(self, number):
        return " ".join(list(map(str, self.get_divisor(number))))

    def exercise6(self, number):
        return sum(self.get_divisor(number))

    def exercise7(self, number):
        multiple = 1
        for i in self.get_divisor(number):
            multiple *= i
        return multiple

    def exercise8(self, number):
        count = 0
        for _ in self.get_divisor(number):
            count += 1
        return count

    def exercise9(self, number):
        return " ".join([str(i) for i in self.get_divisor(number) if i % 2 != 0])

    def exercise10(self, number):
        return sum([i for i in self.get_divisor(number) if i % 2 == 0])

    def exercise11(self, number):
        multiple = 1
        for i in self.get_divisor(number):
            if i % 2 != 0:
                multiple *= i
        return multiple

    def exercise12(self, number):
        count = 0
        for i in self.get_divisor(number):
            if i % 2 == 0:
                count += 1
        return count

    def exercise13(self, number):
        max = 1
        for i in self.get_divisor(number):
            if i % 2 != 0:
                if max < i:
                    max = i
        return max

    def exercise14(self, number):
        sum = 0
        for i in range(1, number):
            if number % i == 0:
                sum += i
        return sum == number

    def exercise15(self, number):
        return int(math.sqrt(number))**2 == number

    def check_prime(self, number):
        if number < 2:
            return False
        return all(number % i != 0 for i in range(2, int(math.sqrt(number)) + 1))

    def exercise16(self, number):
        return self.check_prime(number)

    def exercise17(self, number):
        # if number == 1:
        #     return math.sqrt(2)
        # return math.sqrt(2+self.exercise17(number - 1))
        s = 0
        for _ in range(number):
            s = math.sqrt(2 + s)
        return s

    def exercise18(self, number):
        if number == 1:
            return 1
        return math.sqrt(number + self.exercise18(number - 1))

    def factorial(self, number):
        # if number == 0 or number == 1:
        #     return 1
        # return number * self.factorial(number - 1)
        f = 1
        for i in range(1, number + 1):
            f *= i
        return f

    def exercise19(self, number):
        if number == 1 or number == 0:
            return 1
        return math.sqrt(self.factorial(number) + self.exercise19(self.factorial(number - 1)))

if __name__=="__main__":
    p = Practice8()
    p.show_menu()
    choose = int(input("Enter your choose: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Exercise 1".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Sum = {}".format(p.exercise1(number)))

        if choose == 2:
            print("Exercise 2".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Sum = {}".format(p.exercise2(number)))

        if choose == 3:
            print("Exercise 3".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Sum = {}".format(p.exercise3(number)))

        if choose == 4:
            print("Exercise 4".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Sum = {}".format(p.exercise4(number)))

        if choose == 5:
            print("Exercise 5".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise5(number)))

        if choose == 6:
            print("Exercise 6".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise6(number)))

        if choose == 7:
            print("Exercise 7".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise7(number)))

        if choose == 8:
            print("Exercise 8".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise8(number)))

        if choose == 9:
            print("Exercise 9".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise9(number)))

        if choose == 10:
            print("Exercise 10".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise10(number)))

        if choose == 11:
            print("Exercise 11".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise11(number)))

        if choose == 12:
            print("Exercise 12".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise12(number)))

        if choose == 13:
            print("Exercise 13".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise13(number)))

        if choose == 14:
            print("Exercise 14".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise14(number)))

        if choose == 15:
            print("Exercise 15".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise15(number)))

        if choose == 16:
            print("Exericise 16".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Resutl = {}".format(p.exercise16(number)))

        if choose == 17:
            print("Exercise 17".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise17(number)))

        if choose == 18:
            print("Exercise 18".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise18(number)))

        if choose == 19:
            print("Exercise 19".center(40, "-"))
            number = p.input_number()
            print("Given number = {}".format(number))
            print("Result = {}".format(p.exercise19(number)))


        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT PROOGRAM".center(50, "="))


