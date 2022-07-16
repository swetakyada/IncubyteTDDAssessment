import re

def add(numbers) :
    sum = 0
    if len(numbers) == 0 :
        return sum
    elif len(numbers) == 1 and numbers >= '0' and numbers <= '9' :
        return int(numbers)
    delim = ','
    if numbers[0] == numbers[1] == '/' :
        if len(numbers) >= 4 and numbers[3] == '\n' :
            delim = numbers[2]
    nums = []
    neg_nums = []
    if delim == ',' :
        nums = [int(x.strip()) for x in re.split(',|\n', numbers)]
    else :
        nums = [int(x.strip()) for x in re.split(delim + '|\n', numbers[4:])]
    for num in nums : 
        if num < 0 :
            neg_nums.append(num)
        sum += num
    try :
        if len(neg_nums) > 0 :
            neg_list = ','.join(str(x) for x in neg_nums)
            raise Exception("Negatives not allowed : " + neg_list)
    except Exception as e :
        return str(e)
    return sum

def test_string_calculator() :

    assert(add("") == 0)
    assert(add("1") == 1)
    assert(add("1,2") == 3)
    assert(add("1,2,3") == 6)
    assert(add("1\n2,3") == 6)
    assert(add("//;\n1;2") == 3)
    assert(add("1,-2,3") == "Negatives not allowed : -2")
    assert(add("1,-2\n3,-4") == "Negatives not allowed : -2,-4")
    assert(add("//;\n1;-2;3;4;-5") == "Negatives not allowed : -2,-5")
    # assert(add("2,1000") == 1002)
    # assert(add("2,1001") == 2)
    # assert(add("//[***]\n1***2***3") == 6)
    # assert(add("//[*][%]\n1*2%3") == 6)

    print("All tests Passed")

test_string_calculator()