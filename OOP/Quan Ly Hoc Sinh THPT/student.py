class Student:

    def __init__(self):
        self.id = 0
        self.fullname = ""
        self.age = 0
        self.clas_name = ""
        self.village = ""
        self.__data = []

    def showMenu(self):
        print("CHUONG TRINH QUAN LY THONG TIN HOC SINH".center(50, "="))
        print("1. Them hoc sinh")
        print("2. In danh sach hoc sinh")
        print("0. Thoat chuong trinh")
        print("".center(50, "="))

    def addStudent(self):
        n = int(input("Nhap so hoc sinh ban muon them vao: "))
        for i in range(n):
            self.id = len(self.__data) + 1
            self.fullname = input("Nhap ho ten hoc sinh: ")
            self.age = int(input("Nhap tuoi hoc sinh: "))
            self.clas_name = input("Nhap ten lop cua hoc sinh: ")
            self.village = input("Nhap que huong cua hoc sinh: ")
            self.__data.append([self.id, self.fullname, self.age, self.clas_name, self.village])
            print()

    def printStudent(self):
        print("Thong tin hoc sinh".center(40, "+"))
        print()
        for i in range(len(self.__data)):
            print(f"Thong tin hoc sinh thu {self.__data[i][0]}".center(30, "+"))
            print(f"ID hoc sinh: {self.__data[i][0]}")
            print(f"Ho ten hoc sinh: {self.__data[i][1]}")
            print(f"Tuoi hoc sinh: {self.__data[i][2]}")
            print(f"Lop cua hoc sinh: {self.__data[i][3]}")
            print(f"Que huong cua hoc sinh: {self.__data[i][4]}")
            print()





