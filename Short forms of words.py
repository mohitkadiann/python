print("                -:Generating an acronym word from a given sentence:-")
alist=eval(input("Enter the list containing multiple strings:"))
acr=""
for i in alist:
    acr=acr+i[0]
print(acr.upper())    
