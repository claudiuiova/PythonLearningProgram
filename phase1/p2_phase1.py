"""
P2. Merge 2 objects with any depth (including contained dictionaries, lists, sets, strings, integers, floats). Type mismatches should yield a tuple with the two elements. Examples:
a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}
Expected result:
{'x': [1,2,3,4,5,6], 'y': 5, 'z': set([1,2,3,4]), 'w': 'qweqweasdf', 't': {'a': [1, 2, 3, 2]}, 'm': ([1], "wer")}

"""

dict1 = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
dict2 = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf',   't': {'a': [3, 2]}, 'm': "wer"}


def mergeObjects(dict1, dict2):
	for key in dict1.keys():
		try:
			if isinstance(dict1[key], set):
				dict1[key] = dict1[key].union(dict2[key])
			elif isinstance(dict1[key], dict):
				mergeObjects(dict1[key], dict2[key])
			else:
				dict1[key] = dict1[key] + dict2[key]
		except TypeError as e:
			dict1[key] = (dict1[key], dict2[key])

mergeObjects(dict1, dict2)
print(dict1) 