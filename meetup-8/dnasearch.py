import pytest

TESTCASES = (  # expected, search, sequence
    (True,  'TCCG',         'AATTCCGG'),
    (False, 'AATTT',        'AATTCCGG'),
    (True,  'ATCGATCGAA',   'ATCGATCGATCGAA'),
    (False,  'ATCGAA',      'ATCGATCGATCGA'),
)

@pytest.mark.parametrize('expected, search, sequence', TESTCASES)
def test(expected, search, sequence):
    assert expected is match(search, sequence)

def match(search, s):
    return match_trivial(search, s)


############################################################

@pytest.mark.parametrize('expected, search, sequence', TESTCASES)
def test_testcases(expected, search, sequence):
    assert expected is match_trivial(search, sequence)

def match_trivial(search, s):
    ''' Trivial to do in Python, though it's not clear what the
        algorithmic complexity of this is.

        This would make a good quickcheck condition.
    '''
    return search in s
