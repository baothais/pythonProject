# class User:
#     user_count = 0
#     def __init__(self, username):
#         self.username = username
#         User.user_count += 1
#
# if __name__=="__main__":
#     u1 = User("johnsmith10")
#     u2 = User("marysue1989")
#     print(User.user_count)
# class Dog:
#
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []    # creates a new empty list for each dog
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)

class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self):
        self.tricks.append(self.name)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick()
e.add_trick()
print(d.tricks)
print(e.tricks)

