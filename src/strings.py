from math import floor


def int_to_string(num):
    '''
    Problem 7.1
    convert an integer to a string, without using `str`
    '''
    negative = num < 0
    output = []
    if negative: num *= -1

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
    negative = string[0] == '-'
    if negative: string = string[1:]

    idx = 0
    output = 0

    while idx < len(string):
        low = ord(string[idx]) - ord('0')
        output = (output * 10) + low
        idx += 1

    if negative: output *= -1
    return output


def convert_base(s, base1, base2):
    '''
    Problem 7.2
    Convert number from one base to another
    '''
    # Convert string to int
    negative = s[0] == '-'
    begin = 1 if negative else 0

    num = 0
    # converting string to int
    for char in s[begin:]:
        num *= base1
        num += int(char) if char.isnumeric() else ord(char) - ord('A') + 10

    # converting int to string
    result = []
    while num:
        remainder = num % base2
        result.append(chr(ord('A') + remainder - 10) if remainder >= 10 else str(remainder))
        num /= base2

    if len(result) == 0:
        return '0'

    if negative:
        result.append('-')

    result.reverse()
    return unicode(''.join(result), 'utf-8')


def check_palindrome(string):
    '''
    Question 7.5: Check palindromicity of string
    '''
    begin = 0
    end = len(string) - 1

    while begin < end:
        while not string[begin].isalnum() and begin < end:
            begin += 1
        while not string[end].isalnum() and begin < end:
            end -= 1

        if string[begin].lower() != string[end].lower():
            return False
        begin += 1
        end -= 1
    return True

def reverse_words(sentence):
    '''
    Question 7.6: Reverse space-separated words in string
    '''
    split_sentence = sentence.split()
    return ' '.join(reversed(split_sentence))


def get_phone_mnemonics(number):
    '''
    Question 7.7: Generate mnemonics for phone numbers
    '''
    keymapping = {
        '0': [''],
        '1': [''],
        '2': ['A','B','C'],
        '3': ['D','E','F'],
        '4': ['G','H','I'],
        '5': ['J','K','L'],
        '6': ['M','N','O'],
        '7': ['P','Q','R','S'],
        '8': ['T','U','V'],
        '9': ['W','X','Y','Z'],
    }
    if not len(number):
        return ['']

    first_num = number[0]
    rest_num = number[1:]

    res = []
    for letter in keymapping[first_num]:
        for rest in get_phone_mnemonics(rest_num):
            res.append(''.join([letter,rest]))

    return res
