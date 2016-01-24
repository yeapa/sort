from show import showList
import copy
import numpy as np


def exchange(aList, a, b):
    aList[a], aList[b] = aList[b], aList[a]
    pass


def insertSort(aList):
    display_temp = []
    for i in xrange(1, len(aList)):
        for j in xrange(i, 0, -1):
            if aList[j] < aList[j - 1]:
                exchange(aList, j, j - 1)
        display_temp.append(copy.copy(aList))
    showList(display_temp)
    return aList


def selectSort(aList):
    display_temp = []
    for i in xrange(0, len(aList)):
        min = aList[i]
        for j in xrange(i + 1, len(aList)):
            if min > aList[j]:
                min = aList[j]
        aList[i] = min
        display_temp.append(copy.copy(aList))
    showList(display_temp)
def shellSort(aList):

    pass

if __name__ == "__main__":
    aList = np.random.randint(1, 50, 10)
    sortedList = selectSort(aList)
    print sortedList
