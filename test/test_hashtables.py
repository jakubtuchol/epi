from src.hashtables import find_anagrams
from src.hashtables import find_longest_distinct_subarray
from src.hashtables import find_nearest_repetition
from src.hashtables import IsbnCache
from src.hashtables import palindromic_permutation


class TestFindAnagrams(object):
    """
    Question 13.1
    """

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
            {'debitcard', 'badcredit'},
            {'elvis', 'lives', 'levis'},
            {'silent', 'listen'},
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


class TestPalindromicPermutation(object):
    """
    Question 13.2
    """

    def test_basic_case(self):
        assert palindromic_permutation('civic')
        assert palindromic_permutation('ivicc')
        assert palindromic_permutation('aabbcadad')

    def test_basic_negative_case(self):
        assert not palindromic_permutation('civil')
        assert not palindromic_permutation('livci')


class TestIsbnCache(object):
    """
    Question 13.4
    """

    def test_serial_insert_removes_least_recent(self):
        isbns = [
            ('1101874937', 16.51),
            ('0393245446', 11.71),
            ('1455561789', 13.99),
            ('0062414216', 17.50),
            ('081298840X', 15.00),
            ('0553447432', 16.71),
            ('081299860X', 16.20),
            ('0812997743', 18.36),
            ('1616204583', 17.65),
            ('1610395832', 14.93),
        ]
        cache = IsbnCache(5)

        # insert first five elements
        for isbn in isbns[:5]:
            cache.insert(isbn[0], isbn[1])

        # check that each of these are in cache
        for isbn in isbns[:5]:
            assert isbn[0] in cache.contents
            assert cache.tail.val == isbn[0]
            assert isbn[1] == cache.lookup(isbn[0])
            assert cache.head == cache.contents[isbn[0]]


class TestFindNearestRepetition(object):
    """
    Question 13.7
    """

    def test_book_example(self):
        words = [
            'All', 'work', 'and',
            'no', 'play', 'makes',
            'for', 'no', 'work',
            'no', 'fun', 'and',
            'no', 'results',
        ]
        assert 2 == find_nearest_repetition(words)

    def test_repetitions(self):
        words = [
            'no', 'no', 'no',
        ]
        assert 1 == find_nearest_repetition(words)

    def test_all_unique(self):
        words = [
            'All', 'work', 'and',
            'no', 'play', 'makes',
        ]
        assert None is find_nearest_repetition(words)


class TestFindLongestDistinctSubarray(object):
    """
    Question 13.10
    """

    def test_book_example(self):
        ls = ['f', 's', 'f', 'e', 't', 'w', 'e', 'n', 'w', 'e']
        expected = ['s', 'f', 'e', 't', 'w']
        assert expected == find_longest_distinct_subarray(ls)

    def test_repeating_example(self):
        ls = ['f'] * 12
        assert ['f'] == find_longest_distinct_subarray(ls)

    def test_geeks_example(self):
        ls = 'geeksforgeeks'
        assert 'ksforge' == find_longest_distinct_subarray(ls)
