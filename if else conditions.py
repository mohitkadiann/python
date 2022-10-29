# if else conditions

# some imp logical conditions
x=2
y=2
x==y        #equals
x!=y        #not equal






'''syntax of if condition
if(conditon):
    code that need to be executed if the conditon is true'''
if(2>1):
    print("2 is greater then 1")
if(2<1):
    print("2 is smaller then 1")
x=5
y=3
if(x>y):
    print("x is greater then y")
else:       #all the condition except the if condition will be executed here
    print("x is smaller then or equals to y")
# if student comes at college entry time then student is allowed but with late remarks(elif conditions)
collegeEntryTime= 9
studentEntryTime= 8
if(studentEntryTime<collegeEntryTime):
    print("you can go to college")
elif(stundentEntryTime==collegeEntryTime):
    print("you can go to college but you are late today")
else:
    print("go back to your home")
    
# Short hand if condition
if(10>5): print("10 is greater then 5")

# Short hand if else condition
x=5
y=6
print("X") if x>y else print("Y")

# Logical operators "and" and "or" keywords
x=2
y=3
z=4
if(x<y and x<z):
    print(x,"is the smallest number among",x,y,z)
# Nested conditions
age=int(input("Enter your age"))
if(age>=18):
    print("You are allowed to the cinema")
elif(age<18):
    if(age<10):
        print("You are not allowed in the cinema")
    else:
        print("You are allowed in the cinema with your parents")







