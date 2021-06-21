class IceCream:

    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles
        if self.flavor == "Chocolate":
            self.num_sprinkles += 10
        if self.flavor == "Vanilla":
            self.num_sprinkles += 5
        if self.flavor == "Strawberry":
            self.num_sprinkles += 10
        if self.flavor == "Plain":
            self.num_sprinkles += 0
        if self.flavor == "ChocolateChip":
            self.num_sprinkles += 5

def sweetest_icecream(lst_ice):
    new_lst_ice = [i.num_sprinkles for i in lst_ice]
    return max(new_lst_ice)

if __name__=="__main__":
    ice1 = IceCream("Chocolate", 13)  # value of 23
    ice2 = IceCream("Vanilla", 0)  # value of 5
    ice3 = IceCream("Strawberry", 7)  # value of 17
    ice4 = IceCream("Plain", 18)  # value of 18
    ice5 = IceCream("ChocolateChip", 3)  # value of 8
    print(sweetest_icecream([ice3, ice1]))
