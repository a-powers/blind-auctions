from replit import clear
#HINT: You can call clear() to clear the output in the console.

bid_dict = {}
continue_bidding = False

while not continue_bidding:
    bidder = input("What is your name? ")
    bid = int(input("What is your bid? "))
    more_bidders = input("Are there more bidders? ")
    if more_bidders == 'no':
        continue_bidding = True
    else:
        bid_dict[bidder] = bid
    print(bid_dict)
    