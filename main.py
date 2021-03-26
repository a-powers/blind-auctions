from replit import clear
#HINT: You can call clear() to clear the output in the console.
print("Welcome to the Auction.")

bidder = False

while not bidder:

    auction_bids = {}
    name1 = input("What is your name? ")
    bid1 = int(input("How much are you bidding? $"))
    auction_bids[name1] = bid1
    bidder = True
    print(auction_bids)