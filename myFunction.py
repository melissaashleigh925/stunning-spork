# 12/7/2016
# Python 3.4
# Program has listed functions that get called in testFunctions.

def smallest(myList):
    myMin = myList[0]
    for i in range(1,len( myList)):
        if myList[i] < myMin:
            myMin = myList[i]
    return myMin

def largest(myList):
    myMax = myList[0]
    for j in range(1,len(myList)):
        if myList[j] > myMax:
            myMax = myList[j]
    return myMax 

def average(myList):

    return sum(myList)/float(len(myList))

def sumthing(myList):
    total = 0
    for i in myList:
        total += i
    return total

def absolute(value):
    if value < 0:
        return - value
    return value

def isEven(N):

    if N % 2 == 0:
        return True
    else:
        return False
        
def find(key,myList):
	for i in myList:
		if i == key:
			return True
	return False

