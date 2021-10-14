# i want to print out a string n number of times
# and i want to call this function printNTimes()
# inputs: a string, an integer
# output: no output, just a print to console
def printNTimes(whatToPrint, howManyTimesToPrint):
  for i in range(0, howManyTimesToPrint ):
    print(whatToPrint)

printNTimes("hello jake", 10)
printNTimes("hello betina", 100)


# rationale: get the sum of a list
# input: a list
# output: sum of that list
def findSum(aListToSum):
  numSum = 0
  for x in aListToSum:
    numSum += x
  
  return numSum

result = findSum([3,4,5])
print(result)


