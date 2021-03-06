from math import floor
from os import SEEK_END


def int_to_string(num):
    """
    Problem 7.1
    convert an integer to a string, without using `str`
    """
    negative = num < 0
    output = []
    if negative:
        num *= -1

    while num > 0:
        code = ord('0') + (num % 10)
        output.insert(0, chr(code))
        num = int(floor(num / 10))

    if negative:
        output.insert(0, '-')
    return ''.join(output)


def string_to_int(string):
    """
    Problem 7.1
    convert a string to an integer, without using `int`
    """
    negative = string[0] == '-'
    if negative:
        string = string[1:]

    idx = 0
    output = 0

    while idx < len(string):
        low = ord(string[idx]) - ord('0')
        output = (output * 10) + low
        idx += 1

    if negative:
        output *= -1
    return output


def convert_base(s, base1, base2):
    """
    Problem 7.2
    Convert number from one base to another
    """
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
        result.append(chr(ord('A') + remainder - 10)
                      if remainder >= 10 else str(remainder))
        num /= base2

    if len(result) == 0:
        return '0'

    if negative:
        result.append('-')

    result.reverse()
    return unicode(''.join(result), 'utf-8')


def get_spreadsheet_column(code):
    """
    Question 7.3: Compute spreadsheet column encoding
    """
    cur_power = 1
    total = 0
    for elt in code[::-1]:
        total += cur_power * (ord(elt) - ord('A') + 1)
        cur_power *= 26
    return total


def replace_and_remove(ls, size):
    """
    Question 7.4: Apply the following rules to an array
    of characters
        Replace each 'a' by two 'd's
        delete each entry containing 'b'
    """
    write_idx = 0
    num_a = 0
    for idx in xrange(size):
        if ls[idx] != 'b':
            if ls[idx] == 'a':
                num_a += 1
            ls[write_idx] = ls[idx]
            write_idx += 1

    cur_idx = write_idx - 1
    write_idx = write_idx + num_a - 1

    while write_idx >= 0:
        if ls[cur_idx] == 'a':
            ls[write_idx] = 'd'
            write_idx -= 1
            ls[write_idx] = 'd'
            write_idx -= 1
        else:
            ls[write_idx] = ls[cur_idx]
            write_idx -= 1
        cur_idx -= 1

    return ls


def check_palindrome(string):
    """
    Question 7.5: Check palindromicity of string
    """
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
    """
    Question 7.6: Reverse space-separated words in string
    """
    split_sentence = sentence.split()
    return ' '.join(reversed(split_sentence))


def get_phone_mnemonics(number):
    """
    Question 7.7: Generate mnemonics for phone numbers
    """
    keymapping = {
        '0': [''],
        '1': [''],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z'],
    }
    if not len(number):
        return ['']

    first_num = number[0]
    rest_num = number[1:]

    res = []
    for letter in keymapping[first_num]:
        for rest in get_phone_mnemonics(rest_num):
            res.append(''.join([letter, rest]))

    return res


def look_say(n):
    """
    Question 7.8: Return nth step in looksay sequence
    """
    x = '1'

    for _ in xrange(1, n):
        x = look_say_helper(x)
    return x


def look_say_helper(s):
    run = 0
    char = ''

    string = []

    for c in s:
        if char != c:
            if run:
                string.append(str(run))
                string.append(char)
            char = c
            run = 1
        else:
            run += 1

    if run:
        string.append(str(run))
        string.append(char)

    return ''.join(string)


def roman_to_integer(roman):
    """
    Question 7.9: Convert from roman
    numeral to decimal
    """
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    pairs = {
        'I': None,
        'V': 'I',
        'X': 'I',
        'L': 'X',
        'C': 'X',
        'D': 'C',
        'M': 'C',
    }
    total = 0

    last_roman = None
    for elt in roman:
        if last_roman and last_roman == pairs[elt]:
            total -= 2 * values[last_roman]
        total += values[elt]

        last_roman = elt

    return total


def get_valid_ip_address(ls):
    """
    Question 7.10: Compute all valid IP addresses
    from decimal string, given that
    """
    ips = []
    # loop over first ip packet
    first_idx = 1
    while first_idx < 4 and first_idx < len(ls):
        second_idx = 1
        while second_idx < 4 and \
                first_idx + second_idx < len(ls):
            third_idx = 1
            while third_idx < 4 and \
                    first_idx + second_idx + third_idx < len(ls):
                first_octet = ls[:first_idx]
                second_octet = ls[first_idx:first_idx + second_idx]
                third_octet = ls[first_idx +
                                 second_idx:first_idx + second_idx + third_idx]
                fourth_octet = ls[first_idx + second_idx + third_idx:]
                octets = [first_octet, second_octet, third_octet, fourth_octet]
                if all([int(octet) <= 255 for octet in octets]):
                    ips.append('.'.join(octets))
                third_idx += 1
            second_idx += 1
        first_idx += 1

    return ips


def snake_string(ls):
    """
    Question 7.11: Write a string sinusoidally
    """
    result = []
    strlen = len(ls)
    for idx in xrange(1, strlen, 4):
        result.append(ls[idx])

    for idx in xrange(0, strlen, 2):
        result.append(ls[idx])

    for idx in xrange(3, strlen, 4):
        result.append(ls[idx])

    return ''.join(result)


def encode_string(ls):
    """
    Question 7.12: Implement run-length encoding
    for strings
    """
    result = []
    last = ls[0]
    count = 1
    for elt in ls[1:]:
        if elt != last:
            result.append(str(count))
            result.append(last)
            count = 1
        else:
            count += 1
        last = elt
    result.append(str(count))
    result.append(last)

    return ''.join(result)


def decode_string(ls):
    """
    Question 7.12: Implement run-length decoding
    for strings
    """
    result = []
    count = 0

    for elt in ls:
        if elt.isdigit():
            count = (count * 10) + int(elt)
        else:
            result += [elt for _ in xrange(count)]
            count = 0
    return ''.join(result)


def tail(file_name, num_lines):
    """
    Question 7.13: Implement UNIX tail command
    """
    lines = []
    for line in reverse_readline(file_name):
        if not num_lines:
            break
        lines.append(line)
        num_lines -= 1

    lines.reverse()
    return '\n'.join(lines)


def reverse_readline(filename, buf_size=8192):
    """
    Generator to read lines in reverse
    """
    with open(filename) as fp:
        segment = None
        offset = 0
        fp.seek(0, SEEK_END)
        file_size = remaining_size = fp.tell()
        while remaining_size > 0:
            offset = min(file_size, offset + buf_size)
            fp.seek(file_size - offset)
            buf = fp.read(min(remaining_size, buf_size))
            remaining_size -= buf_size
            lines = buf.split('\n')
            if segment is not None:
                if buf[-1] is not '\n':
                    lines[-1] += segment
                else:
                    yield segment
            segment = lines[0]
            for index in range(len(lines) - 1, 0, -1):
                if len(lines[index]):
                    yield lines[index].strip()
        # don't yield None if file was empty
        if segment is not None:
            yield segment.strip()
