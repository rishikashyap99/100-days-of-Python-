print("Welcome to the   Pizza Flask Deliveries")
Bill= 0

size=input("Enter the pizza size : S/M/L")

if size=='S':
    Bill +=15
elif size =='M':
    Bill +=20
elif size =='L':
    Bill +=25

Pepperoni=input("Do you want to add peperoni: Y/N")
if Pepperoni=="Y":
    if size=="S":
        Bill+=2
    else:
        Bill+=3
cheese=input("do you want extra cheese: Y/N")
if cheese=="Y":
    Bill+=5
print(f"please Pay your Total bill Amount : $ {Bill}")



