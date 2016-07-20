from src.strings import int_to_string, string_to_int

class TestIntToString:
    def test_basic(self):
        assert '187' == int_to_string(187)
        assert '5151' == int_to_string(5151)

    def test_negative(self):
        assert '-1155' == int_to_string(-1155)
        assert '-188' == int_to_string(-188)
