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
    matchers = []
    for i in range(len(s)):
        c = s[i]
        new_matchers = []
        for m in matchers:
            if m.next(c):
                new_matchers.append(m)
        if c == search[0]:
            m = Matcher(search, i)
            assert m.next(c)            # Awkward; we already did this!
            new_matchers.append(m)
        matchers = new_matchers
    #   We could return a list of positions at which this was found
    new_matchers = []
    for m in matchers:
        if m.complete():
            new_matchers.append(m)
    matchers = new_matchers
    for m in matchers:
       print(m)
    return len(new_matchers) > 0

class Matcher:
    def __init__(self, search, loc=0):
        self.search = search
        self.loc = loc
        self.i = -1

    def next(self, c):
        " True if c is the next char we're looking for. "
        self.i += 1
        if self.complete():
            return True                 # Final state
        return c == self.search[self.i]

    def complete(self):
        return self.i == len(self.search)

    def __str__(self):
        return 'Matcher loc={} i={} len={} search={}' \
            .format(self.loc, self.i, len(self.search), self.search)

def test_matcher():
    assert     Matcher('').next('A')
    assert     Matcher('A').next('A')
    assert not Matcher('A').next('B')

    m = Matcher('ABC')
    assert not m.complete(); assert m.next('A')
    assert not m.complete(); assert m.next('B')
    assert not m.complete(); assert m.next('C')
    assert     m.complete(); assert m.next('D')

    m = Matcher('ABC')
    assert m.next('A')
    assert not m.next('C')

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
