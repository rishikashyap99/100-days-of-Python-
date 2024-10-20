logo="""╔═══════════════════════╗
║    C A E S A R        ║
║       C I P H E R     ║
║                       ║
║   A → B → C → D ...   ║
║       (Shift)         ║
╚═══════════════════════╝"""
print(logo) 

alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

def ceaser(text, shift_amount, encode_or_decode):
    encrypted_text=""

    

    if encode_or_decode=="decode":
            shift_amount *= -1

    for letters in text:

        if letters not in alphabets:
            encrypted_text+=letters
        else:

            shift_pos =alphabets.index(letters) + shift_amount

            shift_pos%=len(alphabets)
            encrypted_text+=alphabets[shift_pos]
        
    print(f"you {encode_or_decode}d message is {encrypted_text}") 

should_continue=True
while should_continue:

    direction=input("do you want to encrypt or decrypt the message: encode/decode: ".lower())
    text_data=input("enter your message for encryption: ".lower())
    shift=int(input("enter the digits you want to shift the message: "))

    ceaser(text_data,shift,direction)
    restart=input("do you want to continue type yes/no")
    if restart=="no":
         should_continue=False
         print("good bye")






















# def encrypt(text_data, shift_amount):
#     encrypted_text=""
#     for letters in text_data:
#         shift_pos =alphabets.index(letters) + shift_amount
#         shift_pos%=len(alphabets)
#         encrypted_text+=alphabets[shift_pos]
        
#     print(encrypted_text)

# encrypt(text , shift)

# def ceaser(text, shift_amount, encode_or_decode):
#     encrypted_text=""
#     for letters in text:
#         if encode_or_decode=="decode":
#             shift_pos =alphabets.index(letters) - shift_amount

#         else:
#             shift_pos =alphabets.index(letters) + shift_amount

#         shift_pos%=len(alphabets)
#         encrypted_text+=alphabets[shift_pos]
        
#     print(encrypted_text)

# ceaser(text_data,shift,direction)