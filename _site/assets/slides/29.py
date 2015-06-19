class Range:
    """An implicit sequence of consecutive integers.

    >>> r = Range(3, 12)
    >>> len(r)
    9
    >>> r[3]
    6
    """
    def __init__(self, start, end=None):
        if end is None:
            start, end = 0, start
        self.start = start
        self.end = end

    def __repr__(self):
        return 'Range({0}, {1})'.format(self.start, self.end)

    def __len__(self):
        return max(0, self.end - self.start)

    def __getitem__(self, k):
        if k >= len(self):
            raise IndexError('index out of range')
        return self.start + k

class RangeIter:
    """An iterator over integers.

    >>> ri = RangeIter(3, 7)
    >>> next(ri)
    3
    >>> next(ri)
    4
    >>> next(ri)
    5
    """

    def __init__(self, start, end):
        self.next = start
        self.end = end

    def __next__(self):
        if self.next >= self.end:
            raise StopIteration
        result = self.next
        self.next += 1
        return result

class LetterIter:
    """An iterator over letters.

    >>> a_to_c = LetterIter('a', 'c')
    >>> next(a_to_c)
    'a'
    >>> next(a_to_c)
    'b'
    >>> next(a_to_c)
    Traceback (most recent call last):
        ...
    StopIteration
    """
    def __init__(self, start='a', end='e'):
        self.next_letter = start
        self.end = end

    def __next__(self):
        if self.next_letter >= self.end:
            raise StopIteration
        result = self.next_letter
        self.next_letter = chr(ord(result)+1)
        return result

class Letters:
    """An implicit sequence of letters.

    >>> b_to_k = Letters('b', 'k')
    >>> first_iterator = b_to_k.__iter__()
    >>> next(first_iterator)
    'b'
    >>> next(first_iterator)
    'c'
    >>> second_iterator = iter(b_to_k)
    >>> second_iterator.__next__()
    'b'
    >>> first_iterator.__next__()
    'd'
    >>> first_iterator.__next__()
    'e'
    >>> second_iterator.__next__()
    'c'
    >>> second_iterator.__next__()
    'd'
    """
    def __init__(self, start='a', end='e'):
        self.start = start
        self.end = end

    def __iter__(self):
        return LetterIter(self.start, self.end)

def built_in_demo():
    """Using built-in sequence functions.

    >>> b_to_e = Letters('b', 'e')
    >>> caps = map(lambda x: x.upper(), b_to_e)
    >>> next(caps)
    'B'
    >>> next(caps)
    'C'
    >>> s = range(3, 7)
    >>> doubled = map(double, s)
    >>> next(doubled)
    *** 3 => 6 ***
    6
    >>> next(doubled)
    *** 4 => 8 ***
    8
    >>> list(doubled)
    *** 5 => 10 ***
    *** 6 => 12 ***
    [10, 12]
    >>> f = lambda x: x < 10
    >>> a = filter(f, map(double, reversed(s)))
    >>> list(a)
    *** 6 => 12 ***
    *** 5 => 10 ***
    *** 4 => 8 ***
    *** 3 => 6 ***
    [8, 6]
    """

def double(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x

def letters_generator(next_letter, end):
    """A generator function that returns an iterator over letters.

    >>> list(letters_generator('a', 'e'))
    ['a', 'b', 'c', 'd']
    """
    while next_letter < end:
        yield next_letter
        next_letter = chr(ord(next_letter)+1)
