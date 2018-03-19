### Question 1.3
""" Write a function that takes in a value x and updates and prints the result
based on input functions"""

def memory(n):
	"""
	>>> f = memory(10)
	>>> f = f(lambda x: x*2)
	20
	>>> f = f(lambda x: x - 7)
	13
	>>> f = f(lambda x: x > 5)
	True
	"""
	def todo(func):
		nonlocal n
		n = func(n)
		print(n)
		return todo
	return todo 



### Question 2.2
"""Write a function that takes in a value x, a value el, and a list and adds as
many el’s to the end of the list as there are x’s. 
Make sure to modify the original list using list mutation techniques"""

def add_this_many(x, el, lst):
	"""Adds el to the end of lst the number of items x occurs in lst
	>>> lst = [1, 2, 4, 2, 1]
	>>> add_this_many(1, 5, lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5]
	>>> add_this_many(2, 2 , lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5, 2, 2]
	"""
	n = lst.count(x)
	for _ in range(n):
		lst.append(el)



### Question 2.3
"""Write a function that takes in a list and reverses it in place, i.e. mutate the
given list itself, instead of returning a new list. """

def reverse(lst):
	""" Reverse lst in place
	>>> x = [3, 2, 4, 5, 1]
	>>> reverse(x)
	>>> x
	[1, 5, 4, 2, 3]
	"""
	for i in range(len(lst)):
		lst.insert( i, lst.pop() )



### Question 3.2
"""Write a function that takes in a sequence s and a function fn and returns a
dictionary.
The values of the dictionary are lists of elements from s. Each element e in
a list should be constructed such that fn(e) is the same for all elements in
that list. Finally, the key for each value should be fn(e). """

def group_by(s, fn):
	"""
	>>> group_by([12, 23, 14, 45], lambda p: p//10)
	{1: [12, 14], 2: [23], 4: [45]}
	>>> group_by(range(-3, 4), lambda x: x*x)
	{0: [0], 1: [-1, 1], 4:[-2, 2], 9: [-3, 3]}
	"""
	if type(s) != list:
		s = list(s)
	d = {}
	for e in s:
		key = fn(e)
		if key in d:
			d[key].append(e)
		else:
			d[key] = [e]
	return d



### Question 3.3
"""Write a function that takes in a deep dictionary d and replace all occurences
of x as a value (not a key) with y.
Hint: You will need to combine iteration and recursion. Also, for a dictionary
z, type(z) == dict will evaluate to True"""

def replace_all_deep(d, x, y):
	"""
	>>> d = {1: {2:'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
	>>> replace_all_deep(d, 'x', 'y')
	>>> d
	{1: {2: 'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
	"""
	for key in d:
		if d[key] == x:
			d[key] == y
		elif type(d[key]) == dict:
			replace_all_deep(d[key], x, y)
