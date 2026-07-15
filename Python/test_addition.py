from Calculater import add, subtract, multiply, divide, power, modulus, floor_divide

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_multiply_positive_numbers():
    assert multiply(4, 3) == 12

def test_divide_positive_numbers():
    assert divide(10, 2) == 5

def test_power_positive_numbers():
    assert power(2, 3) == 8

def test_modulus_positive_numbers():
    assert modulus(10, 3) == 1

def test_floor_divide_positive_numbers():
    assert floor_divide(10, 3) == 3
    assert add(-2, -3) == -5
def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2
def test_multiply_negative_numbers():
    assert multiply(-4, -3) == 12
def test_divide_negative_numbers():
    assert divide(-10, -2) == 5
def test_power_negative_numbers():
    assert power(-2, 3) == -8
def test_modulus_negative_numbers():
    assert modulus(-10, 3) == 2
def test_floor_divide_negative_numbers():
    assert floor_divide(-10, 3) == -4
def test_divide_by_zero():
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."


def test_add_zero():
    assert add(0, 5) == 5

def test_add_positive_and_negative():
    assert add(5, -3) == 2

def test_add_floats():
    assert add(2.5, 3.1) == 5.6