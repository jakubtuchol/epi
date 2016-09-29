from mock import mock_open
from mock import patch

from src.strings import check_palindrome
from src.strings import convert_base
from src.strings import decode_string
from src.strings import encode_string
from src.strings import get_phone_mnemonics
from src.strings import get_spreadsheet_column
from src.strings import get_valid_ip_address
from src.strings import int_to_string
from src.strings import look_say
from src.strings import replace_and_remove
from src.strings import reverse_words
from src.strings import roman_to_integer
from src.strings import string_to_int
from src.strings import tail


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


class TestGetSpreadsheetColumn(object):
    """
    Question 7.3
    """

    def test_single_char(self):
        assert 1 == get_spreadsheet_column('A')
        assert 23 == get_spreadsheet_column('W')
        assert 26 == get_spreadsheet_column('Z')

    def test_double_chars(self):
        assert 27 == get_spreadsheet_column('AA')
        assert 51 == get_spreadsheet_column('AY')
        assert 52 == get_spreadsheet_column('AZ')
        assert 53 == get_spreadsheet_column('BA')
        assert 80 == get_spreadsheet_column('CB')
        assert 702 == get_spreadsheet_column('ZZ')

    def test_triple_chars(self):
        assert 705 == get_spreadsheet_column('AAC')


class TestReplaceRemove(object):
    """
    Question 7.4
    """

    def test_book_example(self):
        ls = ['a', 'c', 'd', 'b', 'b', 'c', 'a']
        expected = ['d', 'd', 'c', 'd', 'c', 'd', 'd']
        assert expected == replace_and_remove(ls, 7)

    def test_larger_example(self):
        ls = ['a', 'c', 'a', 'a', None, None, None]
        expected = ['d', 'd', 'c', 'd', 'd', 'd', 'd']
        assert expected == replace_and_remove(ls, 4)


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


class TestRomanToInteger(object):
    """
    Question 7.9
    """

    def test_single_nums(self):
        assert 1 == roman_to_integer('I')
        assert 5 == roman_to_integer('V')
        assert 10 == roman_to_integer('X')
        assert 50 == roman_to_integer('L')
        assert 100 == roman_to_integer('C')
        assert 500 == roman_to_integer('D')
        assert 1000 == roman_to_integer('M')

    def test_increment_nums(self):
        assert 7 == roman_to_integer('VII')
        assert 8 == roman_to_integer('VIII')
        assert 72 == roman_to_integer('LXXII')
        assert 33 == roman_to_integer('XXXIII')

    def test_decrement_nums(self):
        assert 9 == roman_to_integer('IX')
        assert 79 == roman_to_integer('LXXIX')
        assert 90 == roman_to_integer('XC')

    def test_large_numbers(self):
        assert 890 == roman_to_integer('DCCCXC')
        assert 1500 == roman_to_integer('MD')
        assert 1800 == roman_to_integer('MDCCC')
        assert 900 == roman_to_integer('CM')
        assert 707 == roman_to_integer('DCCVII')


class TestValidIpAddress(object):
    """
    Question 7.10
    """

    def test_book_example(self):
        dec_string = '19216811'
        expected = [
            '1.92.168.11',
            '19.2.168.11',
            '19.21.68.11',
            '19.216.8.11',
            '19.216.81.1',
            '192.16.81.1',
            '192.16.8.11',
            '192.168.1.1',
            '192.1.68.11',
        ]
        assert sorted(expected) == sorted(get_valid_ip_address(dec_string))


class TestEncodeString(object):
    """
    Question 7.12
    """

    def test_book_example(self):
        ls = 'aaaabcccaa'
        expected = '4a1b3c2a'
        assert expected == encode_string(ls)

    def test_single_run(self):
        ls = 'aaaaaaaaaa'
        expected = '10a'
        assert expected == encode_string(ls)


class TestDecodeString(object):
    """
    Question 7.12
    """

    def test_book_example(self):
        ls = '3e4f2e'
        expected = 'eeeffffee'
        assert expected == decode_string(ls)

    def test_continuous_example(self):
        ls = '12a'
        expected = 'aaaaaaaaaaaa'
        assert expected == decode_string(ls)


email_data = \
    """Message-ID: <27065550.1075858882700.JavaMail.evans@thyme>
    Date: Wed, 18 Jul 2001 10:32:00 -0700 (PDT)
    From: steven.kean@enron.com
    To: maureen.mcvicker@enron.com
    Subject: Board of Directors Meeting - August 14, 2001
    Mime-Version: 1.0
    Content-Type: text/plain; charset=us-ascii
    Content-Transfer-Encoding: quoted-printable
    X-From: Steven J Kean
    X-To: Maureen McVicker <Maureen McVicker/NA/Enron@Enron>
    X-cc:
    X-bcc:
    X-Folder: \SKEAN (Non-Privileged)\Kean, Steven J.\Sent Items
    X-Origin: Kean-S
    X-FileName: SKEAN (Non-Privileged).pst
    calendar and meeting file
    ---------------------- Forwarded by Steven J Kean/NA/Enron on 07/18/2001 07
    :32 AM ---------------------------
    From:=09Kelly Johnson/ENRON@enronXgate on 07/16/2001 03:22 PM
    To:=09Jeremy Blachman/HOU/EES@EES, Raymond Bowen/ENRON@enronXgate, Michael
    Brown/Enron@EUEnronXGate, Harold G Buchanan/HOU/EES@EES, Rick Buy/ENRON@enr
    onXgate, Richard Causey/ENRON@enronXgate, Wade Cline/ENRON_DEVELOPMENT@ENRO
    N_DEVELOPMENt, David Cox/Enron Communications@Enron Communications, James D
    errick/ENRON@enronXgate, Janet R Dietrich/HOU/EES@EES, Steve Elliott/Enron
    Communications@Enron Communications, Jim Fallon/Enron Communications@Enron
    Communications, Andrew S Fastow/ENRON@enronXgate, Mark Frevert/ENRON@enronX
    gate, Ben Glisan/HOU/ECT@ECT, Kevin Hannon/Enron Communications@Enron Commu
    nications, Rod Hayslett/ENRON@enronXgate, Stanley Horton/ENRON@enronXgate,
    James A Hughes/ENRON@enronXgate, Steven J Kean/NA/Enron@Enron, Louise Kitch
    en/ENRON@enronXgate, Mark Koenig/ENRON@enronXgate, John J Lavorato/ENRON@en
    ronXgate, Kenneth Lay/ENRON@enronXgate, Dan Leff/HOU/EES@EES, Danny McCarty
    /ET&S/Enron@Enron, Mike Mcconnell/ENRON@enronXgate, Rebecca McDonald/ENRON@
    enronXgate, Jeffrey McMahon/ENRON@enronXgate, Mark Metts/Enron@EnronXGate,
    Mark S Muller/HOU/EES@EES, Cindy Olson/ENRON@enronXgate, Lou L Pai/HOU/EES@
    EES, Mark Pickering/Enron@EUEnronXgate, Greg Piper/ENRON@enronXgate, Ken Ri
    ce/Enron Communications@Enron Communications, Matthew Scrimshaw/Enron@EUEnr
    onXGate, Jeffrey A Shankman/ENRON@enronXgate, Jeffrey Sherrick/ENRON@enronX
    gate, John Sherriff/ENRON@EUEnronXGate, Jeff Skilling/ENRON@enronXgate, Mar
    ty Sunde/HOU/EES@EES, Greg Whalley/ENRON@enronXgate
    cc:=09Jennifer Adams/Enron Communications@Enron Communications, Beverly Ade
    n/HOU/EES@EES, Julie Armstrong/Corp/Enron@ENRON, Connie Blackwood/ENRON@enr
    onXgate, Vivianna Bolen/ENRON@enronXgate, Loretta Brelsford/ENRON@enronXgat
    e, Jennifer Burns/ENRON@enronXgate, Alan Butler/EU/Enron@Enron, Kathy Campo
    s/ENRON@enronXgate, Kay Chapman/HOU/EES@EES, Inez Dauterive/HOU/ECT@ECT, Bi
    nky Davidson/HOU/EES@EES, Nicki Daw/ENRON@enronXgate, Sharon Dick/HOU/EES@E
    ES, Kathy Dodgen/HOU/EES@EES, Kerry Ferrari/Enron@EUEnronXGate, Dolores Fis
    her/Enron@EnronXGate, Rosalee Fleming/ENRON@enronXgate, Sue Ford/ENRON@enro
    nXgate, Mrudula Gadade/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Stephanie Harri
    s/ENRON@enronXgate, Linda Hawkins/ENRON@enronXgate, Kimberly Hillis/ENRON@e
    nronXgate, Mary Joyce/ENRON@enronXgate, Samantha Lopez-Dias/EU/Enron@Enron,
     Bridget Maronge/ENRON@enronXgate, Lucy Marshall/Enron Communications@Enron
     Communications, Stephanie Mcginnis/ENRON@enronXgate, Kathy McMahon/ENRON@e
    nronXgate, Maureen McVicker/NA/Enron@Enron, Karen Owens/HOU/EES@EES, Jana L
     Paxton/ENRON@enronXgate, Cathy Phillips/ENRON@enronXgate, "Rijo, Leah" <Le
    ah.Rijo@ENRON.com>@SMTP@enronXgate, Marsha Schiller/ENRON@enronXgate, Tammi
    e Schoppe/ENRON@enronXgate, Sherri Sera/ENRON@enronXgate, Caron Stark/ENRON
    @enronXgate, Sharon E Sullo/ENRON@enronXgate, Liz M Taylor/ENRON@enronXgate
    , Lauren Urquhart/Enron@EUEnronXGate, Christina Valdez/ENRON@enronXgate, Ve
    ronica Valdez/ENRON@enronXgate, Terry West/ENRON@enronXgate, Sharron Westbr
    ook/ENRON@enronXgate, Joannie Williamson/ENRON@enronXgate, Teresa Wright/EN
    RON@enronXgate=20
    Subject:=09Board of Directors Meeting - August 14, 2001
    =20
    Kelly M. Johnson
    Enron Corp.
    Executive Assistant
    Tel: (713) 853-6485
    Fax: (713) 853-2534
    E-Mail: kelly.johnson@enron.com"""


class TestTail(object):
    """
    Question 7.13
    """

    def test_extract_last_five_lines(self):
        expected_five = \
            """Enron Corp.
            Executive Assistant
            Tel: (713) 853-6485
            Fax: (713) 853-2534
            E-Mail: kelly.johnson@enron.com"""

        with patch('src.strings.open', mock_open(read_data=email_data)):
            received_tail = tail('email.txt', 5)

            clean_received = [
                line.strip()
                for line
                in received_tail.split('\n')
            ]
            clean_expected = [
                line.strip()
                for line
                in expected_five.split('\n')
            ]
            assert clean_expected == clean_received
