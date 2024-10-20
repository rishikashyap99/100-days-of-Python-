import random
from wordlist import word_list
from hangman_satges import stages,logo


choose=random.choice(word_list)
print(logo)
placeholder=""

for char in choose:
    placeholder+="_"
print(placeholder)
life=6
game_over=False
correct_letters=[]


while not game_over:
    letter= input("guess a letter in the word: ".lower())
    display=""

    if letter in correct_letters:
        print(f"you already choose {letter}, guess another letter")

    for char in choose:
        
        if letter==char:
            display+=char
            correct_letters.append(char)
                
        elif char in correct_letters:
            
            display+=char

        else:
            display+="_"

    print(display)

    if letter not in choose:
        
        life-=1
        print(F"*****************  TOTAL LIFE LEFT {life}/6   **********************")       
        if life==0:
            game_over=True
            print("***************  YOU LOSE  ******************\n GAME OVER")

    if "_" not in display:
            game_over=True
            print("*****************  YOU WON  ************************")

    print(stages[life]) 
