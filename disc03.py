def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_leaf(tree):
    return not branches(tree)


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


# Question 3.1
""" Write a function that returns the largest number in a tree"""


def tree_max(t):
    """Return the max of a tree"""
    return max([label(t)] + [tree_max(b) for b in branches(t)])


# Question 3.2
"""Write a function that returns the height of a tree. Recall that the height of
a tree is the length of the longest path from the root to a leaf"""


def height(t):
    if is_leaf(t):
        return 0
    return 1 + max([height(b) for b in branches(t)])


# Question 3.3
""" Write a function that takes in a tree and squares every value. It should
return a new tree. You can assume that every item is a number. """


def square_tree(t):
    """Return a tree with the square of every element in t"""
    sq_branches = [square_tree(b) for b in branches(t)]
    return tree(label(t)**2, sq_branches)


# Question 3.4
"""Write a function that takes in a tree and a value x and returns a list containing
the nodes along the path required to get from the root of the tree to
a node containing x """


def find_path(tree, x):
    """
    >>> find_path(t, 5)
    [2,7,6,5]
    >>> find_path(t, 10)  # returns None
    """
    if label(tree) == x:
        return [label(tree)]

    for b in branches(tree):
        # to loop till find x ,  paths is None otherwise
        paths = find_path(b, x)
        if paths:
            return [label(tree)] + paths


def prune(t, k):
    if k==0:
        return tree(label(t), [])     # we don't need branches of t anymore
    else:
    	return tree(label(t), [prune(b, k-1) for b in branches(t)])



"""
t = [1, [3, [4], [5], [6]], [2]]

tt = [2, [7, [3], [6, [5], [11]]], [15]]
"""
