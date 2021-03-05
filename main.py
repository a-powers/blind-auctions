from replit import clear
#HINT: You can call clear() to clear the output in the console.

name = input("What is your name? ")
bid = int(input("What is your bid? $"))
more_bidders = input("Are there more bidders? ")

all_bids = {}
active_bids = True

while not active_bids:
    
    all_bids[name] = bid

    print(all_bids)
    active_bids = False



