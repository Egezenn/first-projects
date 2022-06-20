# numN = int(input("Numerator:"))
# numD = int(input("Denominator:"))
# print(numN % numD)
# if numN % numD == 0:
#     print(f"{numN} is divisible by {numD}")
# else:
#     print(f"{numN} is not divisible by {numD}")

# auction_end = False
#
# while auction_end == False:
#     names = []
#     bids = []
#     name = input("Hello, what is your name?\n")
#     bid = input("How much would you like to bid?\n")
#     names += {name}
#     bids += {bid}
#     auction_end1 = input("Does anyone want to get in?\n")
#     if auction_end1 == "y":
#         auction_end = False
#     elif auction_end1 == "n":
#         auction_end = True

# stud_scores = {
#     "Amir": 81,
#     "Bill": 78,
#     "Cynthia": 99,
#     "Derrick": 74,
#     "Elizabeth": 62
# }
# for student in stud_scores:
#     if stud_scores[student] > 90:
#         stud_scores[student] = "A"
#     elif 90 >= stud_scores[student] > 80:
#         stud_scores[student] = "B"
#     elif 80 >= stud_scores[student] > 70:
#         stud_scores[student] = "C"
#     elif 70 >= stud_scores[student]:
#         stud_scores[student] = "D"
# print(stud_scores)

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
#
# def add_country(country, visits, cities):
#     new_country = {}
#     new_country["country"] = country
#     new_country["visits"] = visits
#     new_country["cities"] = cities
#     travel_log.append(new_country)
#
# add_country("Turkey", 99, ["İstanbul", "Tokat", "İzmir"])
# print(travel_log)


print("Welcome to the blind auction!")
bidders = {}
max_bid_value = 0
max_bidder = ""
auction_end = False

while not auction_end:
    name = input("Name: ")
    bid = int(input("Bid: "))
    bidders[name] = bid
    auction_end = input("Continue?\n").lower()
    if auction_end == "n":
        auction_end = True
    else:
        auction_end = False

for bidder in bidders:
    if max_bid_value < bidders[name]:
        max_bid_value = bidders[name]
        max_bidder = bidder

print(f"{max_bidder} has won the auction paying ${max_bid_value}!")
