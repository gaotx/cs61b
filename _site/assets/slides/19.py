def fib(n):
    """The nth Fibonacci number.

    >>> fib(20)
    6765
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def count(f):
    """Return a counted version of f with a call_count attribute.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count(fib)
    >>> fib(20)
    6765
    >>> fib.call_count
    21891
    """
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

def memo(f):
    """Memoize f.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count(fib)
    >>> fib(20)
    6765
    >>> fib.call_count
    21891
    >>> counted_fib = count(fib)
    >>> fib  = memo(counted_fib)
    >>> fib(20)
    6765
    >>> counted_fib.call_count
    21
    >>> fib(35)
    9227465
    >>> counted_fib.call_count
    36
    """
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

class Tree:
    """A tree with entry as its root value."""
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.entry, branches_str)

    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    """A Fibonacci tree.

    >>> fib_tree(4)
    Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
    """
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return Tree(left.entry + right.entry, (left, right))

def hailstone(n):
    """Print a hailstone sequence and return its length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone(3*n+1)

def is_int(x):
    return int(x) == x

def is_odd(n):
    return n % 2 == 1

def hailstone_tree(k, n=1):
    """Build a tree in which paths are hailstone sequences.

    >>> hailstone_tree(6)
    Tree(1, [Tree(2, [Tree(4, [Tree(8, [Tree(16, [Tree(32), Tree(5)])])])])])
     """
    if k == 1:
        return Tree(n)
    else:
        greater, less = 2*n, (n-1)/3
        branches = [hailstone_tree(k-1, greater)]
        if less > 1 and is_int(less) and is_odd(less):
            branches.append(hailstone_tree(k-1, int(less)))
        return Tree(n, branches)

def leaves(tree):
    """Return the leaf entries of a tree.

    >>> leaves(fib_tree(4))
    [0, 1, 1, 0, 1]
    >>> leaves(hailstone_tree(11))
    [1024, 170, 168, 160, 26, 24]
    """
    if tree.is_leaf():
        return [tree.entry]
    else:
        return sum([leaves(b) for b in tree.branches], [])

def longest_path_below(k, t):
    """Return the longest path through t of entries all less than k.

    >>> longest_path_below(20, hailstone_tree(10))
    [1, 2, 4, 8, 16, 5, 10, 3, 6, 12]
    """
    if t.entry >= k:
        return []
    elif t.is_leaf():
        return [t.entry]
    else:
        paths = [longest_path_below(k, b) for b in t.branches]
        return [t.entry] + max(paths, key=len)

class BinaryTree(Tree):
    """A tree with exactly two branches, which may be empty."""
    empty = Tree(None)
    empty.is_empty = True

    def __init__(self, entry, left=empty, right=empty):
        for branch in (left, right):
            assert isinstance(branch, BinaryTree) or branch.is_empty
        Tree.__init__(self, entry, (left, right))
        self.is_empty = False

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def __repr__(self):
        if self.left.is_empty and self.right.is_empty:
            return 'Bin({0})'.format(self.entry)
        elif self.right.is_empty:
            return 'Bin({0}, {1})'.format(self.entry, self.left)
        else:
            left = 'Bin.empty' if self.left.is_empty else repr(self.left)
            return 'Bin({0}, {1}, {2})'.format(self.entry, left, self.right)

    def is_leaf(self):
        return self.left.is_empty and self.right.is_empty

Bin = BinaryTree
