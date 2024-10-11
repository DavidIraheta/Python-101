# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
user_input = input("What do you think of the New York Jets this season?:")
sarcastic_response = ""
for index, char in enumerate(user_input):
    if index % 2 == 0:
        sarcastic_response += char.lower()
    else:
        sarcastic_response += char.upper()
print(sarcastic_response)
 