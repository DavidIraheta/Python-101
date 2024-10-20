# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.
# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it
word_to_guess = "halloween"
word_length = len(word_to_guess)
word_display = ["_"] * word_length
remaining_attempts = 6
guessed_letters = set()
print("Welcome to Hangman!")
print("Try to guess the word:")
print(" ".join(word_display))
print(f"You have {remaining_attempts} attempts to guess the word.")
while remaining_attempts > 0:
    user_guess = input("Enter a letter: ").lower()
    if len(user_guess) != 1 or not user_guess.isalpha():
        print("Please enter a single alphabetic letter.")
        continue
    if user_guess in guessed_letters:
        print(f"You've already guessed '{user_guess}'. Try a different letter.")
        continue
    guessed_letters.add(user_guess)
    if user_guess in word_to_guess:
        print(f"Great job! '{user_guess}' is in the word.")
        for i in range(word_length):
            if word_to_guess[i] == user_guess:
                word_display[i] = user_guess
    else:
        remaining_attempts -= 1
        print(f"Sorry, '{user_guess}' is not in the word.")
        print(f"You have {remaining_attempts} remaining attempts.")
    print(" ".join(word_display))
    if "_" not in word_display:
        print("Congratulations! You've guessed the word!")
        break
    if remaining_attempts == 0:
        print("Sorry, you've run out of attempts.")
        print(f"The word was '{word_to_guess}'.")
        break



# word_to_guess = "halloween"
# word_length = len(word_to_guess)
# word_display = ["_"] * word_length
# remaining_attempts = 8
# guessed_letters = set()
# print("Welcome to Hangman!")
# print(" ".join(word_display))
# print("Try to guess the word")
# print(f"You have {remaining_attempts} attempts to guess the word")

# while remaining_attempts > 0:
#     user_guess = input("Enter a letter: ").lower()
#     print(" ".join(word_display))
#     if len(user_guess) != 1 or not user_guess.isalpha():
#         print("Please enter a single letter")
#         continue
#     if user_guess in guessed_letters:
#         # print(" ".join(word_display))
#         print(f"You have already guessed {user_guess}. Try a different letter")
#         print(" ".join(word_display))
#         continue
#     guessed_letters.add(user_guess)
#     if user_guess in word_to_guess:
#         print(" ".join(word_display))
#         print(f"Great job! {user_guess} is in the word")
#         continue
#     for i in range(word_length):
#             if word_to_guess[i] == user_guess:
#                 word_display[i] = user_guess
#     else:
#         remaining_attempts -= 1
#     print(" ".join(word_display))
#     print(f"Sorry, {user_guess} is not in the word")
#     print(f"You have {remaining_attempts} remaining attempts")
#     if "_" not in word_display:
#          print("Sorry, that letter is not in the word")
#     break
# if word_to_guess == "".join(word_display):
#         print("Congratulations! You have won!")
# if remaining_attempts == 0:
#         print("Sorry, you have run out of attempts")
#         print(f"The word was {word_to_guess}")

# word_to_guess = "halloween"
# word_length = len(word_to_guess)
# word_display = ["_"] * word_length
# remaining_attempts = 8
# guessed_letters = set()
# print("Welcome to Hangman!")
# print(" ".join(word_display))
# print("Try to guess the word")
# print(f"You have {remaining_attempts} attempts to guess the word")

# while remaining_attempts > 0:
#     user_guess = input("Enter a letter: ").lower()
#     print(" ".join(word_display))
#     if len(user_guess) != 1 or not user_guess.isalpha():
#         print("Please enter a single letter")
#         continue
#     if user_guess in guessed_letters:
#         print(" ".join(word_display))
#         print(f"You have already guessed {user_guess}. Try a different letter")
#         continue
#     guessed_letters.add(user_guess)
#     if user_guess in word_to_guess:
#         print(" ".join(word_display))
#         print(f"Great job! {user_guess} is in the word")
#         continue
#     for i in range(word_length):
#             if word_to_guess[i] == user_guess:
#                 word_display[i] = user_guess
#     else:
#         remaining_attempts -= 1
#     print(" ".join(word_display))
#     print(f"Sorry, {user_guess} is not in the word")
#     print(f"You have {remaining_attempts} remaining attempts")
#     if "_" not in word_display:
#          print("Sorry, that letter is not in the word")
#     break
#     if word_to_guess == "".join(word_display):
#         print("Congratulations! You have won!")
#     break
#     if remaining_attempts == 0:
#         print("Sorry, you have run out of attempts")
#         print(f"The word was {word_to_guess}")
#     break