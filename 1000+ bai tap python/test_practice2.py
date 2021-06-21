from practice2 import Practice2
import datetime

p = Practice2()

def test_XO():
    assert p.XO("")
    assert p.XO("ooxx") == True
    assert p.XO("xooxx") == False
    assert p.XO("ooxXm") == True
    assert p.XO("zpzpzpp") == True
    assert p.XO("zzoo") == False
    assert p.XO("Xo") == True
    assert p.XO("x") == False
    assert p.XO("o") == False
    assert p.XO("xxxoo") == False
    assert p.XO("") == True

def test_weight():
    assert p.weight(4, 10) == 0.5
    assert p.weight(30, 60) == 169.65
    assert p.weight(15, 10) == 7.07
    assert p.weight(20, 40) == 50.27
    assert p.weight(100, 30) == 942.48
    assert p.weight(200, 300) == 37699.11
    assert p.weight(15, 23) == 16.26
    assert p.weight(22, 44) == 66.9

def test_card_hide():
    assert p.card_hide("1234123456785678") == "************5678"
    assert p.card_hide("8754456321113213") == "************3213"
    assert p.card_hide("35123413355523") == "**********5523"

def test_filter_list():
    assert p.filter_list([1, 2, "a", "b"]) == [1, 2]
    assert p.filter_list([1, "a", "b", 0, 15]) == [1, 0, 15]
    assert p.filter_list([1, 2, "aasf", "1", "123", 123]) == [1, 2, 123]
    assert p.filter_list(["jsyt", 4, "yt", "6"]) == [4]
    assert p.filter_list(["r", 5, "y", "e", 8, 9]) == [5, 8, 9]
    assert p.filter_list(["a", "e", "i", "o", "u"]) == []
    assert p.filter_list([4, "z", "f", 5]) == [4, 5]
    assert p.filter_list(["abc", 123]) == [123]
    assert p.filter_list(["$%^", 567, "&&&"]) == [567]
    assert p.filter_list(["w", "r", "u", 43, "s", "a", 76, "d", 88]) == [43, 76, 88]

def test_reverse():
    assert p.reverse("Hello World") == "DLROw OLLEh"
    assert p.reverse("ReVeRsE") == "eSrEvEr"
    assert p.reverse("") == ""
    assert p.reverse("Radar") == "RADAr"

def test_time_for_milk_and_cookies():
    assert (p.time_for_milk_and_cookies(datetime.date(2013, 12, 24)) == True)
    assert (p.time_for_milk_and_cookies(datetime.date(3000, 12, 24)) == True)
    assert (p.time_for_milk_and_cookies(datetime.date(2013, 1, 23)) == False)
    assert (p.time_for_milk_and_cookies(datetime.date(2010, 11, 2)) == False)
    assert (p.time_for_milk_and_cookies(datetime.date(1980, 9, 24)) == False)

def test_evenly_divisible():
    assert (p.evenly_divisible(1, 10, 2) == 30)
    assert (p.evenly_divisible(1, 10, 3) == 18)
    assert (p.evenly_divisible(0, 12, 3) == 30)
    assert (p.evenly_divisible(-10, -1, 2) == -30)
    assert (p.evenly_divisible(-10, -1, 3) == -18)
    assert (p.evenly_divisible(1, 10, 20) == 0)
    assert (p.evenly_divisible(-10, 10, 2) == 0)

def test_hamming_distance():
    assert (p.hamming_distance("abcde", "bcdef") == 5)
    assert (p.hamming_distance("abcde", "abcde") == 0)
    assert (p.hamming_distance("strong", "strung") == 1)

def test_count_ones():
    assert (p.count_ones(12) == 2)
    assert (p.count_ones(0) == 0)
    assert (p.count_ones(100) == 3)
    assert (p.count_ones(101) == 4)
    assert (p.count_ones(999) == 8)
    assert (p.count_ones(123456789) == 16)
    assert (p.count_ones(1234567890) == 12)

def test_name_shuffle():
    assert (p.name_shuffle("Donald Trump") == "Trump Donald")
    assert (p.name_shuffle("Rosie O'Donnel") == "O'Donnel Rosie")
    assert (p.name_shuffle("Seymour Butts") == "Butts Seymour")
    assert (p.name_shuffle("Ebony Greene") == "Greene Ebony")
    assert (p.name_shuffle("Ken Kennedy") == "Kennedy Ken")
    assert (p.name_shuffle("Allison Gonzalez") == "Gonzalez Allison")
    assert (p.name_shuffle("Albert Frazier") == "Frazier Albert")
    assert (p.name_shuffle("Eloise Hopkins") == "Hopkins Eloise")
    assert (p.name_shuffle("Donnie Welch") == "Welch Donnie")
    assert (p.name_shuffle("Vernon Thomas") == "Thomas Vernon")


