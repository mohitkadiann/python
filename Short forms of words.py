print("                -:Generating an acronym word from a given sentence:-")
# Taking a list as input that contains various strings
alist=eval(input("Enter the list containing multiple strings:"))
acr=""
# Splitting the elements of the list that are the strings here
for i in alist:
    # Taking the first character of the strings and adding them to make a new string
    acr=acr+i[0]
# Converting the acronym into upper case
# And printing the final acronym word
print(acr.upper())    
