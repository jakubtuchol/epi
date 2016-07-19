def find_parity(x):
    parity = 0

    while x:
        parity += x & 1
        x >>= 1

    return parity % 2

def reverse_digits():
    '''
    Problem 5.8
    '''
    pass
