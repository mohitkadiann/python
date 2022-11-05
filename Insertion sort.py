aList=eval(input("Enter the list:"))
print("Original list is:",aList)
n=len(aList)
for i in range(1,n):
    key=aList[i]
    j=i-1
    while j>=0 and key<aList[j]:
        aList[j+1]=aList[j]
        j=j-1
    else:
        aList[j+1]=key
        
print("List after sorting is:",aList)
