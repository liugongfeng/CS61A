#Question 2.1
"""
Write a function that takes two numbers m and n and returns their product.
Assume m and n are positive integers. Use recursion, not mul or *!

Hint: 5*3 = 5 + 5*2 = 5 + 5 + 5*1
"""

def multiply(m, n):
    if n==1:
        return m
    else:
        return m + multiply(m, n-1)




###Question 2.2
"""
Write a recursive function that takes in an integer n and prints out a countdown
from n to 1.
"""
def countdown(n):
    """
    >>> countdown(3)
    3
    2
    1
    """
    if n==0:
        return 0
    print(n)
    countdown(n-1)


###Question 2.3
    """
    How can we change countdown to count up
    instead without modifying a lot of the code?
    """
def countUp(n):
    if n==0:
        return 0
    countUp(n-1)
    print(n)
        


### Question 2.4
"""
Write a recursive function that takes a number n and returns the sum of its
digits. Assume n is positive.
"""
def sum_digits(n):
    """
    >>> sum_digits(7)
    7
    >>> sum_digits(30)
    3
    >>> sum_digits(228)
    12
    """
    if n<=0:
        return 0
    return sum_digits(n//10) + n%10



### Question 3.1
"""I want to go up a flight of stairs that has n steps.
I can either take 1 or 2 steps each time.
How many different ways can I go up this flight of stairs?
Write a function count_stair_ways that solves this problem for me.
Assume n is positive.
"""
def count_stair_ways(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)



### Question 3.2
    """
Consider a special version of the count_stairways problem,
where instead of taking 1 or 2 steps, we are able to take up to and
including k steps at a time.
    """
def count_k(n, k):
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        total,i = 0, 1
        while i<=k:
            total += count_k(n-i,k)
            i += 1
    return total


















    
