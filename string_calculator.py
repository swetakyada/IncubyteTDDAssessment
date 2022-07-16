import re

def add(numbers) :
    try :
        if len(numbers) == 0 :  # if the string is empty then return 0
            return 0
        elif len(numbers) == 1 and numbers >= '0' and numbers <= '9' :  # if string contains one number then return it 
            return int(numbers)

        delim = ','     # default delimiter
        delims = []     # list of delimiters
        i = 0           

        # finding delimiters from the strating of the string 
        if numbers[0] == numbers[1] == '/' :    
            i += 2
            if numbers[2] == '[' :
                while numbers[i] != '\n' :
                    i += 1
                    dlm = ''
                    while numbers[i] != ']' :
                        dlm += numbers[i]
                        i += 1
                    delims.append(dlm)
                    i += 1
                i += 1
            elif numbers[3] == '\n' :
                delim = numbers[i]
                i += 2

        nums = []   # list of numbers
        neg_nums = []   # list of negative numbers

        if delim == ',' and len(delims) == 0 :  # for numbers with default delimiters as ',' or '\n'
            numbers = numbers.replace('\n', ',')
            nums = [int(x.strip()) for x in numbers.split(delim)]
        elif len(delims) == 0 :     # for numbers with one single character delimiter
            nums = [int(x.strip()) for x in numbers[i:].split(delim)]
        else :      # for numbers with multiple different delimiters
            numbers = numbers[i:]
            for dlm in delims :
                numbers = numbers.replace(dlm, ',')
            nums = [int(x.strip()) for x in re.split(',', numbers)]

        sum = 0
        for num in nums : 
            if num < 0 :    # if the number is negative then we add it to the negative numbers list
                neg_nums.append(num)
            if num <= 1000 :    # consider only the numbers which are less than or equal to 1000
                sum += num

        try :
            if len(neg_nums) > 0 :  # if there is any negative number, then raise and exception 
                neg_list = ','.join(str(x) for x in neg_nums)
                raise Exception("Negatives not allowed : " + neg_list)
        except Exception as e :     # handle the exception
            return str(e)

        return sum
    except Exception as e :
        return "Invalid input"