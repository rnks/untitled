"""
myList = [2,3,5,6,1,4,7,9,8]
m = 0
length = len(myList)
for i in range(0, length-1):
    minIndex = i
    m = m + 1
    for j in range(i+1, length):
        if myList[j] < myList[minIndex]:
            minIndex = j
    if minIndex != i:
        myList[i], myList[minIndex] = myList[minIndex], myList[i]


print(myList,"Periods  = ", m)
"""
print()