#working with strings

#slice a string x[startIndex : endIndex]

x="mohitkadian"
print(x[2:8])
print(x[:5]) #if we want it to start from the starting
print(x[2:]) #from the index to last element
print(x[-6:-3]) #indexing from back

#modify the strings

x="my name is mohit kadian"
print(x.upper()) # all letters in uppercase
print(x.lower()) # all letters in lowercase

splittedText=x.split()
print(splittedText[2])

#replace a string with another one

x="mohit kadian"
print(x.replace("m","r"))

#adding two strings

x="mohit"
y="kadian"
print(x+y)

#booleans

#true or false bool

print(23>11)
print(22==11)
print(20<19)
#exceptions for bool
#1..almost any kind of value will result in true if it has some content
#2..any string passed is true except empty string
#3..any number passed is true except 0
#4..any list tuple dictionary will result in true except the empty ones

#python lists

#creating list
#1..simple way
myList=[1,2,3,"mohit","kadian"]
print(myList)
#length of list
print(len(myList))
#2..using a list constructor
myList=list((1,2,3,33))
print(myList)
#access list items
myList=[10,20,True,30,'mohit']
print(myList[3])  # selecting a single element
print(myList[-3]) #indexing from backside
print(myList[2:5]) #a set of elements

#changing the value at a index
myList=[10,20,30,40,50]
myList[1]=200
myList[1:3]=[2,3]
print(myList)

#inserting a new item
#1..using insert
my_list=[10,20,30,40]
my_list.insert(4,500)
print(my_list)
#2..using append->will always add in the end
my_list.append(5)
print(my_list)

#3..using extend function
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list1)
print(list1)
print(list2)


#remove list items
#1..remove by element
mylist=[1,2,3,4,3]
mylist.remove(3)
print(mylist)
#2..remove by index using pop
mylist.pop(2)#if we don't pass any index here then it removes the last element
print(mylist)


















