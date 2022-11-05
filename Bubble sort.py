aList=eval(input("Enter the list:"))
print("Original list is:",aList)
n=len(aList)
for i in range(n):
    for j in range(0,n-i-1):
        if aList[j]>aList[j+1]:
            aList[j],aList[j+1]=aList[j+1],aList[j]
print("List after sorting is:",aList)
