class Employee:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + " " + lastname
        self.email = firstname.lower() + "." + lastname.lower() + "@company.com"

if __name__=="__main__":
    employee1 = Employee("John", "Smith")
    employee2 = Employee("Mary",  "Sue")
    employee3 = Employee("Antony", "Walker")
    print(employee2.fullname)
    print(employee2.email)

