class Student:

    def __init__(self):
        self.id = 1
        self.name = ""
        self.age = 1
        self.gender = ""
        self.address = ""
        self.mark = 0
        self.__data = []

    def showMenu(self):
        print("QUAN LY SINH VIEN".center(50, "-"))
        print("1. Them moi sinh vien")
        print("2. Xuat thong tin sinh vien")
        print("3. Tim thong tin sinh vien")
        print("4. Xoa thong tin sinh vien")
        print("5. Update thong tin sinh vien")
        print("0. Thoat chuong trinh")
        print("".center(50, "-"))

    def addStudent(self):
        n = int(input("Nhap so sinh vien can them: "))
        for i in range(n):
            self.id = len(self.__data)+1
            self.name = input("Nhap ten sinh vien : ")
            self.age = int(input("Nhap tuoi sinh vien: "))
            self.gender = input("Nhap gioi tinh sinh vien (Name/Nu/Khac): ")
            self.address = input("Nhap dia chi sinh vien: ")
            self.mark = float(input("Nhap diem sinh vien: "))
            self.__data.append([self.id, self.name, self.age, self.gender, self.address, self.mark])
            print()

    def showStudent(self):
        for i in range(len(self.__data)):
            print(f"ID sinh vien: {self.__data[i][0]}")
            print(f"Ten sinh vien: {self.__data[i][1]}")
            print(f"Tuoi sinh: {self.__data[i][2]}")
            print(f"Gioi tinh sinh vien: {self.__data[i][3]}")
            print(f"Dia chi sinh vien: {self.__data[i][4]}")
            print(f"Diem sinh vien: {self.__data[i][5]}")
            print()

    def findStudent(self):
        id = int(input("Nhap ID sinh vien can tim: "))
        while id > len(self.__data) or id < 1:
            print("K hong ton tai ID nay!")
            id = int(input("Nhap lai ID sinh vien can tim: "))
        else:
            for i in range(len(self.__data)):
                if id == self.__data[i][0]:
                    print(f"ID sinh vien: {self.__data[i][0]}")
                    print(f"Ten sinh vien: {self.__data[i][1]}")
                    print(f"Tuoi sinh: {self.__data[i][2]}")
                    print(f"Gioi tinh sinh vien: {self.__data[i][3]}")
                    print(f"Dia chi sinh vien: {self.__data[i][4]}")
                    print(f"Diem sinh vien: {self.__data[i][5]}")
                    print()
                    break

    def deleteStudent(self):
        id = int(input("Nhap ID sinh vien muon xoa: "))
        while id > len(self.__data) or id < 1:
            print("Khong ton tai ID nay!")
            id = int(input("Nhap lai ID sinh vien muon xoa: "))
        else:
            for i in range(len(self.__data)):
                if id == self.__data[i][0]:
                    self.__data.remove(self.__data[i])
                    print("Sinh vien da duoc xoa!\n")
                    break

    def updateStudent(self):
        id = int(input("Nhap ID sinh vien muon update: "))
        while id > len(self.__data) or id < 1:
            print("Khong ton tai ID nay!")
            id = int(input("Nhap lai ID sinh vien muon update: "))
        else:
            for i in range(len(self.__data)):
                if id == self.__data[i][0]:
                    self.__data.remove(self.__data[i])
                    self.id = id
                    self.name = input("Nhap ten sinh vien : ")
                    self.age = int(input("Nhap tuoi sinh vien: "))
                    self.gender = input("Nhap gioi tinh sinh vien (Name/Nu/Khac): ")
                    self.address = input("Nhap dia chi sinh vien: ")
                    self.mark = float(input("Nhap diem sinh vien: "))
                    self.__data.insert(id-1, [self.id, self.name, self.age, self.gender, self.address, self.mark])
                    print("Sinh vien da duoc update!\n")
                    break


