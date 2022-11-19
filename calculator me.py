print("                  :-Are you ready to use the scientific calculator-:")
print("This is a list of operations you can perfrom here:")
print("1-> Addition")
print("2-> Subtraction")
print("3-> Multiplication")
print("4-> Divison")
print("5-> Remainder")
print("6-> Sine")
print("7-> Cosine")
print("8-> Tangent")
print("9-> Conversion from degree to radian")
print("10-> Conversion from radian to degree")
t=True
import math
while t is True:
    c=int(input("Enter the respective number for the operation you want to perfrom:"))
    if c==1:
        a=float(input("Enter the first number here:"))
        b=float(input("Enter the second number here:"))
        print("The sum of",a,"and",b,"is:",a+b)
    elif c==2:
        a=float(input("Enter the first number here:"))
        b=float(input("Enter the second number here:"))
        print("The difference of",a,"and",b,"is:",a-b)
    elif c==3:
        a=float(input("Enter the first number here:"))
        b=float(input("Enter the second number here:"))
        print("The product of",a,"and",b,"is:",a*b)
    elif c==4:
        a=float(input("Enter the first number here:"))
        b=float(input("Enter the second number here:"))
        print("The quotient of",a,"and",b,"is:",a/b)
    elif c==5:
        a=float(input("Enter the first number here:"))
        b=float(input("Enter the second number here:"))
        print("The remainder when",a,"is divided by",b,"is:",a%b)
    elif c==6:
        a=input("You want to enter the angle in radians or degree:write(r/d)")
        if a=="r":
            b=float(input("Enter the ange in radians:"))
            print("Sine of",b,"radians is:",math.sin(b))
        elif a=="d":
            b=float(input("Enter the ange in degree:"))
            print("Sine of",b,"degree is:",math.sin(b*(math.pi)/180))  
    elif c==7:
        a=input("You want to enter the angle in radians or degree:write(r/d)")
        if a=="r":
            b=float(input("Enter the ange in radians:"))
            print("Cosine of",b,"radians is:",math.cos(b))
        elif a=="d":
            b=float(input("Enter the ange in degree:"))
            print("Cosine of",b,"degree is:",math.cos(b*(math.pi)/180))    
    elif c==8:
        a=input("You want to enter the angle in radians or degree:write(r/d)")
        if a=="r":
            b=float(input("Enter the ange in radians:"))
            print("Tangent of",b,"radians is:",math.tan(b))
        elif a=="d":
            b=float(input("Enter the ange in degree:"))
            print("Tangent of",b,"degree is:",math.tan(b*(math.pi)/180))  
    elif c==9:
        b=float(input("Enter the ange in degree:"))
        print(b,"degree is equal to:",b*(math.pi)/180,"radians") 
    elif c==10:
        b=float(input("Enter the angle in radians:"))
        print(b,"radians is equal to:",math.degrees(b))
    d=input("You want to continue using or want to quit the calculator:(c/q)")
    if d=="c" or d=="C":
        t=True
    else:
        t=False
print("Thanks for using the scientific calculator ")