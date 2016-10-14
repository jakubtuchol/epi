def gcd(x, y):
    """
    Question 22.1: Find the greatest common divisor
    of two numbers without using multiplication,
    division, or the modulus operator
    :return:
    """
    if x == y:
        return x
    elif not (x & 1) and not (y & 1):
        # x even, y even
        return gcd(x >> 1, y >> 1) << 1
    elif not (x & 1) and (y & 1):
        # x even, y odd
        return gcd(x >> 1, y)
    elif (x & 1) and not (y & 1):
        # x odd, y even
        return gcd(x, y >> 1)
    elif x > y:
        return gcd(x - y, y)
    else:
        # x <= y
        return gcd(x, y - x)
