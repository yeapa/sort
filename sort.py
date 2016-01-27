from show import showList
import copy
import numpy as np


def exchange(aList, a, b):
    aList[a], aList[b] = aList[b], aList[a]
    pass


def exchange1(a, b):
    a, b = b, a


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
        index, min = i, aList[i]
        for j in xrange(i + 1, len(aList)):
            if min > aList[j]:
                index, min = j, aList[j]
        exchange(aList, i, index)
        display_temp.append(copy.copy(aList))
    showList(display_temp)
    return aList


def shellSort(aList):
    N = len(aList)
    h = 1
    display_temp = []
    while h < N / 3:
        h = 3 * h + 1
    while h >= 1:
        for i in xrange(h, N, 1):
            for j in xrange(i, h - 1, -h):
                if aList[j] < aList[j - h]:
                    exchange(aList, j, j - h)
        h = h / 3
        display_temp.append(copy.copy(aList))
    pass
    showList(display_temp)
    return aList


if __name__ == "__main__":
    print "begin"
    aList = np.random.randint(0, 100, 30)
    sortedList = shellSort(aList)
    print sortedList, "aaa"
    pass
