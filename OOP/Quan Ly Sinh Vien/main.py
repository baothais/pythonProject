import student
# tao doi tuong thuoc lop Student
if __name__=="__main__":
    sv = student.Student()
    sv.showMenu()
    chon = int(input("Moi ban chon cong viec: "))
    while chon!=0:
        if chon==1:
            sv.addStudent()

        if chon==2:
            sv.showStudent()

        if chon==3:
            sv.findStudent()

        if chon==4:
            sv.deleteStudent()

        if chon==5:
            sv.updateStudent()

        chon = int(input("Moi ban chon cong viec: "))
    print("THOAT CHUONG TRINH".center(50, "-"))



