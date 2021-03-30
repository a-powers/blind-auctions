from replit import clear
#HINT: You can call clear() to clear the output in the console.
bid_list = []
bidding_done = False

while bidding_done:
    all_bidders = {}
    bidder = input("What is your name? ")
    bid = int(input("What is your bid? "))
    all_bidders[bidder] = bid
    update_dict = all_bidders[bidder]
    bid_list.append(update_dict)
print(bid_list)
    

