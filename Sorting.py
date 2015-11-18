
myList = [2,3,5,6,1,4,7,9,8]
m = 0
length = len(myList)
for i in range(length):
    for j in range(length - 1 - i):
        if myList[j] > myList[j+1]:
            myList[j], myList[j+1] = myList[j+1],myList[j]
            m = m + 1
            print(myList)
print("Periods  = ", m)
