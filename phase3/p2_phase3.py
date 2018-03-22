"""
P2. Write a generator that returns all the subsets of a given set. 
Example:
Input: set([1, 2, 3])
Output: set([1, 2, 3]), set([2, 3]), set([1, 3]), set([3]), 
        set([1, 2]), set([2]), set([1]), set([])
"""

import itertools

def find_subsets(_sets, r):
    for i in range(r):
        subsets = itertools.combinations(_sets, i) #return subsets as tuples
        for s in subsets:
            s = set(s) #optional
            yield s

my_set = set([1,2,3])
for i in find_subsets(set([1,2,3]), len(my_set) + 1):
    print (i)
