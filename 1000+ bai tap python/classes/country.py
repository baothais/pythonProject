class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = False
        if self.area > 3000000 or self.population > 250000000:
            self.is_big = True

    def compare_pd(self, other):
        if (self.population / self.area) < (other.population / other.area):
            return f"{self.name} has a smaller population density than {other.name}"
        return f"{self.name} has a larger population density than {other.name}"

if __name__=="__main__":
    australia = Country("Australia", 23545500, 7692024)
    andorra = Country("Andorra", 76098, 468)
    print(andorra.is_big)
    print(australia.is_big)
    print(andorra.compare_pd(australia))