# <!-- Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game. -->
user_name = input("What is your name")
print(f"Hello {user_name} welcome to David's world")
print("There are two doors in front of you. One on the left and one on the right")
has_sword = False
door_choice_ = input("Which door do you choose, left or right?: ").lower()
if door_choice_ == "left":
    print("You have entered an empty room")
    look_around = input("Would you like to look around? yes / no: ").lower()
    if look_around == "no":
        print("You left the room")
    if look_around == "yes":
        print("You have found a sword!")
        sword_choice = input("Would you like to take the sword: yes / no: ").lower()
        if sword_choice == "yes":
            print("You found a sword!")
            print("Would you like to open the right door? yes / no: ").lower()
            has_sword = True
        #     open_right_door = input("There is a dragon in this room! Would you like to fight the dragon? yes / no: ").lower()
        # #    if has_sword == True:
        #         print("You have defeated the dragon! You win!")
        #     else: 
        #         print("You have been eaten by the dragon! You lose!")
        # if fight_choice == "no":
        #     print("You left the sword")
        #     if_leaves_sword = "You have left the room"
        #     print( " Would you like to try the right door? yes / no: ").lower()
        #     if open_right_door == "no":
        #         print("You lose, there are no more doors to choose from")
        # elif open_right_door == "yes" and has_sword == True:
        #     print("You have defeated the dragon! You win!")
        # has_sword = True
        # if door_choice_ == "right":
        #     print("There is a dragon in this room!")
        #     # fight_choice = input("Would you like to fight the dragon? yes / no: ")
        #     if fight_choice == "yes":
        #         if has_sword:
        #             print("You have defeated the dragon! You win!") 
        #         else:
        #             print("You have been eaten by the dragon! You lose!") 
        


