def highest_bidder(Bid_dictionary):
    highest_bid=0 
    for bidder in Bid_dictionary:
        Bid_amount=Bid_dictionary[bidder]
        if Bid_dictionary[bidder]>highest_bid:
             highest_bid=Bid_amount
    print(f"the bid winner is {name} with the highest bid of : {highest_bid}")

Bid_Dict={}

bid_continue=True

while bid_continue:
    name=input("Enter your name: ")
    Bid_price=int(input("enter your bidding amount: $"))
    Bid_Dict[name]=Bid_price
    next=input("are there any other bidders: yes/no").lower()
    if next=="no":
        bid_continue=False
        highest_bidder(Bid_Dict)
    elif next=="yes":
        print("\n"*30)
   

