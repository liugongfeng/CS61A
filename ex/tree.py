def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch),'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree)!= list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n<=1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree( label(left)+label(right), [left, right] )


def print_tree(t, indent=0):
    print('  '*indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)


def count_leaves(t):
    """ Count the leaves of tree T."""
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])


def leaves(tree):
    """Return a list containing the leaf label of tree.
>>> leaves(fib_tree(5))
[1,0,1,0,1,1,0,1]
"""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)])


def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented"""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)


def increment(t):
    """Return a tree like t but with all labels incremented."""
    return tree(label(t)+1, [increment(b) for b in branches(t)])


def tree_max(t):
    return max([label(t)] + [tree_max(branch) for branch in branches(t)])


def find_path(tree, x):
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path

def height(tree):
    if is_leaf(tree):
        return 0
    return 1 + max([height(b) for b in branches(tree)])


#t = [2, [7, [3], [6, [5], [11]]], [15]]

t = [1, [3, [4], [5], [6]], [2]]












    
