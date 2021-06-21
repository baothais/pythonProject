class Player:

    @staticmethod
    def show_menu():
        print("PROGRAM SPORTS PLAYER".center(50, "="))
        print("1. Get age")
        print("2. Get height")
        print("3. Get weight")
        print("0. Exit")
        print("".center(50, "="))

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is {self.height}cm"

    def get_weight(self):
        return f"{self.name} weighs {self.weight}kg"

if __name__=="__main__":
    player = Player(name="Thai Bao", age=23, height=168, weight=63)
    player.show_menu()
    choose = int(input("Enter your choose: "))
    print()
    while choose != 0:
        if choose == 1:
            print("Get age".center(40, "-"))
            print("Given name = {}, age = {}".format(player.name, player.age))
            print("{}".format(player.get_age()))

        if choose == 2:
            print("Get height".center(40, "-"))
            print("Given name = {}, height = {}".format(player.name, player.height))
            print("{}".format(player.get_height()))

        if choose == 3:
            print("Get weight".center(40, "-"))
            print("Given name = {}, weight = {}".format(player.name, player.weight))
            print("{}".format(player.get_weight()))

        choose = int(input("\nEnter your choose: "))
        print()
    print("EXIT PROGRAM".center(50, "="))