class Link:

	empty = ()

	def __init__(self, first, rest = empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest

	def __getitem__(self, i):
		if i == 0:
			return self.first
		else:
			return self.rest[i-1]

	def __len__(self):
		return 1 + len(self.rest)


	def __repr__(self):
		if self.rest is Link.empty:
			rest = ''
		else:
			rest = ', ' + repr(self.rest)
		return 'Link({0}{1})'.format(self.first, rest)

	def __str__(self):
		string = '<'
		while self.rest is not Link.empty:
			string += str(self.first) + ' '
			self = self.rest
		return string + str(self.first) + '>'





	@property
	def second(self):
		return self.rest.first

	@second.setter
	def second(self, value):
		self.rest.first = value





def empty(s):
	return s is Link.empty

def set_contain(s, v):
	"""Return True if and only if set s contains v."""
	if empty(s):
		return False
	elif s.first == v:
		return True
	else:
		return set_contain(s.rest, v)

"""
>>> s = Link(4, Link(1, Link(5)))
>>> set_contain(s, 2)
False
>>> set_contain(s, 5)
True
"""


"""Θ(n) tine"""
def adjoin_set(s, v):
	"""Return a set containing all elements of s and element v. """
	if set_contain(s, v):
		return s
	else:
		return Link(v, s)
"""
>>> t = adjoin_set(s, 2)
>>> t
Link(2, Link(4, Link(1, Link(5))))
"""



def contains(s, v):
	"""Return true if set s contains value v as an element.

	>>> s = Link(1, Link(3, Link(5)))
	>>> contains(s, 2)
	False
	>>> contains(s, 5)
	True
	"""
	if empty(s) or s.first > v:
		return False
	elif s.first == v:
		return True
	else:
		return contains(s.rest, v)



def adjoin(s, v):
	if empty(s) or v < s.first:
		return Link(v, s)
	elif v == s.first:
		return s
	else:
		return Link(s.first, adjoin(s.rest, v))



def intersect(set1, set2):
	if empty(set1) or empty(set2):
		return Link.empty
	else:
		e1, e2 = set1.first, set2.first
		if e1 == e2:
			return Link(e1, intersect(set1.rest, set2.rest))
		elif e1 < e2:
			return intersect(set1.rest, set2)
		else:	# e1 > e2
			return intersect(set1, set2.rest)



def union(set1, set2):
	if empty(set1):
		return set2
	elif empty(set2):
		return set1
	else:
		e1, e2 = set1.first, set2.first
		if e1 == e2:
			return Link(e1, union(set1.rest, set2.rest))
		elif e1 < e2:
			return Link(e1, union(set1.rest, set2))
		else: 	# e1 > e2
			return Link(e2, union(set1, set2.rest))



def add(s, v):
	""" Add v to a set s and return s.
	>>> s = Link(1, Link(3, Link(5)))
	>>> add(s, 0)
	Link(0, Link(1, Link(3, Link(5))))
	>>> add(s, 3)
	Link(0, Link(1, Link(3, Link(5))))
	>>> add(s, 4)
	Link(0, Link(1, Link(3, Lin(4, Link(5)))))
	>>> add(s, 6)
	Link(0, Link(1, Link(3, Lin(4, Link(5, Link(6))))))
	"""
	assert not empty(s), 'Cannot add to an empty set.'
	if s.first > v:
		s.first, s.rest = v, Link(s.first, s.rest)
	elif s.first < v and empty(s.rest):
		s.rest = Link(v, s.rest)
	elif s.first < v:
		add(s.rest, v)
	return s
