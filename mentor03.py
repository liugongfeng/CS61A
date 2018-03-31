### Question 3
"""Given some list lst, possibly a deep list, mutate lst to have the accumulated sum of
all elements so far in the list. If there is a nested list, mutate it to similarly reflect the
accumulated sum of all elements so far in the nested list. Return the total sum of lst.
Hint: The isinstance function returns True for isinstance(l, list) if l is a
list and False otherwise """

def accumulate(lst):
	"""
	>>> l = [1, 5, 13, 4]
	>>> accumulate(l)
	23
	>>> l
	[1, 6, 19, 23]
	>>> deep_l = [3, 7, [2, 5, 6], 9]
	>>> accumulate(deep_l)
	32
	>>> deep_l
	[3, 10, [2, 7, 13], 32]
	"""
	sum_so_far = 0
	for i in range(len(lst)):
		item = lst[i]
		if isinstance(item, list):
			inside = accumulate(item)
			sum_so_far += inside
		else:
			sum_so_far += item
			lst[i] = sum_so_far
	return sum_so_far