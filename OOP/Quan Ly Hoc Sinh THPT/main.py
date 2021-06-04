import student

if __name__=="__main__":
    s = student.Student()
    s.showMenu()
    chon = int(input("Moi ban chon cong viec: "))
    while chon != 0:

        # Them hoc sinh
        if chon==1:
            s.addStudent()

        # In danh sach hoc sinh
        if chon==2:
            s.printStudent()

        chon = int(input("Moi ban chon cong viec: "))
    print("THOAT CHUONG TRINH".center(50, "="))