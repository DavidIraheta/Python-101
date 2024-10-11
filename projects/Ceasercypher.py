# Replicate one of the oldest known encryption by writing your own code.
# Apply a Cesar cipher of 7 to the secret variable.
# P.S.: http://www.montypython.net/scripts/dentist.php ;)
# You can start with the following code:
# lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
# secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
# cipher = 7
# You can tackle this challenge using the skills you've learned so far in the course. It might take you a moment to figure out a solution, but give it a try.
# Some concepts that you've learned about so far that might come in handy are looping, conditional statements, string methods, slicing, and indexing.
# As a stretch task you could adapt your solution so that it preserves capitalization of the original text, and that you can change the cipher to get a different encoding.
# Can you also write code to reverse the encryption?
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
text = 
for char in secret:
    if char in lowercase_letters:
        index = lowercase_letters.index(char)
        new_index = (index + cipher) 
