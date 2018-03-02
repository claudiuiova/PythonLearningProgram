"""
P3. Given a file containing a list of dictionaries implement a sorting algorithm (of your choosing) that will 
sort the list based on the dictionary keys. The dictionary keys will contain alphabetic characters while the 
values will be integers. The rule for comparing dictionaries between them is:
	- if the value of the dictionary with the lowest alphabetic key is lower than the value of the other 
	dictionary with the lowest alphabetic key, then the first dictionary is smaller than the second.
	- if the two values specified in the previous rule are equal reapply the algorithm ignoring the current key. 

The input is a file containing the list of dictionaries. Each dictionary key value is specified on the same 
line in the form <key> <whitespace> <value>. Each list item is split by an empty row. The output is a file 
containing a list of integers specifying the dictionary list in sorted order. Each integer identifies a dictionary 
in the order they were received in the input file.

"""

from collections import OrderedDict

class SortDicts:

	def __init__(self):
		self.flag = True
		self.key = 0

	def openFileAndGetTheInput(self):
		with open("input_dict.txt") as dictFile:
			return dictFile.read().split('\n')

	def createListWithLists(self):
		inputs = self.openFileAndGetTheInput()
		result = []
		tempList = []

		for item in inputs:
			if item == '':
				result.append(tempList)
				tempList = []
			else:
				tempList.append(item)

		result.append(tempList)
		return result

	def createListWithDictionaries(self):
		inputs = self.createListWithLists()
		dictList = []

		for i in range(len(inputs)):
			tempList = [{}]

			for item in inputs[i]:
				item = item.split()
				tempList[0].update({item[0]: int(item[1])})
			
			dictList.append({i+1: tempList[0]})
		return dictList

	def sortDictionaryByKey(self, dictionary):
		return dict(OrderedDict(sorted(dictionary.items())))


	def sortAllDictionariesKeys(self):
		sortedDicts = []
		for dictionary in self.createListWithDictionaries():
			for k,v in dictionary.items():
				v = self.sortDictionaryByKey(v)
				dictionary[k] = v
				sortedDicts.append(dictionary)
		return sortedDicts

	def getValueFromDictionary(self, index, listWithDicts, key=0):
		return listWithDicts[index][list(listWithDicts[index].keys())[0]][list(listWithDicts[index]
			[list(listWithDicts[index].keys())[0]].keys())[key]]

	def sortListWithDicts(self, listWithDicts):
		for i in range(len(listWithDicts) - 1, 0, -1):
			for j in range(i):
				if self.getValueFromDictionary(j, listWithDicts) > self.getValueFromDictionary(j+1, listWithDicts):
					temp = listWithDicts[j]
					listWithDicts[j] = listWithDicts[j+1]
					listWithDicts[j+1] = temp

				elif self.getValueFromDictionary(j, listWithDicts) == self.getValueFromDictionary(j+1, listWithDicts):
					while self.flag:
						self.key += 1
						if self.getValueFromDictionary(j, listWithDicts, key=self.key) > self.getValueFromDictionary(j+1, listWithDicts, key=self.key):
							temp = listWithDicts[j]
							listWithDicts[j] = listWithDicts[j+1]
							listWithDicts[j+1] = temp
							self.flag = False

						if self.key == len(self.createListWithLists()[j])-1: #check also if the dictionaries are fully equal.
							#if values are equal, the sorting algorithm will put the dictionaries how was inserted in the input file
							break

				self.flag = True
				self.key = 0

		return listWithDicts

	def writeFile(self):
		sortedList = self.sortListWithDicts(self.sortAllDictionariesKeys())
		result = ''
		for dict_ in sortedList:
			result += "%s " %list(dict_.keys())[0]
		with open("output_dict.txt", "w") as resultFile:
			resultFile.write(str(result))

if __name__ == '__main__':
	sortObj = SortDicts()
	sortObj.writeFile()