class Composer:

    count = 0

    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        # Composer.count += 1
    def composer_count(self):
        Composer.count = 1

if __name__=="__main__":
    c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
    c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
    c3 = Composer("Johannes Brahms", 1833, "Germany")
    c1.composer_count()
    print(c1.count)

