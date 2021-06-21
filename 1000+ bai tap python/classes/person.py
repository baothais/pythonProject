class Person:

    def __init__(self, name, list_like, list_hate):
        self.name = name
        self.list_like = list_like
        self.list_hate = list_hate

    def taste(self, food):
        if food in self.list_like:
            return f"{self.name} eats the {food} and loves it!"
        elif food in self.list_hate:
            return f"{self.name} eats the {food} and hates it!"
        return f"{self.name} eats the {food}!"

if __name__=="__main__":
    p1 = Person("Sam", ["ice cream", "pie", "apples"], ["carrots", "bananas", "cheese", "lettuce"])
    print(p1.taste("ice cream"))

