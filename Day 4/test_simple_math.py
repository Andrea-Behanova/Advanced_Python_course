from simple_math import simple_add, simple_sub, simple_mult, simple_div, poly_first, poly_second

def test_simple_math():
    assert simple_add(4,6) == 10
    assert simple_sub(9,5) == 4
    assert simple_mult(2,3) == 6
    assert simple_div(9,3) == 3
    assert poly_first(3, 1, 2) == 7
    assert poly_second(2, 5, 3, 1) == 15