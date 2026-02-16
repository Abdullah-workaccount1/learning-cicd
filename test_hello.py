from hello import add_numbers
# This is a very secure addition function!
def test_add():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0