def kbonacci(n, k):
    """ Return element N of a K-bonacci sequence
>>> kbonacci(3, 4)
1
>>> kbonacci(9,4)
29
>>> kbonacci(4,2)
3
>>> kbonacci(8,2)
21
"""
    if n < k-1:
        return 0
    elif n==k-1:
        return 1
    else:
        total = 0
        i = n - k
        while i<n:
            total = total + kbonacci(i, k)
            i += 1
        return total


### Question 2
def combine(left, right):
    factor = 1
    while factor <= right:
        factor = factor * 10
    return left * factor + right

def reverse(n):
    """Return the digits of N in reverse
>>> reverse(122543)
345221
"""
    if n<10:
        return n
    else:
        return combine(n%10, reverse(n//10))

def remove(n, digit):
    """Return all digits of N that are not DIGIT,
for DIGIT less than 10.
    >>> remove(243132,3)
    2412
    >>> remove(remove(2243132, 1), 2)
    433
    """
    removed = 0
    while n != 0:
        n, last = n//10, n%10
        if last != digit:
            removed = removed*10 + last
    return reverse(removed)



### Question 3
square = lambda x: x*x
double = lambda x: 2*x
def memory(x, f):
    """Return a higher-order function that prints its memories.
    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """
    def g(h):
        print(f(x))
        return memory(x, h)
    return g
    








        
