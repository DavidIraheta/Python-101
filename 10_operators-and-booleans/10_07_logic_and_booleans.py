# Demonstrate the use of all logical operators (and, or, not) below.
# Create variables that hold boolean values, then combine them
# to express the following sentence:
#
#   do two wrongs make a right?
# 
# Note that the truth value of the statement doesn't matter,
# but try to use all three logical operators in one line of code
# to get another boolean value as your result :)

wrong = False
right = True
temp = 80
sunny = True 
if temp <= 50 or temp >= 85 and not sunny :
    print(" The Tempature is bad")
else: 
    print("The tempature is good")
if sunny: 
    print("it is sunny outside")
else: 
    print("it is cloudy outside")