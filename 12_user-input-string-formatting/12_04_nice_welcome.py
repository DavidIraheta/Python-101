# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.
user_name = input("Enter your name: ")
first_name = user_name.split()[0]
print(f"So Good To Have You Here", {first_name},"!")
if __name__ == "__main__":
    pass
else:
    pass

# Prompt the user to input their name. Store the input in a variable called `user_name`.
# Split the `user_name` into a list of words. Store the result in a variable called `name_list`.