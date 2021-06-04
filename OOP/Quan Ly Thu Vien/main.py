import thuvien

if __name__=="__main__":
    tv = thuvien.Library()
    tv.showMenu()
    chon = int(input("Mời bạn chọn công việc: "))
    while chon!=0:
        if chon==1:
            print()
            print("Thêm mới sách".center(40, "*"))
            tv.addBook()

        if chon==2:
            print()
            print("Hiển thị thông tin sách".center(40, "*"))
            tv.showBook()

        if chon==3:
            print()
            print("Xoá sách theo ID".center(40, "*"))
            tv.deleteBook()

        if chon==4:
            print()
            print("Tìm kiếm sách theo ID".center(40, "*"))
            tv.searchBook()

        chon = int(input("Mời bạn chọn công việc: "))

    print("THOÁT CHƯƠNG TRÌNH".center(50, "-"))