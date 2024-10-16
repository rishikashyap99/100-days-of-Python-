print("Welcome to the game of treasure hunt")
name=input("enter player name\n")
print(f"{name}, You are on mission to find trasure")
choice1=input('you\'re at the path with two ways\n choose the direction "left" or "right"\n'.lower())
if choice1=='right':
    choice2=input("you reached to river\n there is an island in between the centre . choose wait for the boat or swim\n")
    if choice2=='wait':
        choice3=input("There are 3 doors of different colors \n you can choose any one of them \n choose the color of the door [red/yellow/blue]\n")
        if choice3=='yellow':
            print("congratulations you find the treasure! \n now you're rich")
        else:
            print(" you chosen wrong door \n game over")
    else:
        print("OOPS! \n There are crocodile in the river\n game over")
else:
    print("OOPS!! \nYou fallen into trap hole !! game over")
