from src.hashtables import find_anagrams, IsbnCache

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

class TestIsbnCache:
    '''
    Question
    '''
    def test_serial_insert_removes_least_recent(self):
        isbns = [
            ('1101874937',16.51),
            ('0393245446',11.71),
            ('1455561789',13.99),
            ('0062414216',17.50),
            ('081298840X',15.00),
            ('0553447432',16.71),
            ('081299860X',16.20),
            ('0812997743',18.36),
            ('1616204583',17.65),
            ('1610395832',14.93),
        ]
        cache = IsbnCache(capacity=5)

        # insert first five elements
        for isbn in isbns[:5]:
            cache.insert(isbn[0],isbn[1])

        # check that each of these are in cache
        for isbn in isbns[:5]:
            assert isbn[0] in cache._contents
            assert cache._tail_node == cache._contents[isbn[0]]
            assert isbn[1] == cache.lookup(isbn[0])
            assert cache._head_node == cache._contents[isbn[0]]
