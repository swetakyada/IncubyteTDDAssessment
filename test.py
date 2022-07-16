from string_calculator import add

# Testing
def test_string_calculator() :

    assert(add("") == 0)
    assert(add("1") == 1)
    assert(add("1,2") == 3)
    assert(add("1,2,3") == 6)
    assert(add("1,\n") == "Invalid input")
    assert(add("1\n2,3") == 6)
    assert(add("//;\n1;2") == 3)
    assert(add("1,-2,3") == "Negatives not allowed : -2")
    assert(add("1,-2\n3,-4") == "Negatives not allowed : -2,-4")
    assert(add("//;\n1;-2;3;4;-5") == "Negatives not allowed : -2,-5")
    assert(add("2,1000") == 1002)
    assert(add("2,1001") == 2)
    assert(add("//[***]\n1***2***3") == 6)
    assert(add("//[*][%]\n1*2%3") == 6)
    assert(add("//[**][%%%]\n1**2%%%3") == 6)

    print("All tests Passed")

test_string_calculator()