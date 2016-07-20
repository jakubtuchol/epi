from math import floor

def int_to_string(num):
    '''
    Problem 7.1
    convert an integer to a string, without using `str`
    '''
    negative = num < 0
    output = []
    if negative:
        num *= -1

    while num > 0:
        code = ord('0') + (num % 10)
        output.insert(0, chr(code))
        num = int(floor(num / 10))

    if negative: output.insert(0, '-')
    return ''.join(output)

def string_to_int(string):
    '''
    Problem 7.1
    convert a string to an integer, without using `int`
    '''
    pass
