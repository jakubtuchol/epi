from src.strings import check_palindrome
from src.strings import convert_base
from src.strings import get_phone_mnemonics
from src.strings import int_to_string
from src.strings import look_say
from src.strings import reverse_words
from src.strings import string_to_int


class TestIntToString(object):
    """
    Question 7.1
    """

    def test_basic(self):
        assert '187' == int_to_string(187)
        assert '5151' == int_to_string(5151)

    def test_negative(self):
        assert '-1155' == int_to_string(-1155)
        assert '-188' == int_to_string(-188)


class TestStringToInt(object):
    """
    Question 7.1
    """

    def test_basic(self):
        assert 187 == string_to_int('187')
        assert 5151 == string_to_int('5151')

    def test_negative(self):
        assert -1155 == string_to_int('-1155')
        assert -188 == string_to_int('-188')


class TestConvertBase(object):
    """
    Question 7.2
    """

    def test_basic_conversion(self):
        assert u'1A7' == convert_base(u'615', 7, 13)

    def test_binary_conversion(self):
        assert u'4' == convert_base(u'100', 2, 10)


class TestCheckPalindrome(object):
    """
    Question 7.5
    """

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


class TestReverseWord(object):
    """
    Question 7.6
    """
    def test_reverse_basic_word(object):
        assert 'Alice likes Bob' == reverse_words('Bob likes Alice')

    def test_another_case(object):
        assert 'ram is costly' == reverse_words('costly is ram')


class TestGetPhoneMnemonics(object):
    """
    Question 7.7
    """

    def test_limited_example(self):
        results = [
            'AD', 'AE', 'AF',
            'BD', 'BE', 'BF',
            'CD', 'CE', 'CF',
        ]
        assert results == get_phone_mnemonics('23')

    def test_longer_example(self):
        results = get_phone_mnemonics('2276696')
        assert 'ACRONYM' in results
        assert 'ABPOMZN' in results


class TestLookSay(object):
    """
    Question 7.8
    """

    def test_look_say(self):
        assert '1' == look_say(1)
        assert '11' == look_say(2)
        assert '21' == look_say(3)
        assert '1211' == look_say(4)

    def test_long_example(self):
        assert '1113213211' == look_say(8)
