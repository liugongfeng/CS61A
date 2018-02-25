### Question 0.1

def is_sorted(n):
    """
>>> is_sorted(2)
True
>>> is_sorted(22222)
True
>>> is_sorted(9876543210)
True
>>> is_sorted(9087654321)
False
"""
    flag = True
    n, last = n//10, n%10
    while n:
        if n%10<last:
            return False
        n, last = n//10, n%10
    return True



### Question 1
def mario_number(level):
    """ Return the number of ways that Mario can traverse the
level, where Mario can either hop by one digit or two
digits each turn. A level is defined as being an integer
with digits where a 1 is something Mario can step on and 0 is
something Mario cannot step on.
>>> mario_number(10101)
1
>>> mario_number(11101)
2
>>> mario_number(100101)
0
"""
    if level == 1:
        return 1
    elif level % 10 == 0:
        return 0
    else:
        return mario_number(level//10) + mario_number( (level//10)//10 )



### Quesion 2
def make_change(n):
    """ Write a function, make_change that takes in an
integer amount, n, and returns the minimum number
of coins we can use to make change for that n,
using 1-cent, 3-cent, and 4-cent coins.
Look at the doctests for more examples.
>>> make_change(5) # Not 1+1+3  but 1+4
2
>>> make_change(6) # tricky!  Not 4+1+1 but 3+3
2
"""
    if n<1:
        return 0
    elif n<3:
        return 1 + make_change(n-1)  # (return n) is also fine
    elif n<4:
        use_1 = 1 + make_change(n-1)
        use_3 = 1 + make_change(n-3)
        return min(use_1, use_3)
    else:
        use_1 = 1 + make_change(n-1)
        use_3 = 1 + make_change(n-3)
        use_4 = 1 + make_change(n-4)
        return min(use_1, use_3, use_4)
    



### Question 1   ADT
"""The following is an Abstract Data Type (ADT) for elephants. Each elephant keeps
track of its name, age, and whether or not it can fly. Given our provided constructor,
fill out the selectors:"""

def elephant(name, age, can_fly):
    """Takes in a string name, an int age, and a boolean can_fly.
Constructs an elephant with these attributes.
>>> dumbo = elephant("Dumbo", 10, True)
>>> elephant_name(dumbo)
"Dumbo"
>>> elephant_age(dumbo)
10
>>> elephant_can_fly(dumbo)
True
"""
    return [name, age, can_fly]


def elephant_name(e):
    return e[0]

def elephant_age(e):
    return e[1]

def elephant_can_fly(e):
    return e[2]




### Question 3
""" Fill out the following constructor for the given selectors."""
def elephant(name, age, can_fly):
    return [ [name, age], can_fly]

def elephant_name(e):
    return e[0][0]

def elephant_age(e):
    return e[0][1]

def elephant_can_fly(e):
    return e[1]



### Question 5
"""  Fill out the following constructor for the given selectors."""
def elephant(name, age, can_fly):
    """
>>> chris = elephant("Chris Martin", 38, False)
>>> elephant_name(chris)
'Chris Martin'
>>> elephant_age(chris)
38
>>> elephant_can_fly(chris)
False
"""
    def select(command):
        if command == "name":
            return name
        elif command == "age":
            return age
        elif command == "can_fly":
            return can_fly
        else:
            pass
    return select
    
def elephant_name(e):
    return e("name")

def elephant_age(e):
    return e("age")

def elephant_can_fly(e):
    return e("can_fly")
