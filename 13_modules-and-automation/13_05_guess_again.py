# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random

num = random.randint(1, 20)
guess = None
#allow the user to guess 5 times
for i in range(5):
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == num:
        print("You're a genius!")
        break
    else:
        print("No, sorry. Give it another try.")
        print(f"You have {4 - i} guesses left")