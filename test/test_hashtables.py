from src.hashtables import find_anagrams

class TestFindAnagrams:
    '''
    Question 13.1
    '''
    def test_find_anagrams(self):
        words = [
            'debitcard',
            'elvis',
            'silent',
            'badcredit',
            'lives',
            'freedom',
            'listen',
            'levis',
            'money',
        ]

        expected = [
            {'debitcard','badcredit'},
            {'elvis','lives','levis'},
            {'silent','listen'},
        ]
        resolved = find_anagrams(words)
        # turns out, asserting equality between
        # two maps of strings to sets is quite difficult
        assert len(expected) == len(resolved)

        # search dicts until find matching set
        for expect in expected:
            # get single element from expected set
            elt = next(iter(expect))
            match = None
            for res in resolved:
                if elt in res:
                    match = res
                    break
            assert match is not None
            for element in expect:
                assert element in res
