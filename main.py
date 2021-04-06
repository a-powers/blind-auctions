from replit import clear
#HINT: You can call clear() to clear the output in the console.

bid_list = []
continue_bidding = True


while continue_bidding:
    bid_dict = {}
    bidder = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bid_dict[bidder] = bid
    bid_list.append(bid_dict[bidder])
    more_bidders = input("Are there more bidders? ")
    if more_bidders == "no":
        continue_bidding = False
    print(bid_list)