from math_tools import add, multiply, is_even, subtract, max_of_three, is_palindrome
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("test_add: ALL PASSED")
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) ==-10
    assert multiply(0, 100) == 0
    print("test_multiply: ALL PASSED")
def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("test_is_even: ALL PASSED")
def test_subtract():
    assert subtract(5,4)==1
    assert subtract(-3,1)==-4
    assert subtract(9,9)==0
    print("test_subtract: ALL PASSED")
def test_max_of_three():
    assert max_of_three(1, 5, 3) == 5
    assert max_of_three(7, 7, 3) == 7
    assert max_of_three(4, 4, 4) == 4
    assert max_of_three(-10, -5, -20) == -5
    assert max_of_three(-2, 0, 2) == 2
    assert max_of_three(1.5, 2.5, 2.4) == 2.5
    print("test_max_of_three: ALL PASSED")
def test_is_palindrome():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("nurses run") == True
    assert is_palindrome("race car") == True
    assert is_palindrome("Racecar") == False
    print("test_is_palindrome: ALL PASSED")
#Run all tests
test_add()
test_multiply()
test_is_even()
test_subtract()
test_max_of_three()
test_is_palindrome()
print("--- All tests passed!---")