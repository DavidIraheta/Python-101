# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
filename_ispdf = True

filename = "operators.pdf"
filename_ispdf = True

# The expected characters for the '.pdf' extension
expected_extension = ['p', 'd', 'f']

# Counter to track the position from the end of the string
count = 0
# Loop through the filename in reverse
for char in reversed(filename):
    # Check if we have checked the last four characters
    if count < 4:
        # Check if the character matches the expected extension
        if char != expected_extension[count]:
            filename_ispdf = False  # Set the flag to False if there's a mismatch
            break  # Exit the loop if a mismatch is found
        count += 1
    else:
        break  # Exit the loop after checking four characters

# Check the result
if filename_ispdf:
    print(f"{filename} is a PDF file.")
else:
    print(f"{filename} is NOT a PDF file.")
