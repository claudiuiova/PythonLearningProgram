"""
P1. Given a dictionary, swap keys <-> values. The program should use some custom logic to check if 
the swap is possible, but without using try..except constructs or the __hash__() function. Example:

Input: {'a': 123, 'b': 456}
Output: {123: 'a', 456: 'b'}
------------------------------------------------
Input: {'a': (1, 2, [3])}
Output: Swap is not possible

"""

class Swap:

	def __init__(self):
		
		self.swapKeyValue = {}
		self.errorOutput = 'swap was not possible for key-value: '
		self.flag = True

	def checkTuple(self, tupleToCheck):
		for tup in tupleToCheck:
			if isinstance(tup, tuple):
				self.checkTuple(tup)
			else:
				if not isinstance(tup, str) or not isinstance(tup, int):
					self.flag = False
					return self.flag
		return self.flag


	def changeKeyValue(self, listWithDicts):
		for _dict in listWithDicts:
			for k,v in _dict.items():
				if isinstance(v, tuple):
					if self.checkTuple(v):
						self.swapKeyValue.update({v: k})
					else:
						self.swapKeyValue.update({k: v})
						self.errorOutput += "%s: %s "%(str(k), str(v))

				elif isinstance(v, str) or isinstance(v, int):
					self.swapKeyValue.update({v: k})
				
				else:
					self.swapKeyValue.update({k: v})
					self.errorOutput += "%s: %s "%(str(k), str(v))

			print("Input: %s" %_dict)

			if self.flag:
				print("Output: %s" % self.swapKeyValue)
			else:
				print("Output: %s - %s" % (self.swapKeyValue, self.errorOutput))
				self.flag = True

			print ("----------------------------")
			self.errorOutput = 'swap was not possible for key-value: '
			self.swapKeyValue = {}

if __name__ == "__main__":
	listWithDicts = [{'a':2, 'b':3}, {'h': 98, 'a': (1, 2, [3]), 'z': 87}, 
	{'g': 5, 'nm': 18}, {'k': 12, 'kl': (9, 45, [8])}]
	swapObj = Swap()
	swapObj.changeKeyValue(listWithDicts)