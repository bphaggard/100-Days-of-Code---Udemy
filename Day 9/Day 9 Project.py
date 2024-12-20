from art import logo

auction_users = {}
other_bidders = True

print(logo)

while other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_users[name] = bid
    others = input("Are there other users who want to bid? Type 'yes' or 'no': ").lower()
    if others == "no":
        max_value = 0
        for value in auction_users:
            if auction_users[value] > max_value:
                max_value = auction_users[value]
                winner = auction_users[value]

        for name, bid in auction_users.items():
            if max_value == bid:
                print("\nThe winner of this auction is {} with a bid of ${}".format(name, bid))
        other_bidders = False
    else:
        print("\n" * 100)

# # Solution
# bids = {}
# bidding_finished = False
#
# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid:
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")
#
# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()