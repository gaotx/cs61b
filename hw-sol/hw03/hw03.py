def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n in (1, 2, 3):
        return n
    return g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n == 1 or n == 2 or n == 3:
        return n
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c + 2*b + 3*a
        n = n - 1
    return c


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    def pingpong_next(k, p, up):
        if k == n:
            return p
        if up:
            return pingpong_switch(k+1, p+1, up)
        else:
            return pingpong_switch(k+1, p-1, up)

    def pingpong_switch(k, p, up):
        if k % 7 == 0 or has_seven(k):
            return pingpong_next(k, p, not up)
        else:
            return pingpong_next(k, p, up)

    return pingpong_next(1, 1, True)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    return count_using(1, amount)

def count_using(min_coin, amount):
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    elif min_coin > amount:
        return 0
    else:
        with_min = count_using(min_coin, amount - min_coin)
        without_min = count_using(2*min_coin, amount)
        return with_min + without_min


def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    if n == 1:
        print("Move the top disk from rod", start, "to rod", end)
    else:
        other = 6 - start - end
        towers_of_hanoi(n-1, start, other)
        towers_of_hanoi(1, start, end)
        towers_of_hanoi(n-1, other, end)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))
