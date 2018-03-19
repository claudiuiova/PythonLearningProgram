"""
P1. Given a binary tree encoded as a tuple (node_label, left_node_tuple, right_node_tuple) 
write an iterator / generator that returns the nodes of the tree in pre-order.
Example:
Input: ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))
Output: b, a, z, c, zz

"""

def get_left_child(parent):
    return parent[1]

def get_right_child(parent):
    return parent[2]

def get_root_val(tree):
    return tree[0]

def traverse_in_preorder(tree):
    if tree:
        yield get_root_val(tree)
        yield from traverse_in_preorder(get_left_child(tree))
        yield from traverse_in_preorder(get_right_child(tree))

if __name__ == '__main__':
    tree = ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))
    for node in traverse_in_preorder(tree):
        print(node)

