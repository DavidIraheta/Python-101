# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please
user_string = input("string input:")
user_char = input("symbol input:")
# for char in user_string:
#     if char == user_string[0]:
user_string = user_string.replace(user_string[0], user_char)
print(f"Result: {user_string}")
