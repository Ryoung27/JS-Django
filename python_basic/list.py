myList = [1,2,3]
myList = ['string', 1, 2, 3, 4, True]

print(len(myList))

print(myList[-1])

myList.append("new item")

myList.extend([9,8,7])
print(myList)

myList.pop()
print(myList)

myList.pop(6)
print(myList)

myList.reverse()
print(myList)