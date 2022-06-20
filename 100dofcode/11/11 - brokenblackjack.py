# import random  #got tangled
#
# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
#
# user_cards = 0
# user_score = 0
# dealer_cards = 0
# dealer_score = 0
#
# if user_cards == 0:
#     user_score += random.choice(cards) + random.choice(cards)
#     user_cards += 2
#     print(f"user: {user_score}[{user_cards}]")
#     dealer_score += random.choice(cards)
#     dealer_cards += 2
#     print(f"dealer: {dealer_score}[{dealer_cards}]")
#     dealer_score += random.choice(cards)
#     dealer_cards += 1
#
# hit = False
# if user_score < 22:
#     hit_stand = input("Hit or stand?").lower()
# if hit_stand == "hit":
#     user_score += random.choice(cards)
#     user_cards += 1
#     print(f"user: {user_score}[{user_cards}]")
#     if user_score < 22:
#         hit_stand = input("Hit or stand?").lower()
#     if user_score > 21:
#         print(f"You lost! {user_score}[{user_cards}] - {dealer_score}[{dealer_cards}]")
#         exit()
#     while dealer_score < 17 and dealer_score < 22:
#         dealer_score += random.choice(cards)
#         dealer_cards += 1
#         print(f"dealer: {dealer_score}[{dealer_cards}]")
#         if dealer_score > 22:
#             print(f"You won! {user_score}[{user_cards}] - {dealer_score}[{dealer_cards}]")
#
# elif hit_stand == "stand":
#     print(f"dealer: {dealer_score}[{dealer_cards}]")
#     while dealer_score < 17 and dealer_score < 22:
#         dealer_score += random.choice(cards)
#         dealer_cards += 1
#         print(f"dealer: {dealer_score}[{dealer_cards}]")
#         if dealer_score > 22:
#             print(f"You won! {user_score}[{user_cards}] - {dealer_score}[{dealer_cards}]")
#
# if user_score > 21:
#     if dealer_score < 21:
#         print(f"You lost! {user_score}[{user_cards}] - {dealer_score}[{dealer_cards}]")
#     else:
#         print("debug the game retard")
#
# elif user_score < 21:
#     if dealer_score < 21:
#         if user_score > dealer_score:
#             print(f"You won! {user_score}[{user_cards}] - {dealer_score}[{dealer_cards}]")
#         else:
#             print(f"You lost! {user_score}[{user_cards}] - {dealer_score}[{dealer_cards}]")
#     else:
#         print(f"You won! {user_score}[{user_cards}] - {dealer_score}[{dealer_cards}]")

# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]   #ace works in a way that i didn't know, need to revise the whole thing, didn't
# import random
#
# def deal():
#     return random.choice(cards)
#
# user_cards = 0
# user_score = 0
# dealer_cards = 0
# dealer_score = 0
# gamestate = "continue"
#
# if user_cards == 0:
#     user_score += deal() + deal()
#     user_cards += 2
#     while user_score == 22:
#         user_score -= 11
#         user_cards -= 1
#         user_score += deal()
#         user_cards += 1
#     print(f"user: {user_score}[{user_cards}]")
#     dealer_score += deal()
#     dealer_cards += 1
#     print(f"dealer: {dealer_score}[{dealer_cards}]")
#     dealer_score += deal()
#     dealer_cards += 1
#     userhs = input("h or s ").lower()
#
# while gamestate == "continue":
#
#     if userhs == "h":
#         user_score += deal()
#         user_cards += 1
#         print(f"user: {user_score}[{user_cards}]")
#
#         if user_score > 21:
#             print(f"You lost! {user_score}[{user_cards}] - {dealer_score}[{dealer_cards}]")
#             exit()
#
#         userhs = input("h or s ").lower()
#
#     while userhs == "s":
#         print(f"dealer: {dealer_score}[{dealer_cards}]")
#
#         while dealer_score < 17:
#             dealer_score += deal()
#             dealer_cards += 1
#             print(f"dealer: {dealer_score}[{dealer_cards}]")
#
#         if dealer_score > 21:
#             print(f"You won! {user_score}[{user_cards}] - {dealer_score}[{dealer_cards}]")
#             exit()
#
#         elif dealer_score >= 17:
#             userhs = ""
#             gamestate = "end"
#
# if gamestate == "end":
#     if user_score > dealer_score:
#         print(f"You won! {user_score}[{user_cards}] - {dealer_score}[{dealer_cards}]")
#     elif user_score == dealer_score:
#         print(f"Draw! {user_score}[{user_cards}] - {dealer_score}[{dealer_cards}]")
#     else:
#         print(f"You lost! {user_score}[{user_cards}] - {dealer_score}[{dealer_cards}]")