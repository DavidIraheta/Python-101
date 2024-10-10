# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4
user_string = input("string input:")
user_letter = input("letter input:")

# if len(user_letter) != 1:
#     print("Please enter a single letter")
if len(user_letter) != 1:
    print("Please enter a single letter")
# else: 
#     index = user_string.index(user_letter)
# if index != -1:
#     print(f"Result: {index}")
# else: 
#     print("Letter not found")


