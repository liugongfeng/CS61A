HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(a)-street(b)) + abs(avenue(a)-avenue(b))

from math import sqrt
def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    l = []
    for i in s:
        j = round(sqrt(i))
        if j*j == i:
            l.append(j)
    return l



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
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<=3:
        return n
    else:
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
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<=3:
        return n
    """We could calculate from margin number,g(4), g(5),g(6)...g(n)"""
    p1, p2, p3 = 1, 2, 3
    i, current = 4,0
    while i<=n:
        current = p3 + 2*p2 + 3*p1
        p1, p2, p3 = p2, p3, current
        i+=1
    return current
    
    

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
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    """
    l=[1]
    flag = True     # True: Plus,    False: Minus
    while len(l)<n:
        if flag:
            l.append(l[-1]+1)
            if has_seven(len(l)) or len(l)%7==0:
                flag = not flag
        else:
            l.append(l[-1]-1)
            if has_seven(len(l)) or len(l)%7==0:
                flag = not flag     
    return l[n-1]
    """
    def pingpong_next(k, p, up):  # k: kth  p:pingpong num   up:flag
        if k==n:
            return p
        if up: #True: Plus   False: Minus
            return pingpong_change(k+1, p+1, up)
        else:
            return pingpong_change(k+1, p-1, up)
        
    def pingpong_change(k, p, up):
        if k%7==0 or has_seven(k):
            return pingpong_next(k, p, not up)
        else:
            return pingpong_next(k, p, up)
            
    return pingpong_next(1, 1, True)
            

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
    "*** YOUR CODE HERE ***"
    def count_partitions(min_coin, amount):
        if amount==0:
            return 1
        elif min_coin > amount:
            return 0
        else:
            with_min = count_partitions(min_coin, amount-min_coin)
            without_min = count_partitions(2*min_coin, amount)
            return with_min + without_min
        
    return count_partitions(1, amount)

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda k:f(f,k)) (lambda f, k: 1 if k==1 else mul(k, f(f,sub(k,1)) ))
    

