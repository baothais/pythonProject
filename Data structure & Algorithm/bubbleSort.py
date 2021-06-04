import random

class BubbleSort():

    def showMenu(self):
        print("PRACTICE BUBBLE SORT".center(50, "="))
        print("1. Bubble sort 1")
        print("0. Exit")
        print("".center(50, "="))

    def bubbleSort1(self, my_list):
        for i in range(len(my_list)):
            for j in range(len(my_list)-i-1):
                if my_list[j] > my_list[j+1]:
                    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

        return my_list

if __name__=="__main__":
    b = BubbleSort()
    b.showMenu()
    choose = int(input("Enter your choose: "))
    print()
    while choose!=0:
        if choose==1:
            print("Bubble sort 1".center(40, "-"))
            my_list = random.sample(range(1, 100), 5)
            print(b.bubbleSort1(my_list))

        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT PROGRAM".center(50, "="))
