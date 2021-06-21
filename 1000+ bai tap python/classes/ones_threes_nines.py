class Ones_Threes_Nines:

    def __init__(self, num):
        self.ones = num
        self.threes = num // 3
        self.nines = num // 9

if __name__=="__main__":
    n1 = Ones_Threes_Nines(5)
    print(n1.nines)
