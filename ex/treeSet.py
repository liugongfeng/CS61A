from classTree import *

class BTree(Tree):
	empty = Tree(None)

	def __init__(self, label, left=empty, right=empty):
		for b in (left, right):
			assert isinstance(b, BTree) or b is BTree.empty
		Tree.__init__(self, label, (left, right))


	@property
	def left(self):
		return self.branches[0]

	@property
	def right(self):
		return self.branches[1]

	def is_leaf(self):
		return [self.left, self.right] == [BTree.empty] * 2


	def __repr__(self):
		if self.is_leaf():
			return 'BTree({0})'.format(self.label)
		elif self.right is BTree.empty:
			left = repr(self.left)
			return 'BTree({0}, {1})'.format(self.label, left)
		else:
			left, right = repr(self.left), repr(self.right)
			if self.left is BTree.empty:
				left = 'BTree.empty'
			template = 'BTree({0}, {1}, {2})'
			return template.format(self.label, left, right)


def fib_BTree(n):
	"""A fibonacci binary tree"""
	if n == 0 or n == 1:
		return BTree(n)
	else:
		left = fib_BTree(n - 2)
		right = fib_BTree(n - 1)
		fib_n = left.label + right.label
		return BTree(fib_n, left, right)


def contents(t):
	if t is BTree.empty:
		return []
	else:
		return contents(t.left) + [t.label] + contents(t.right)


def balanced_bst(s):
	"""Construct a binary search tree from a sorted list"""
	if not s:
		return BTree.empty
	mid = len(s) // 2
	left = balanced_bst(s[:mid])
	right = balanced_bst(s[mid+1:])
	return BTree(s[mid], left, right)



"""What's the largest element in a binary search tree?"""
def largest(t):
	if t.right is BTree.empty:
		return t.label
	else:
		return largest(t.right)


"""What's the second largest element in a binary search tree?"""
def second(t):
	if t.is_leaf():
		return None
	elif t.right is BTree.empty:
		return largest(t.left)
	elif t.right.is_leaf():
		return t.label
	else:
		return second(t.right)


def contains(s, v):
	if s is BTree.empty:
		reutrn False
	elif s.root == v:
		return True
	elif s.root < v:
		return contains(s.right, v)
	else:
		return contains(s.left, v)



def adjoin(s, v):
	if s is BTree.empty:
		return BTree(v)
	elif s.root == v:
		return s
	elif s.root < v:
		return BTree(s.root, s.left, adjoin(s.right, v))
	elif s.root > v:
		return BTree(s.root, adjoin(s.left, v), s.right)




t = BTree(3, BTree(1), 
			 BTree(7, BTree(5),
			 		  BTree(9, BTree.empty,
			 		  		   BTree(11))))
