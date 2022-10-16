#BITWISE OPERATORS
#They are used to compare binary numbers
# $ ->and->both bits are one then sets to 1
# | ->or-> if atleast one bit is 1 then it sets to 1
# ^ ->XOR-> if one and only one of the two bits is  then it sets to 1
# ~ ->NOT-> it inverts the results

# << ->zero fill left shift->the binary number is appended with 0's at the end
# A=10
#A<<2=1010<<2=101000
# >> ->right shift-> the right side of the bits is removed
#A>>2=10(remove the right side after 2 bits)
x=10
y=7
print(x|y)