def inc(x):
    return x + 1

def div_by_zero(n):
    return n/0

def test_answer1():
    assert inc(4) == 3

def test_answer2():
    assert inc(10) == 11

def test_answer3():
    assert 1 / 0