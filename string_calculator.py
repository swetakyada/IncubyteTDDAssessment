import re

def add(numbers) :
    sum = 0
    if len(numbers) == 0 :
        return sum
    elif len(numbers) == 1 and numbers >= '0' and numbers <= '9' :
        return int(numbers)
    nums = [int(x.strip()) for x in re.split(',|\n', numbers)]
    for num in nums : 
        sum += num
    return sum

def test_string_calculator() :

    assert(add("") == 0)
    assert(add("1") == 1)
    assert(add("1,2") == 3)
    assert(add("1,2,3") == 6)
    assert(add("1\n2,3") == 6)
    # assert(add("//;\n1;2") == 3)
    # assert(add("1,-2,3") == Exception())
    # assert(add("\n1,-2,3;-4") == Exception())
    # assert(add("2,1000") == 1002)
    # assert(add("2,1001") == 2)
    # assert(add("//[***]\n1***2***3") == 6)
    # assert(add("//[*][%]\n1*2%3") == 6)

    print("All tests Passed")

test_string_calculator()