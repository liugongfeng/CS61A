### Question 1
"""
Implement the longest_increasing_suffix function, which returns
the longest suffix (end) of a positive integer that
consists of strictly increasing digits.

"""
def longest_increasing_suffix(n):
    """Return the longest increasing suffix of a positive
     integer n.
     >>> longest_increasing_suffix(63134)
     134
     >>> longest_increasing_suffix(233)
     3
     >>> longest_increasing_suffix(5689)
     5689
     >>> longest_increasing_suffix(568901)  # Note: 01 is the suffix, displayed as 1
     1
     """
    m, suffix, k = 10, 0, 1
    while n:
        n, last = n//10, n%10
        if last < m:
            m, suffix, k = last, suffix+k*last, k*10
        else:
            return suffix
    return suffix




### Question 2
"""
A number n contains a sandwichif a digit in n is
surrounded by two identical digits.
For example, the number 242 contains a sandwich because
4 is surrounded by 2 on both sides.
1242 also contains a sandwich, while 12532 does not contain a sandwich
"""
def sandwich(n):
    """Return True if n contains a sandwich and False otherwise
    >>> sandwich(416263)   # 626
    True
    >>> sandwich(5050)
    True
    >>> sandwich(4441)     #444
    True
    >>> sandwich(1231)
    False
    >>> sandwich(55)
    False
    >>> sandwich(4456)
    False

"""
    ten, one = (n//10)%10, n%10
    n = n//100
    while n:
        if n%10==one:
            return True
        else:
            ten, one = n%10, ten
            n = n//10
    return False




### Question 3
"""
The Luhn sum of a non-negative integer n adds the sum of
each digit in an even position to the sum of doubling each digit in an odd position.
If doubling an odd digit results in a two-digit number,
those two digits are summed to form a single digit.

"""
def luhn_sum(n):
    """Return the Luhn sum of n.
    >>> luhn_sum(135)     # 1 + 6 + 5
    12
    >>> luhn_sum(185)     # 1 + (1+6) + 5
    13
    >>> luhn_sum(138743)  # 2+3+(1+6)+7+8+3
    30
    """
    def luhn_digit(digit):
        x = digit * multiplier
        return (x//10) + x%10

    total, multiplier = 0, 1
    while n:
        n, last = n//10, n%10
        total = total + luhn_digit(last)
        multiplier = 3 - multiplier
    return total

















