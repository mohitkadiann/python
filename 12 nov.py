#Ques 1:

a=int(input("Enter the value of n:"))
s=0
for i in range(1,a+1):
    s+=i
print("Sum is:",s)

#Ques 2:

a=input("Enter the string:")
for i in range(1,len(a)+1):
    print("Reversed string is:",a[-i],end="")

#Ques 3:

a=eval(input("Enter the list:"))
s=0
for i in a:
    s+=i
print("Sum of elements is:",s)

#Python practice question

#Ques 1:

a=int(input("Enter the number:"))
b=int(input("Enter the power:"))
p=a
for i in range(1,b):
    p=p*a
print(a,"^",b,"=",p)

#Ques 2:

def display_student(name,place):
    print(name,place)
display_student("Mohit","Haryana")
showStudent = display_student
showStudent("Mohit","Haryana")

#Ques 3:

a=int(input("Enter the lower limit:"))
b=int(input("Enter the upper limit:"))
s=0
for i in range(a,b+1):
    if i%2==0:
        continue
    else:
        s+=i
print("Sum of all odd numbers between",a,"and",b,"is:",s)

#Ques 4:

a=int(input("Enter the number:"))
o=True
for i in range(1,a):
    if i**2==a:
        o=False
        print("Even number")
        break
    else:
        o=True
if o==True:
    print("Odd number")

#Ques 5:

a=int(input("Enter the number:"))
p=True
if a==1:
    print(a,"is neither prime nor composite")
elif a==2:
    print(a,"is a prime number")
else:
    for i in range(2,a):
        if a%i==0:
            print(a,"is a composite number")
            p=False
            break
        else:
            p=True 
if p==True:
    print(a,"is a prime number")

#Ques 6:

a=int(input("Enter the lower limit:"))
b=int(input("Enter the upper limit:"))
for i in range(a,b+1):
    if i%2==0 or i%3==0:
        continue
    else:
        print(i,end=",")

#Ques 7:

a=int(input("Enter the number"))
b=str(a)
p=True
for i in range(0,len(b)):
    if b[i]==b[-(i+1)]:
        p=True
    else:
        p=False
        break
if p==True:
    print(a,"is a palindrome number")
else:
    print(a,"is not a plaindrome number")

#Ques 8:

a=input("Enter the string:")
b="aeiouAEIOU"
count=0
for i in a:
    if i in b:
        count+=1
    else:
        continue
print("Number of vowels in",a,"are:",count)

#Ques 9:

a=input("Enter the string:")
b=""
for i in range(0,len(a)):
    if i%2==0:
        b+=a[i]
    else:
        continue
print(b)

#Ques 10:

a=input("Enter the string:")
b=int(input("Enter the value of n:"))
s=""
for i in a:
    if i==a[b]:
        continue
    else:
        s+=i
print(s)

#Ques 11:

a=input("Enter the string:")
b=" "
s=""
for i in a:
    if i==b:
        s+="-"
    else:
        s+=i
print(s)

#Ques 12:

a=input("Enter the string:")
count=0
for i in a:
    count+=1
print("Length of the string",a,"is:",count)

#Ques 13:

a=input("Enter the string:")
count=0
for i in a:
    if i.isupper():
        continue
    else:
        count+=1
print("No of lowecase character in the string",a,"is:",count)

#Ques 14:

a=input("Enter the string:")
b="aeiouAEIOU"
count=0
for i in a:
    if i in b:
        count+=1
    else:
        continue
print("Number of vowels in",a,"is:",count)

#Ques 15:

a=input("Enter the string:")
u=0
l=0
for i in a:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
print("Number of lowercase letters are:",l)
print("Number of uppercase letter are:",u)

#Ques 16:

a=input("Enter the first string:")
b=input("Enter the second string:")
for i in a:
    if i in b:
        print(i,end=" ")
    else:
        continue

#Ques 17:

a=input("Enter the string:")
p=True
for i in range(0,len(a)):
    if a[i]==a[-(i+1)]:
        continue
    else:
        p=False
        break
if p==True:
    print(a,"is a palindrome number")
else:
    print(a,"is not a palindrome number")

#Ques 18:

a=input("Enter the string:")
b=input("Enter the character to check:")
count=0
for i in a:
    if i==b:
        count+=1
print("Number of times",b,"has occured in",a,"is:",count)
