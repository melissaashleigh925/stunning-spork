# 12/7/2016
# Python 3.4
# Program tests all functions from myFunction.py

import myFunction

aList = [1,2,3]
key = 2
test1 = 10
test2 = -15


print("The sum of aList is: ", myFunction.sumthing(aList))
print("The average of a List is: ", myFunction.average(aList))
print("The smallest in aList is: ", myFunction.smallest(aList))
print("The largest in a List is: ", myFunction.largest(aList))
print("The absolute value in a List is: ", myFunction.absolute(test2))
print("Is the value even: ", myFunction.isEven(test1))
print("Is the value is Odd: ", myFunction.isEven(test2))
print("If the key 2 is in list will return True: ", myFunction.find(key,aList))

'''
The sum of aList is:  6
The average of a List is:  2.0
The smallest in aList is:  1
The largest in a List is:  3
The absolute value in a List is:  15
Is the value even:  True
Is the value is Odd:  False
If the key 2 is in list will return True:  True
'''	
