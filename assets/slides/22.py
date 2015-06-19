# Cycles

def cycle_demo():
    """A linked list can contain cycles.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first = 5
    >>> t = s.rest
    >>> t.rest = s
    >>> s.first
    5
    >>> s.rest.rest.rest.rest.rest.first
    2
    """

# Bear Environment

def oski(bear):
    """Oski the bear.

    >>> oski(abs)
    [2, [3, 1]]
    """
    def cal(berk):
        nonlocal bear
        if bear(berk) == 0:
            return [berk+1, berk-1]
        bear = lambda ley: berk-ley
        return [berk, cal(berk)]
    return cal(2)

# Work

class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'My job is to gather wealth'

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

def work():
    """Working.

    >>> Worker().work()
    'Sir, I work'
    >>> jack
    Peon
    >>> jack.work()
    'Maam, I work'
    >>> john.work()
    Peon, I work
    'My job is to gather wealth'
    >>> john.elf.work(john)
    'Peon, I work'
    """

# Morse tree

abcde = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.'}

def ensure(tree, k):
    """Ensure that branch k of tree is not empty and return it."""
    if tree.branches[k] is BinaryTree.empty:
        tree.branches[k] = BinaryTree(' ')
    return tree.branches[k]

def morse(code):
    """Return a binary tree representing the code. Left is . & right is -

    >>> morse(abcde).left # Starts with .
    Bin(e, Bin.empty, Bin(a))
    >>> morse(abcde).right.left # Starts with -.
    Bin( , Bin(d, Bin(b)), Bin( , Bin(c)))
    """
    root = BinaryTree(' ')
    for letter, signals in abcde.items():
        branch = root
        for signal in signals:
            if signal == '.':
                branch = ensure(branch, 0)
            elif signal == '-':
                branch = ensure(branch, 1)
        branch.entry = letter
    return root

def decode(signals, tree):
    """Decode signals into a letter.

    >>> t = morse(abcde)
    >>> [decode(s, t) for s in ['-..', '.', '-.-.', '.-', '-..', '.']]
    ['d', 'e', 'c', 'a', 'd', 'e']
    """
    for signal in signals:
        if signal == '.':
            tree = tree.left
        elif signal == '-':
            tree = tree.right
    return tree.entry

# Link, Tree, and BinaryTree classes

class Link:
    """A linked list."""

    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)    

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

