"""
P1. Implement a function that will flatten two lists up to a maximum given depth:
def flatten(list_a, list_b, max_depth)

"""

LIST1 = ['1a', '1aa', ['2a', ['3a', '3aa', ['4a', '4aa', ['5a']], '3aaa'], '2aa', ['3aaaa']], '1aaa']
LIST2 = ['1b', '1bb', ['2b', ['3b', '3bb', ['4b', '4bb', '4bbb'], '3bbb'], '2bb', ['3bbbb']], '1bbb']


class FlatList:
	def __init__(self):
		
		self.flattenList_ = []
		self.depth = 1
		self.flag = False

	def parseList(self, customList, maxDepth):
		for item in customList:
			if isinstance(item, list):
				if self.depth == maxDepth:
					self.flag = True
				
				self.depth += 1
				
				if self.flag:
					continue
				else:
					self.parseList(item, maxDepth)
			else:
				self.flattenList_.append(item)

	def flattenList(self, listA, listB, maxDepth):

		parsedListA = self.parseList(listA, maxDepth)
		self.depth = 1
		self.flag = False
		parsedListB = self.parseList(listB, maxDepth)


if __name__ == '__main__':
	listObj = FlatList()
	listObj.flattenList(LIST1, LIST2, 2)
	print(listObj.flattenList_)