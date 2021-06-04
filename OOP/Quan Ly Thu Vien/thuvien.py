class Library:

    def __init__(self):
        self.id = 0
        self.author = ""
        self.page_number = 0
        self.release_number = 0
        self.release_month = 0
        self.release_day = 0
        self.__data = []

    def showMenu(self):
        print()
        print("CHƯƠNG TRÌNH THƯ VIỆN".center(50, "-"))
        print("1. Thêm mới sách")
        print("2. Hiển thị thông tin sách")
        print("3. Xoá sách theo ID")
        print("4. Tìm kiếm sách theo ID")
        print("0. Thoát chương trình")
        print("".center(50, "-"))

    def addBook(self):
        n = int(input("Nhập số sách bạn muốn thêm vào: "))
        for i in range(n):
            self.id = len(self.__data) + 1
            self.author = input("Nhập tên tác giả: ")
            self.page_number = int(input("Nhập số trang: "))
            self.release_number = input("Nhập số phát hành: ")
            self.release_day = input("Nhập ngày phát hành (dd/mm/yyyy): ")
            print()
            self.__data.append([self.id, self.author, self.page_number, self.release_number, self.release_day])

    def showBook(self):
        for i in range(len(self.__data)):
            print(f"ID sách: {self.__data[i][0]}")
            print(f"Tên tác giả: {self.__data[i][1]}")
            print(f"Số trang: {self.__data[i][2]}")
            print(f"Số phát hành: {self.__data[i][3]}")
            print(f"Ngày phát hành: {self.__data[i][4]}")
            print()

    def deleteBook(self):
        id = int(input("Nhập ID sách cần xoá: "))
        while id < 1 or id > len(self.__data):
            id = int(input("ID không tồn tại! Nhập lại ID sách cần xoá: "))
        else:
            for i in range(len(self.__data)):
                if id==self.__data[i][0]:
                    self.__data.remove(self.__data[i])
                    print("Sách đã được xoá thành công!\n")
                    break

    def searchBook(self):
        id = int(input("Nhập ID sách cần tìm kiếm: "))
        while id < 1 or id > len(self.__data):
            id = int(input("ID không tồn tại! Nhập lại ID sách cần tìm kiếm: "))
        else:
            for i in range(len(self.__data)):
                if id == self.__data[i][0]:
                    print("Thông tin sách cần tìm".center(30, "+"))
                    print(f"ID sách: {self.__data[i][0]}")
                    print(f"Tên tác giả: {self.__data[i][1]}")
                    print(f"Số trang: {self.__data[i][2]}")
                    print(f"Số phát hành: {self.__data[i][3]}")
                    print(f"Ngày phát hành: {self.__data[i][4]}")
                    print()
                    break





