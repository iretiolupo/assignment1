myUniqueList = []

myUniqueList.append(12)

myUniqueList.append("Pen")

myUniqueList.append(23)

myUniqueList.append("Paper")

if 12 in myUniqueList:
    print(myUniqueList)
    print(False)
else:
    myUniqueList.append(12)
    print(myUniqueList)
    print(True)
    
if 100 in myUniqueList:
    print(myUniqueList)
    print(False)
else:
    myUniqueList.append(100)
    print(myUniqueList)
    print(True)