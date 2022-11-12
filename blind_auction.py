import art

print(art.logo)
print("Welcome to the secret auction program.")

bidders_dictionary = [

]


def add_bidders(my_name, my_bid):
    # bidders_dictionary["name"] = my_name
    # bidders_dictionary["bid"] = my_bid

    bidders_dictionary.append({"name": str(my_name), "bid": int(my_bid)})


name = input("What is your name?: ")
bid = input("What is your bid?: $")
add_bidders(name, bid)

more_bidders = True

while more_bidders:
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if other_bidders == "yes":
        another_name = input("What is your name?: ")
        another_bid = input("What is your bid?: $")
        add_bidders(another_name, another_bid)
    else:
        print(bidders_dictionary.values())
        find_max = max(bidders_dictionary.values(), key=bidders_dictionary.get)
        print("Highest bidder {highest_bidder} has won! Congratulations".format(highest_bidder=find_max))
        exit()
