from replit import clear
#HINT: You can call clear() to clear the output in the console.

bid_list = []
continue_bidding = True


while continue_bidding:
    bid_dict = {}
    bidder = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bid_dict[bidder] = bid
    continue_bidding = input("Are there more bidders?")
    if continue_bidding == 'no':
        continue_bidding = False
    print(bid_dict)
    