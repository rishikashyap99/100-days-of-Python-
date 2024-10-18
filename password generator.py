import random
# List of uppercase characters

characters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

Char = int(input("Enter the number of  letters: "))
num = int(input("Enter the number of numbers: "))
sym = int(input("Enter the number of symbols: "))

# List of numbers from 0 to 9
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of some symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

password=[]
for i in range (0,Char):
    password.append(random.choice(characters))
for i in range (0,num):
    password.append(random.choice(numbers))
for i in range (0,sym):
    password.append(random.choice(symbols))

random.shuffle(password)

new=""
for items in password:
    new+=items
print("the suggested strong password is :" , new)



    
    

