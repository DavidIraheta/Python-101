# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.
user_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = {vowel: 0 for vowel in vowels}
for char in user_string:
    if char in vowels:
        vowel_count[char] += 1
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")