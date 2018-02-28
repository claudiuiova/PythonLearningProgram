def openFileAndGetTheInput():
	with open("input_dict.txt") as dictFile:
		return dictFile.read().split('\n')

def createListWithLists():
	inputs = openFileAndGetTheInput()
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

def createListWithDictionaries():
	inputs = createListWithLists()
	dictList = []

	for i in range(len(inputs)):
		tempList = [{}]

		for item in inputs[i]:
			item = item.split()
			tempList[0].update({item[0]: int(item[1])})
		
		dictList.append({i+1: tempList[0]})
	return dictList
			
def sortDictionaries():
	allDictionaries = createListWithDictionaries()

	for dictionary in allDictionaries:
		for k,v in dictionary.items():
			
			print(min(v, key=v.get))

			print('........')
			
			print(min(v))

#need work
sortDictionaries()