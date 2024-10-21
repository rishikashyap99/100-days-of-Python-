import random

deck_list=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]

computer_list=[]

for i in range(2):
    computer_list.append(random.choice(deck_list))
    comp_total=sum(computer_list)
print(f"Computer's one of the card is {random.choice(computer_list)}")


player_list=[]

for i in range(2):
    player_list.append(random.choice(deck_list))
    my_total=sum(player_list)
print(f"your cards are {player_list}")

add=input("do you want to add more cards yes/ no").lower()
if add=="yes":
    player_list.append(random.choice(deck_list))
    my_total=sum(player_list)

print(f"your cards are {player_list} : Total Score :{my_total}")

if comp_total<21:
        computer_list.append(random.choice(deck_list))

def check():
    while my_total>21:

        if 11 in player_list and my_total>21:
            my_total-=10
    black_jack()


def black_jack():
    show=input("do you want to show the cards yes/ no").lower()
    if show=="yes":
        if comp_total==my_total:
            print("both have same as total draw")
        elif my_total>21 and comp_total<=21:
            check()            
            print(f"you cards are {player_list}, computer cards are {computer_list} , you lose")
        elif comp_total<my_total<=21:
            check()
            print(f"you cards are {player_list}, computer cards are {computer_list} , you won")
        elif my_total<comp_total<=21:
            check()
            print(f"you cards are {player_list}, computer cards are {computer_list}computer won")
        

black_jack()


