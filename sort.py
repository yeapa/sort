
def exchange(aList,a,b):
    aList[a],aList[b]=aList[b],aList[a]
    pass

def insertSort(aList): 
    for i in xrange(1, len(aList)):
        for j in xrange(i,0,-1):
            if aList[j] < aList[j-1]:
                exchange(aList,j, j-1)

    return aList

aList = [1, 5, 3, 2]
sortedList = insertSort(aList)
print sortedList