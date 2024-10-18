import random
Choice=int(input("welcome to the game of rock paper sciccors\n Choose 0, 1 or 2 for rock, paper 0r scissor"))
if Choice==0:
    print("rock")
elif Choice==1:
    print("paper")
elif Choice==2:
    print("scissors")

   
Computer_choice=random.randint(0,2)

if Computer_choice==0:
    print("rock")
elif Computer_choice==1:
    print("paper")
elif Computer_choice==2:
    print("scissors")


if 3<= Choice<0:
    print("please choose a valid number")
elif Choice == Computer_choice:
    print("Draw")
elif (Choice == 0 and Computer_choice== 1) or (Choice == 1 and Computer_choice==2) or (Choice==2 and Computer_choice==0):
    print("Computer Won")
elif (Choice == 1 and Computer_choice== 0) or (Choice == 2 and Computer_choice==1) or (Choice==0 and Computer_choice==2):
    print("you Won")