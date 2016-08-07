from src.strings import int_to_string, string_to_int, convert_base

class TestIntToString:
    def test_basic(self):
        assert '187' == int_to_string(187)
        assert '5151' == int_to_string(5151)

    def test_negative(self):
        assert '-1155' == int_to_string(-1155)
        assert '-188' == int_to_string(-188)

class TestStringToInt:
    def test_basic(self):
        assert 187 == string_to_int('187')
        assert 5151 == string_to_int('5151')

    def test_negative(self):
        assert -1155 == string_to_int('-1155')
        assert -188 == string_to_int('-188')

class TestConvertBase:
    def test_basic_conversion(self):
        assert u'1A7' == convert_base(u'615',7,13)

    def test_binary_conversion(self):
        assert u'4' == convert_base(u'100', 2, 10)
