import random

rps=["rock","paper","scissors"]
ran=random.randint(0, 2)
computer_input = "a"
if ran==0:
    computer_input=rps[0]
elif ran==1:
    computer_input=rps[1]
elif ran==2:
    computer_input=rps[2]

player_input=int(input("Please type '0'(rock) or '1'(paper) or '2'(scissors)\n"))
if player_input==0:
    player_input=rps[0]
elif player_input==1:
    player_input=rps[1]
elif player_input==2:
    player_input=rps[2]

print(f"You chose {player_input}!")
print(f"Computer chose {computer_input}!")

if player_input==rps[0]:
    if computer_input==rps[0]: print("Draw!")
    elif computer_input==rps[1]: print("You lost!")
    elif computer_input==rps[2]: print("You won!")

if player_input==rps[1]:
    if computer_input==rps[0]: print("You won!")
    elif computer_input==rps[1]: print("Draw!")
    elif computer_input==rps[2]: print("You lost!")

if player_input==rps[2]:
    if computer_input==rps[0]: print("You lost!")
    elif computer_input==rps[1]: print("You won!")
    elif computer_input==rps[2]: print("Draw!")

# import random
#
# numba=random.randint(0, 1)
# if numba==0:
#     print("heads")
# elif numba==1:
#     print("tails")

# import random
#
# print("welcome to London's rich bankers russian roulette")
#
# list = []
#
# list=input("Please write names of the people that are going to play this game, split the names with a comma \n")
# listsp=list.split(",")
#
# numberofppl=len(listsp)
#
# participants=random.randint(0, numberofppl - 1)
# print(f"there were {participants} people...")
# print(f"and {listsp[participants]} was the unlucky one!")


# r1=["a","a","a"]
# r2=["a","a","a"]
# r3=["a","a","a"]
# l=[r1,r2,r3]
# print(f"{r1}\n{r2}\n{r3}")
# pos=input("coords please\n")
# horizonal=int(pos[0])
# vertical=int(pos[1])
#
# l[horizonal - 1][vertical - 1] = "X"
#
# print(f"{r1}\n{r2}\n{r3}")
