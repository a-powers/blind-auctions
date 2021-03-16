from replit import clear
#HINT: You can call clear() to clear the output in the console.




all_bids = {}
active_bids = False

while not active_bids:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    all_bids[name] = bid
    more_bidders = input("Are there more bidders? ")
    if more_bidders == "n":
        active_bids = True
        print(all_bids)