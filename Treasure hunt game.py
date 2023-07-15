#Treasure hunt game

print("Welcome to Treasure hunt island !!!\nYour in the middle of the mountain Hunting for a Treasure")

choice1 = int(input("enter 1 to go up or 2 to go down: "))

if choice1 == 2:
       print("You will reached the top of mountain !!!")

       choice2 = int(input("Enter 1 to Swim or 2 to Wait for the boat: "))   

       if choice2 == 2:
            print("You reached the island \n There is a house with 3 doors in front of you!!!")

            choice3 == int(input("Choose the door: \n1-Red \n2-Yellow \n3-Blue \n"))

            if choice3 == 1:
                print("Room is full of fire!!")
                print("Game over")

            elif choice3 == 2:
                print("Room is full of Glod!!")
                print("You found the Treasure! \n You won the Game!!!")

            elif choice3 == 3:
                print("Room is Full of Monsters!!")
                print("Game over!")

            else:
                print("please choose the correct door no ")
                print("Game over!")

       elif choice2 == 1:
            print("You got attacked by a Crocodile !!!! You died \n Game over!")

elif choice1 == 1:
    print("You reached top of the mountain ! fell down\n Game over!!!!")
else:
    print("please enter te correct no")
    

            

    
            
            
            
    

                              
