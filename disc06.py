def fib_iter(n):
	prev, curr, i = 0, 1, 1
	while i < n:
		prev, curr = curr, prev + curr
		i += 1
	return prev


def fib_recursive(n):
	if n  == 0 or n == 1:
		return n
	else:
		return fib_recursive(n - 1) + fib_recursive(n - 2)


import compo
"""Write a function that takes in a a linked list and returns the sum of all its elements.
You may assume all elements in lnk are integers. """
def sum_nums(lnk):
	"""
	>>> a = Link(1, Link(6, Link(7)))
	>>> sum_nums(a)
	14
	"""
	if lnk is Link.empty:
		return 0
	return lnk.first + sum_nums(lnk.rest)





def sum_of_factorial(n):
	if n == 0:
		return 1
	else:
		return factorial(n) + sum_of_factorial(n - 1)


def bonk(n):
	total = 0
	while n >= 2:
		total += n
		n = n / 2
	return total



def mod_7(n):
	if n % 7 == 0:
		return 0
	else:
		return 1 + mod_7(n - 1)




def bar(n):
	if n % 2 == 1:
		return n + 1
	return n

def foo(n):
	if n < 1:
		return 2
	if n % 2 == 0:
		return foo(n - 1) + foo(n - 2)
	else:
		return 1 + foo(n - 2)

""" What is the order of growth of foo(bar(n))?"""



import compo

def multiply_lnks(lst_of_lnks):
	"""
	>>> a = Link(2, Link(3, Link(5)))
	>>> b = Link(6, Link(4, Link(2)))
	>>> c = Link(4, Link(1, Link(0, Link(2))))
	>>> p = multiply_lnks([a, b, c])
	>>> p.first
	48
	>>> p.rest.first
	12
	>>> p.rest.rest.rest
	()
	"""
	product = 1
	for lnk in lst_of_lnks:
		if lnk is Link.empty:
			return Link.empty
		product *= lnk.first
	lst_of_lnk_rests = [lnk.rest for lnk in lst_of_lnks]
	return Link(product, multiply_lnks(lst_of_lnk_rests))




"""Write a function that takes a SORTED linked list of integers and mutates it so that
all duplicates are removed."""
def remove_duplicates(lnk):
	"""
	>>> lnk = Link(1, Link(1, Link(1, Link(5))))
	>>> unique = remove_duplicates(lnk)
	>>> unique
	Link(1, Link(5))
	>>> lnk
	Link(1, Link(5))
	"""
	if lnk is Link.empty or lnk.rest is Link.empty:
		return lnk
	elif lnk.first == lnk.rest.first:
		lnk.rest = lnk.rest.rest
		remove_duplicates(lnk)
		return lnk
	else:
		remove_duplicates(lnk.rest)
		return lnk




"""Write a function that takes a list and returns a new list that keeps only the even-indexed
elements of lst and multiplies them by their corresponding index."""
def even_weighted(lst):
	"""
	>>> x = [1, 2, 3, 4, 5, 6]
	>>> even_weighted(x)
	[0, 6, 20]
	"""
	return [ lst[i] * i for i in range(0, len(lst), 2) ]




"""QuickSort"""
def quickSort_list(lst):
	if len(lst)<2:
		return lst
	pivot = lst[0]
	less = [ ele for ele in lst[1:] if ele <= pivot ]
	greater = [ele for ele in lst[1:] if ele > pivot]
	return quickSort_list(less) + [pivot] + quickSort_list(greater)

	

"""Write a function that takes in a list and returns the maximum product that can be
formed using nonconsecutive elements of the list. The input list will contain only
numbers greater than or equal to 1. """
from operator import mul
from functools import reduce

def max_product(lst):
	"""Return the maximum product that can be formed using lst
without using any consecutive numbers.

	>>> max_product([10,3,1,9,2]) 	# 10 * 9
	90
	>>> max_product([5,10,5,10,5])  # 5 * 5 * 5
	125
	>>> max_product([])
	1
	"""
	if len(lst) == 0:
		return 1
	result = 0
	splited = [lst[i::j] for i in range(len(lst)) for j in range(2,len(lst)) ]
	for ele in splited:
		temp = reduce(mul, ele)
		if result < temp:
			result = temp
	return temp





"""An expression tree is a tree that contains a function for each non-leaf node,
which can be either ’+’ or ’*’. All leaves are numbers. Implement eval_tree,
which evaluates an expression tree to its value. You may want to use the functions
sum and prod, which take a list of numbers and compute the sum and product
respectively."""
def eval_tree(tree):
	"""Evaluates an expression tree with functions the root.
	>>> eval_tree(tree(1))
	1
	>>> expr = tree('*', [tree(2), tree(3)])
	>>> eval_tree(expr)
	6
	>>> eval_tree(tree('+', [expr, tree(4), tree(5)]))
	15
	"""
	if is_leaf(tree):
		return label[tree]
	args = [eval_tree(b) for b in branches(tree)]
	if label[tree] == '+':
		return sum(args)
	else:
		return prod(args)

def prod(iter):
	from functools import reduce
	from operator import mul
	return reduce(mul, iter, 1)

