from practice5 import Practice5

p = Practice5()

def test_is_in_order():
    assert (p.is_in_order("abc") == True)
    assert (p.is_in_order("edabit") == False)
    assert (p.is_in_order("xyz") == True)
    assert (p.is_in_order("xyzz") == True)
    assert (p.is_in_order("123") == True)
    assert (p.is_in_order("321") == False)

def test_convert_to_decimal():
    assert (p.convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]) == [0.33, 0.981, 0.5644, 1])
    assert (p.convert_to_decimal(["45%", "32%", "97%", "33%"]) == [0.45, 0.32, 0.97, 0.33])
    assert (p.convert_to_decimal(["1%", "2%", "3%"]) == [0.01, 0.02, 0.03])

def test_unique_sort():
    assert (p.unique_sort([1, 5, 8, 2, 3, 4, 4, 4, 10]) == [1, 2, 3, 4, 5, 8, 10])
    assert (p.unique_sort([1, 2, 5, 4, 7, 7, 7]) == [1, 2, 4, 5, 7])
    assert (p.unique_sort([7, 6, 5, 4, 3, 2, 1, 0, 1]) == [0, 1, 2, 3, 4, 5, 6, 7])
    assert (p.unique_sort([3, 6, 5, 4, 3, 27, 1, 100, 1]) == [1, 3, 4, 5, 6, 27, 100])
    assert (p.unique_sort([-9, -3.1414, -87, 8, -4.323827, -3.1415, -3.1415]) == [-87, -9, -4.323827, -3.1415, -3.1414, 8])

def test_is_symmetrical():
    assert (p.is_symmetrical(23) == False)
    assert (p.is_symmetrical(9562) == False)
    assert (p.is_symmetrical(10019) == False)
    assert (p.is_symmetrical(1) == True)
    assert (p.is_symmetrical(3223) == True)
    assert (p.is_symmetrical(95559) == True)
    assert (p.is_symmetrical(66566) == True)

def test_square_digits():
    assert (p.square_digits(9119) == 811181)
    assert (p.square_digits(8726) == 6449436)
    assert (p.square_digits(9763) == 8149369)
    assert (p.square_digits(2230) == 4490)
    assert (p.square_digits(2797) == 4498149)
    assert (p.square_digits(233) == 499)
    assert (p.square_digits(7437) == 4916949)
    assert (p.square_digits(2483) == 416649)
    assert (p.square_digits(5742) == 2549164)
    assert (p.square_digits(5636) == 2536936)
    assert (p.square_digits(841) == 64161)

def test_eda_bit():
    assert (p.eda_bit(1, 20) == [1, 2, 'Eda', 4, 'Bit', 'Eda', 7, 8, 'Eda', 'Bit', 11, 'Eda', 13, 14, 'EdaBit', 16, 17, 'Eda', 19, 'Bit'])
    assert (p.eda_bit(-250, -230) == ['Bit', 'Eda', -248, -247, 'Eda', 'Bit', -244, 'Eda', -242, -241, 'EdaBit', -239, -238, 'Eda', -236, 'Bit', 'Eda', -233, -232, 'Eda', 'Bit'])
    assert (p.eda_bit(-10, 5) == ['Bit', 'Eda', -8, -7, 'Eda', 'Bit', -4, 'Eda', -2, -1, 'EdaBit', 1, 2, 'Eda', 4, 'Bit'])
    assert (p.eda_bit(33, 45) == ['Eda', 34, 'Bit', 'Eda', 37, 38, 'Eda', 'Bit', 41, 'Eda', 43, 44, 'EdaBit'])
    assert (p.eda_bit(50, 90) == ['Bit', 'Eda', 52, 53, 'Eda', 'Bit', 56, 'Eda', 58, 59, 'EdaBit', 61, 62, 'Eda', 64, 'Bit', 'Eda', 67, 68, 'Eda', 'Bit', 71, 'Eda', 73, 74, 'EdaBit', 76, 77, 'Eda', 79, 'Bit', 'Eda', 82, 83, 'Eda', 'Bit', 86, 'Eda', 88, 89, 'EdaBit'])

def test_count_palindromes():
    assert (p.count_palindromes(1, 10) == 9)
    assert (p.count_palindromes(555, 556) == 1)
    assert (p.count_palindromes(878, 898) == 3)
    assert (p.count_palindromes(8, 34) == 5)
    assert (p.count_palindromes(1550, 1556) == 1)

def test_setify():
    assert (p.setify([1, 3, 3, 5, 5]) == [1, 3, 5])
    assert (p.setify([4, 4, 4, 4]) == [4])
    assert (p.setify([5, 7, 8, 9, 10, 15]) == [5, 7, 8, 9, 10, 15])
    assert (p.setify([5, 9, 9]) == [5, 9])
    assert (p.setify([1, 2, 3, 4, 5, 5, 6, 6, 7]) == [1, 2, 3, 4, 5, 6, 7])
    assert (p.setify([1, 1, 2, 2, 2]) == [1, 2])

def test_get_student_names():
    assert (p.get_student_names({
        "Student 1": "Steve",
        "Student 2": "Becky",
        "Student 3": "John"
    }) == ["Becky", "John", "Steve"])

    assert (p.get_student_names({
        "Student 1": "Jacek",
        "Student 2": "Ewa",
        "Student 3": "Zygmunt",
        "Student 4": "Tomek"
    }) == ["Ewa", "Jacek", "Tomek", "Zygmunt"])

def test_greet_people():
    assert (p.greet_people(["Kyrill"]) == "Hello Kyrill")
    assert (p.greet_people(["Kyrill", "Mom", "Dad", "Zuzu"]) == "Hello Kyrill, Hello Mom, Hello Dad, Hello Zuzu")
    assert (p.greet_people([]) == "")