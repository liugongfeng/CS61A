class Link:
	empty = ()
	def __init__(self, first, rest=empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest

"""Write a function skip, which takes in a Link and 
returns a new Link with every other element skipped."""

def skip(lst):
	"""
	>>> a = Link(1, Link(2, Link(3, Link(4))))
	>>> a
	Link(1, Link(2, Link(3, Link(4))))
	>>> b = skip(a)
	>>> b
	Link(1, Link(3))
	>>> a
	Link(1, Link(2, Link(3, Link(4))))   # Original is unchanged
	"""
	if lst is Link.empty:
		return Link.empty
	elif lst.rest is Link.empty	:
		return Link(lst.first)
	return Link(lst.first, skip(lst.rest.rest))


"""Now write function skip by mutating the original list, 
instead of returning a new list. Do NOT call the Link constructor. """
def skip(lst):
	"""
	>>> a = Link(1, Link(2, Link(3, Link(4))))
	>>> b = skip(a)
	>>> b
	None
	>>> a
	Link(1, Link(3))
	"""
	if lst is Link.empty or lst.rest is Link.empty:
		return lst
	lst.rest = lst.rest.rest
	skip(lst.rest)




"""Write a function reverse, which takes in a Link and 
returns a new Link that has the order of the contents reversed.
Hint: You may want to use a helper function if 
you’re solving this recursively.
"""
def reverse(lst):
	"""
	>>> a = Link(1, Link(2, Link(3)))
	>>> b = reverse(a)
	>>> b
	Link(3, Link(2, Link(1)))
	>>> a
	Link(1, Link(2, Link(3)))
	"""
	result = Link.empty
	while lst is not Link.empty:
		result = Link(lst.first, result)
		lst = lst.rest
	return result







class Tree:
	def __init__(self, label, branches=[]):
		self.label = label
		self.branches = branches
	def is_leaf(self):
		return not self.branches


"""Write a function that returns true only if there exists 
a path from root to leaf that contains at least 
n instances of elem in a tree t."""

def contains_n(elem, n, t):
	"""
	>>> t1 = Tree(1, [Tree(1, [Tree(2)])])
	>>> contains(1, 2, t1)
	True
	>>> contains(2, 2, t1)
	False
	>>> contains(2, 1, t1)
	True
	>>> t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
	>>> contains(1, 3, t2)
	True
	>>> contains(2, 2, t2)		# Not on a path
	False
	"""
	if n == 0:
		return True
	elif t.is_leaf():
		return n == 1 and t.label == elem
	elif t.label == elem:
		return True in [contains_n(elem, n-1, b) for b in t.branches]
	else:
		return True in [contains_n(elem, n, b) for b in t.branches]





"""Define the function factor_tree which returns a factor tree. 
Recall that in a factor tree, multiplying the leaves together is
the prime factorization of the root, n. See below for an example of 
a factor tree for n = 20. 
		20
	   /  \
	  2    10
	      /  \
	     2    5
"""
def factor_tree(n):
	for i in range(2, n):
		if n % i == 0:
			return Tree(n, [factor_tree(i), factor_tree(n // i)])
	return Tree(n)


