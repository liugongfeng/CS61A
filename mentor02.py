### Question 3
""" Write a function that takes in a list nums and returns a new list with only the primes
from nums. Assume that is_prime(n) is defined. You may use a while loop, a for
loop, or a list comprehension. """

def all_primes(nums):
	lst = [ele for ele in nums if is_prime(ele)]
	return lst


### Question 4
"""Write a function that takes in a list of positive integers and outputs a list of lists where
the i-th list contains the integers from 0 up to, but not including, the i-th element of
the input list."""

def list_of_lists(lst):
	"""
	>>> list_of_lists([1, 2, 3])
	[[0], [0, 1], [0, 1, 2]]

	>>> list_of_lists([1])
	[[0]]

	>>> list_of_lists([])
	[]
	"""
	if not lst:
		return []

	return [ list(range(ele)) for ele in lst ]



####################
#Things to remember#
####################
def tree(label, branches=[]):
	return [label] + [branches]

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]


### Question 1
t = tree(9, 
		[tree(2,[]), 
		 tree(4,
				[tree(1,[])]),
		 tree(4, 
		 		[tree(7,[]), 
		 		tree(3, [])])])

### Question 2

# 9
# [4, [7,3]]
# 7


### Question 3
#label(branches(t)[0])



### Question 4
""" Write the function sum_of_nodes which takes in a tree and outputs the sum of all
the elements in the tree."""

def sum_of_nodes(t):
	"""
	>>> sum_of_nodes(t)
	30
	"""
	total = label(t)
	for b in branches(t):
		total += sum_of_nodes(b)
	return total



