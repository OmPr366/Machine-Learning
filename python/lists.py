myList =  ['om','om','Sansu','Himanshu']
print(myList)


myList =  list()
print(myList)

myList =  ["Om",5,True, "-90"]
print(myList)

print("Index at 1 is :- "+myList[0])
print("Index at 1 is :- "+myList[-1])

myList.append("Sannn")

for i in myList:
    print(i)

print("omi" in myList)

print(len(myList))

print("**********************")
print("**********************")
print("**********************")
print("**********************")

newlist =  [2]*5

newlist2 =  [90.34,34,3,5,23,7,78]

newlist+= newlist2

print(newlist)
print("newlist")
print(newlist[:-1])
print(newlist[:])
print(newlist[::-1])
