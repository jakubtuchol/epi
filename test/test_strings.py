from src.strings import int_to_string, string_to_int, convert_base, \
        check_palindrome

class TestIntToString(object):
    '''
    Question 7.1
    '''
    def test_basic(self):
        assert '187' == int_to_string(187)
        assert '5151' == int_to_string(5151)

    def test_negative(self):
        assert '-1155' == int_to_string(-1155)
        assert '-188' == int_to_string(-188)

class TestStringToInt(object):
    '''
    Question 7.1
    '''
    def test_basic(self):
        assert 187 == string_to_int('187')
        assert 5151 == string_to_int('5151')

    def test_negative(self):
        assert -1155 == string_to_int('-1155')
        assert -188 == string_to_int('-188')

class TestConvertBase(object):
    '''
    Question 7.2
    '''
    def test_basic_conversion(self):
        assert u'1A7' == convert_base(u'615',7,13)

    def test_binary_conversion(self):
        assert u'4' == convert_base(u'100', 2, 10)


class TestCheckPalindrome(object):
    '''
    Question 7.5
    '''
    def test_classic_case(self):
        assert check_palindrome('amanaplanacanalpanama')
        assert check_palindrome('ablewasiereisawelba')

    def test_wrong_case(self):
        assert not check_palindrome('rayaray')
        assert not check_palindrome('amanaplanacanalpanam')

    def test_punctuation_case(self):
        assert check_palindrome('A man, a plan, a canal, Panama!')
        assert check_palindrome('Able was I, ere I saw Elba!')

    def test_punctuated_non_palindrome(self):
        assert not check_palindrome('A man, a 8 plan, a canal, Panama!')
        assert not check_palindrome('Ray, a Ray')
