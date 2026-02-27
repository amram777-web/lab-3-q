from math_tools import add, multiply, is_even, subtract, max_of_three, is_palindrome, find_min, remove_duplicates

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
    
def test_find_min():   
    assert find_min([3, 1, 4, 2]) == 1
    assert find_min([-5, -2, -9]) == -9
    assert find_min([10, 7, 3]) == 3
    assert find_min([0, 5, 2]) == 0
    assert find_min([8]) == 8
    print("test_find_min: ALL PASSED")

def test_remove_duplicates():
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 1, 3, 2, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([1, "1", 1, "1"]) == [1, "1"]
    assert remove_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
    print("test_remove_duplicates: ALL PASSED")
#Run all tests
test_add()
test_multiply()
test_is_even()
test_subtract()
test_max_of_three()
test_is_palindrome()
test_find_min()
test_remove_duplicates()
print("--- All tests passed!---")