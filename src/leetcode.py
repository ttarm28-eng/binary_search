'''
All of the functions in this file are classic leetcode style interview questions.
They all take a container xs as input and run in time O(log n),
where n is the length of xs.

JOKE: There are 2 hard problems in computer science:
1. cache invalidation,
2. naming things, and
3. off-by-1 errors.

It's really easy to have off-by-1 errors in these problems.
Pay very close attention to your list indexes and your < vs <= operators.
'''


def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT:
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    first = 0
    last = len(xs) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if xs[midpoint] <= 0:
            first = midpoint + 1
        else:
            last = midpoint - 1
    if first == len(xs):
        return None
    return first


def find_largest_negative(xs, lo=0, hi=None):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the largest negative number.
    If no such index exists, return `None`.

    HINT:
    This is the mirror image of find_smallest_positive:
    both functions search for the boundary at 0,
    but they return different sides of that boundary.

    >>> find_largest_negative([-3, -2, -1, 0, 1, 2, 3])
    2
    >>> find_largest_negative([1, 2, 3]) is None
    True
    >>> find_largest_negative([-3, -2, -1])
    2
    '''
    first = 0
    last = len(xs) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if xs[midpoint] >= 0:
            last = midpoint - 1
        else:
            first = midpoint + 1
    if last < lo:
        return None
    return last


def find_smallest(xs, lo=0, hi=None):
    '''
    Assume that xs is a list of numbers that is strictly decreasing
    and then strictly increasing,
    so that xs has a unique smallest element.
    Return the index of that element, or `None` if xs is empty.

    NOTE:
    This is the discrete analogue of argmin in src/argmin.py:
    argmin minimizes a convex function over the reals,
    and find_smallest minimizes a list of numbers.

    >>> find_smallest([4, 3, 2, 1, 2, 3])
    3
    >>> find_smallest([1, 2, 3])
    0
    >>> find_smallest([3, 2, 1])
    2
    >>> find_smallest([]) is None
    True
    '''
    hi = len(xs) - 1
    if len(xs) == 0:
        return None
    first = lo
    last = hi
    while first <= last:
        midpoint = (first + last) // 2
        if midpoint < hi and xs[midpoint] > xs[midpoint + 1]:
            first = midpoint + 1
        else:
            last = midpoint -1
    return first


def _firstcount(xs, x):
    first = 0
    last = len(xs) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if xs[midpoint] > x:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return first


def _lastcount(xs, x):
    first = 0
    last = len(xs) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if xs[midpoint] >= x:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return first


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT:
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand-alone functions for steps 1 and 2,
    and write your own doctests for these functions.
    Then, once you're sure these functions work independently,
    completing step 3 will be easy.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    return _lastCount(xs, x) - _firstCount(xs, x)
