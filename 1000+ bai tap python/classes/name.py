class Name:

    def __init__(self, fname, lname):
        self.fname = fname.title()
        self.lname = lname.title()
        self.fullname = self.fname + " " + self.lname
        self.initials = self.fname[0] + "." + self.lname[0]

if __name__=="__main__":
    n1 = Name("john", "SMITH")
    print(n1.fname)
    print(n1.lname)
    print(n1.fullname)
    print(n1.initials)
