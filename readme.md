# 排序算法
1. 插入排序
2. 选择排序
3. 希尔排序


## 插入排序
代码
```
def insertSort(aList):
    display_temp = []
    for i in xrange(1, len(aList)):
        for j in xrange(i, 0, -1):
            if aList[j] < aList[j - 1]:
                exchange(aList, j, j - 1)
        display_temp.append(copy.copy(aList))
    showList(display_temp)
    return aList
```
![图片](http://cl.ly/3x122z2o2T1N/download/insert.png)


## 选择排序
```
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

```
![图片](http://cl.ly/3v0923171B2q/download/select.png)


## 希尔排序
### 改进型插入排序 希尔排序的思想是使数组中任意间隔为h的元素都是有序的，即h有序数组。在进行排序时，若h很大，我们就能将元素移动到远处。h=1时，数组即为有序数组了。
#### 代码
```
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
    ```
![图片](http://cl.ly/0w1l2Y3Z0H2A/download/shell.png)
