# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings
user_string1 = input("Tell me something good: ")
user_string2 = input("What made your week great?: ")
user_string3 = input("What was your favorite part of your day today?: ")
string_list = [user_string1, user_string2, user_string3]
longest_string = ""
for string in string_list:
    if len(string) > len(longest_string):
        longest_string = string
print(f"{len(longest_string)}, {longest_string}")