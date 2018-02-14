"""Write a higher-order function that passes the following doctests
 Changlenge: Write the function body in one line"""

def mystery(f, x):
    """
    >>> from operator import add, mul
    >>> a = mystery(add, 3)
    >>> a(4) # add(3, 4)
    7
    >>> a(12)
    15
    >>> b = mystery(mul, 5)
    >>> b(7) # mul(5, 7)
    35
    >>> b(1)
    5
    >>> c = mystery(lambda x, y: x * x + y, 4)
    >>> c(5)
    21
    >>> c(7)
    23
    """
    """
    def fn(y):
        return f(x,y)
    return fn
    """
    return lambda y:f(x,y)



def fox_says(start, middle, end, num):
    """
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """
    def repeat(k):
       if k==1:
           return middle
       else:
            return middle + '-' + repeat(k-1)

    return start + '-' + repeat(num) + '-' + end

from operator import add,mul
def combine(n, f, result):
    """
Combine the digits in non-negative integer n using f.
>>> combine(3, mul, 2) # mul(3, 2)
6
>>> combine(43, mul, 2) # mul(4, mul(3, 2))
24
>>> combine(6502, add, 3) # add(6, add(5, add(0, add(2, 3))) )
16
>>> combine(239, pow, 0) # pow(2, pow(3, pow(9, 0))))
8
"""
    if n==0:
        return result
    else:
        return combine(n//10, f, f(n%10, result) ) 





















    
