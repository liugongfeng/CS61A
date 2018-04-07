"""7. Conserve Links (Challenge Linked List problem)
Implement conserve_links, as described below."""

"""Makes Linked List a share as many Link instances as possible
with Linked List b.a can use b's i-th Link instance as its i-th
Link instance if a and b have the same element at position i.
Should mutate a. b is allowed to be destroyed. Returns the new
first Link instance of a.
"""

def converse_links(a, b):
	if a.first == b.first:
		b.rest = converse_links(a.rest, b.rest)
		return b
	else:
		return a






"""Implement slice_reverse which takes
a linked list s and mutatively reverses the elements on the interval, 
[i, j) (including i but excluding j). Assume s is zero-indexed, 
i > 0, i < j, and that s has at least j elements."""
def slice_reverse(s, i, j):
	"""
	>>> s = Link(1, Link(2, Link(3)))
	>>> slice_reverse(s, 1, 2)
	>>> s
	Link(1, Link(2, Link(3)))
	>>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
	>>> slice_reverse(s, 2, 4)
	>>> s
	Link(1, Link(2, Link(4, Link(3, Link(5)))))
	"""
	begin = s 
	for _ in range(i - 1):
		begin = begin.rest 		# 3 4 5
	reverse = Link.empty
	current = begin.rest 		# 4 5
	for _ in range(j - i):		
		rest = current.rest 	# 5
		current.rest = reverse
		reverse = current
		current = rest

	### unfinished

