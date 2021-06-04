import demo2
import pytest

def test1():
    assert demo2.add(10, 5) == 20

def test2():
    assert demo2.sub(10, 5) == 5

def test3():
    assert demo2.multiply(10, 5) == 15

def test4():
    with pytest.raises(ZeroDivisionError) as z:
        return 1 / 0

    assert 'division by zero' in str(z.value)


