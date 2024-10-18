# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.
user_name = input("What is your name?:")
print(f"Hello {user_name} Welcome to Medieval Times")
print("There are two doors in front of you. One on the left and one on the right")
has_sword = False
door_choice = input("Which door do you choose, left or right?: ").lower()
if door_choice == "left":
    print("You have entered an empty room")
    look_around = input("Would you like to look around? yes / no: ").lower()
    if look_around == "yes":
        print("You have found a sword!")
        sword_choice = input("Would you like to take the sword: yes / no: ").lower()
        if sword_choice == "yes":
            has_sword = True
            print("You now have a sword!")
        else: 
            print("You have left the sword")
    else: 
        print("You have left the room without looking around")
    open_right_door  = input("Would you like to open the right door now? yes / no: ").lower()
    if open_right_door == "yes":
        print("You have entered the room with a dragon!")
        fight_choice = input("Would you like to fight the dragon? yes / no: ").lower()
        if fight_choice == "yes":
            if has_sword:
                print("You bravely fight the dragon with your sword and win! You are victorious!")
            else:
                print("You try to fight the dragon, but without a sword, you are eaten. Game over.")
        else:
            print("You chose not to fight the dragon. You lose.")
elif door_choice == "right":
    print("You have entered the room with a dragon!")
    fight_choice = input("Would you like to fight the dragon? yes / no: ").lower()
    if fight_choice == "yes":
        if has_sword:
            print("You bravely fight the dragon with your sword and win! You are victorious!")
        else:
            print("You try to fight the dragon, but without a sword, you are eaten. Game over.")
    else:
        print("You chose not to fight the dragon. You lose.")
else: 
    print("Invalid choice. You lose.")

        # open_right_door = input("Would you like to open the right door? yes / no: ").lower()
        # if open_right_door == "yes":
        #     print("You have entered the room with a dragon!")
        #     fight_choice = input("Would you like to fight the dragon? (yes/no): ").lower()
        # if fight_choice == "yes":
        #      has_sword == True
        #     print("You bravely fight the dragon with your sword and win! You are victorious!")
        # else:
        # print("You try to fight the dragon, but without a sword, you are eaten. Game over.")
        # else:
        # print("You chose not to fight the dragon. You lose.")
#         else:
#         print("You chose not to open the right door. There are no more doors left. Game over.")
#         if door_choice== "right":
#     print("You have entered the room with a dragon!")
# fight_choice = input("Would you like to fight the dragon? (yes/no): ").lower()
# if fight_choice == "yes":
#         if has_sword:
#             print("You bravely fight the dragon with your sword and win! You are victorious!")
#         else:
#             print("You try to fight the dragon, but without a sword, you are eaten. Game over.")
#     else:
#         print("You chose not to fight the dragon. You lose.")
# else:
# print("Invalid choice. Game over.")
        
# elif door_choice == "right":
# print("There is a dragon in this room!")
#     fight_choice = input("Would you like to fight the dragon? yes / no: ").lower()
#     if fight_choice == "yes":
#         if has_sword:
#             print("You have defeated the dragon! You win!") 
#     else:
#         print("You have been eaten by the dragon! You lose!")
              

       
# user_name = input("What is your name? ")
# print(f"Hello {user_name}, Welcome to Medieval Times!")
# print("There are two doors in front of you. One on the left and one on the right.")

# has_sword = False  # Initialize sword possession to False

# # First choice: which door to enter
# door_choice_ = input("Which door do you choose, left or right?: ").lower()

# # Left Door
# if door_choice_ == "left":
#     print("You have entered an empty room.")
    
#     look_around = input("Would you like to look around? (yes / no): ").lower()
#     if look_around == "yes":
#         print("You have found a sword!")
#         sword_choice = input("Would you like to take the sword? (yes / no): ").lower()
        
#         if sword_choice == "yes":
#             has_sword = True
#             print("You now have a sword!")
#         else:
#             print("You left the sword.")
#     else:
#         print("You left the room without looking around.")

#     open_right_door = input("Would you like to open the right door now? (yes / no): ").lower()
    
#     if open_right_door == "yes":
#         print("You have entered the room with a dragon!")
#         fight_choice = input("Would you like to fight the dragon? (yes / no): ").lower()
        
#         if fight_choice == "yes":
#             if has_sword:
#                 print("You bravely fight the dragon with your sword and win! You are victorious!")
#             else:
#                 print("You try to fight the dragon, but without a sword, you are eaten. Game over.")
#         else:
#             print("You chose not to fight the dragon. You lose.")
#     else:
#         print("You chose not to open the right door. There are no more doors. Game over.")

# # Right Door
# elif door_choice_ == "right":
#     print("You have entered the room with a dragon!")
    
#     fight_choice = input("Would you like to fight the dragon? (yes / no): ").lower()
    
#     if fight_choice == "yes":
#         if has_sword:
#             print("You bravely fight the dragon with your sword and win! You are victorious!")
#         else:
#             print("You try to fight the dragon, but without a sword, you are eaten. Game over.")
#     else:
#         print("You chose not to fight the dragon. You lose.")

# # Invalid Choice
# else:
#     print("Invalid choice. Game over.")