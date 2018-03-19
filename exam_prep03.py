### Question 1

def sum_range(t):
"""Returns the range of the sums of t, that is, the
difference between the largest and the smallest
sums of t."""
	def helper(t):
		if is_leaf(t):
			return [label(t), label(t)]
		else:
			a = min([helper(b)[1] for b in branches(t)])
			b = max([helper(b)[0] for b in branches(t)])
			x = label(t)
			return [b + x,  a + x]
	x, y = helper(t)
	return x - y




### Question 2
"""Fill in the blanks of the implementation of no_eleven below, a function that returns
a list of all distinct length-n lists of ones and sixes in which 1 and 1 do not appear
consecutively. """

def no_eleven(n):
	"""Return a list of lists of 1's and 6's that do not
contain 1 after 1.

	>>> no_eleven(2)
	[[6, 6], [6, 1], [1, 6]]
	>>> no_eleven(3)
	[[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
	>>> no_eleven(4)[:4]
	[[6, 6, 6, 6], [6, 6, 6, 1], [6, 6, 1, 6], [6, 1, 6, 6]]
	>>> no_eleven(4)[4:] # second half
	[[6, 1, 6, 1], [1, 6, 6, 6], [1, 6, 6, 1], [1, 6, 1, 6]]
	"""

	if n == 0:
		return [[]]
	elif n == 1:
		return [[6], [1]]
	else:
		a, b = no_eleven(n-1) , no_eleven(n-2)
		return [[6] + s for s in a] + [[1, 6] + s for s in b]




def eval_with_add(t):
	"""Evaluate an expression tree of * and + using only addition.
	>>> plus = Tree('+', [Tree(2), Tree(3)])
	>>> eval_with_add(plus)
	5
	>>> times = Tree('*', [Tree(2), Tree(3)])
	>>> eval_with_add(times)
	60
	>>> eval_with_add(Tree('*'))
	1
	"""
	if label(t) == '+' :
		return sum([eval_with_add(b) for b in branches(t)])
	elif label(t) == '*' :
		total = 1
		for b in branches(t):
			term, total = total, 0
			for _ in range(eval_with_add(b)):
				total = total + term
		return total
	else:
		return label(t)


