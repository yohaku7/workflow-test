from src.module import foo, bar

def test_foo_1():
    assert foo(1, 2) == 3
    assert foo(0, 0) == 0

    assert bar(2, 1) == 1
    assert bar(5, 2) != 3  # oh my gosh!

