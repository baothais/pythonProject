class Calculator:

    @staticmethod
    def show_menu():
        print("PROGRAM CALCULATOR".center(50, "="))
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("0. Exit")
        print("".center(50, "="))

    def input(self):
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        return a, b

    def add(self, a, b):
        return a + b

    def subtract(self, a , b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

if __name__=="__main__":
    calculator = Calculator()
    calculator.show_menu()
    choose = int(input("Enter your choose: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Add two numbers".center(40, "-"))
            a, b = calculator.input()
            print("Given a = {}, b = {}".format(a, b))
            print("Result = {}".format(calculator.add(a, b)))

        if choose == 2:
            print("Subtract two numbers".center(40, "-"))
            a, b = calculator.input()
            print("Given a = {}, b = {}".format(a, b))
            print("Result = {}".format(calculator.subtract(a, b)))

        if choose == 3:
            print("Multiply two numbers".center(40, "-"))
            a, b = calculator.input()
            print("Given a = {}, b = {}".format(a, b))
            print("Result = {}".format(calculator.multiply(a, b)))

        if choose == 4:
            print("Multiply two numbers".center(40, "-"))
            a, b = calculator.input()
            print("Given a = {}, b = {}".format(a, b))
            print("Result = {}".format(calculator.divide(a, b)))

        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT PROGRAM".center(50, "="))
