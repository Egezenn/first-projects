print("welcome to the treasure island")
opt=input("Your mission is to find the treasure in the island\nYou're at a cross road, which direction do you want to go?\nOptions are 'left', 'right'\n").lower()

if opt == "left":
    opt= input("There is a lake in front of you, do you want to swim across or wait for a boat?\nOptions are 'swim','wait'\n").lower()
    if opt == "swim": print("You don't know how to swim, you drown.")
    elif opt == "wait":
        opt= input("You get accross, there are 3 paths, which one do you want to take?\nOptions are '1', '2', '3'\n").lower()
        if opt == "1":
            opt=input("While walking on the path you see a weird looking dirt patch, do you want to walk away or dig the patch?\nOptions are 'walk away', 'dig'\n").lower()
            if opt == "walk away": print("You walk away, 'til the end of time.")
            elif opt == "dig": print("Congratulations! You've found the treasure.")
        elif opt == "2":
            opt= input("After a long journey you see a small village with 3 houses, what do you want to do?\nOptions are 'check the houses', 'gather molotof materials to burn the village', 'walk away'\n").lower()
            if opt == "check the houses": print("Villagers were not that kind to strangers, they decapitated you.")
            elif opt == "gather molotof materials to burn the village":
                opt= input("You need paper, flint and a glass bottle. Where do you want to find them?\nOptions are 'village', 'forest'\n").lower()
                if opt == "village": print("As you sneakily walk into the village, "
                                        "you notice that villagers are quite filthy and they have stuff thrown all over the place. "
                                        "You get lucky and find all the materials needed for molotoves, you throw them all, "
                                        "as the houses burn, you see a chest far away. You run to it hoping that it's the treasure you wanted all along"
                                        "but when you open the chest you realize that it wasn't your normal chest, it was a trapped one,"
                                        "you realize this when you a million glass shards cut deep into your body with an explosion. "
                                        "You question if all of this was worth it.")
                elif opt == "forest": print("While you walk into the woods, you start hearing strange noises, "
                                         "soon after a bunch of animals just charge onto you."
                                       "Pretty self explanatory what happened next.")
            elif opt == "walk away": print("You walk away, 'til the end of time.")
        elif opt == "3": print("You come across a bunch of lovely musicians playing their material only for them to enjoy,"
                     "you find a seat for yourself on their primitively made sitting logs, you listen and listen. "
                     "Then they ask you to play some of your material. As a non-musician you start to yell in the hopes of them thinking this was your opera, "
                     "you quickly realize how this was a huge mistake by being out of tone and not being able to manage your breath."
                     "After you stop yelling they make a few eyebrow movements to each other, they march onto you with their instruments, bashing you to death.")
if opt == "right": print("I'm exhausted of writing all this text, I'm here to code and I'm not here to tell a story, farewell.")
else: print("You're dead")

# print("welcome to the rollercoaster")
# h = int(input("What is your height in centimeters?"))
#  if h >= 160:
#   print("You can ride the rc!")
#  else:
#   print("Back off little boy.")


# print("welcome to odd or even")
#
# number = int(input("write a number"))
#
# a = number % 2
#
# if a == 0:
#  print("Even")
#
# else:
#  print("Odd")


# print("welcome to the rc")
#
# h = int(input("how tall are you?\n"))
# a = int(input("how old are you?\n"))
# m = int(input("how much money do you have?\n"))
# p = bool(input("do you want a photo? its 3$\nType anything for yes, nothing for no\n"))

# if h >= 160:
#     if a < 10:
#         if p == True:
#             if m < 8:print(f"money needed {8 - m}")
#             else:print(f"please pay 8$")
#         elif m < 5:print(f"money needed {5 - m}")
#         else:print("please pay 5$")
#     elif 10 =< a < 18:
#         if p == True:
#             if m < 13:print(f"money needed {13 - m}")
#             else:print(f"please pay 13$")
#         elif m < 10:print(f"money needed {10 - m}")
#         else:print("please pay 10$")
#     else:
#         if p == True:
#             if m < 23:print(f"money needed {23 - m}")
#             else:print(f"please pay 23$")
#         elif m < 20:print(f"money needed {20 - m}")
#         else:print("please pay 20$")
# else:print(f"sorry fam, you need to be at least {int(160-h)}cm taller")
#
# print(f"height:{h}\nage:{a}\nmoney{m}\nphoto:{p}")

# w=float(input("weight\n"))
# h=float(input("height\n"))
# bmi=float(round(w/h**2, 3))
#
# print(bmi)
# if bmi<18.5:
#  print("underweight")
# elif 18.5<=bmi<25:
#  print("normal weight")
# elif 25<=bmi<30:
#  print("overweight")
# elif 30<=bmi<35:
#  print("obese")
# else:
#  print("clinically obese")


# year=int(input("write the number you want to check \nnumber:"))
# div4=year%4
# div100=year%100
# div400=year%400
#
# if div4==0:
#     if div100==0:
#         if div400==0:
#             print(f"yup, {year} is a leap year")
#         else:
#             print(f"nah, {year} is not a leap year")
#     else:
#         print(f"yup, {year} is a leap year")
# else:
#     print(f"nah, {year} is not a leap")

# print("welcome to πzza")
#
# pizza_size=input("How big would you like your pizza? S/M/L\n")
# pepperoni=input("Would you like pepperoni on it? S:+$2/M:$3/L:$4\n Type Y or N\n")
# cheese_extra=input("Would you like extra cheese on it? S:$1/M:$1.5/L:$2\n Type Y or N\n")
#
# bill=float(0)
#
# if pizza_size == "S":
#     bill+=15
# elif pizza_size == "M":
#     bill+=20
# elif pizza_size == "L":
#     bill+=25
# if pepperoni == "Y":
#     if pizza_size == "S":
#         bill += 2
#     elif pizza_size == "M":
#         bill += 3
#     elif pizza_size == "L":
#         bill += 4
# if cheese_extra == "Y":
#     if pizza_size == "S":
#         bill += 1
#     elif pizza_size == "M":
#         bill += 1.5
#     elif pizza_size == "L":
#         bill += 2
# else: print("Incorrect pizza size")
# print(bill)
# if pizza_size == "L":
#     if pepperoni == "Y":
#         if cheese_extra == "Y":
#             print("have a feast mate")


# n1 = input("NAME1")
# n2 = input("NAME2")
# n3 = (n1 + n2).lower()
# score = n3.count("l") + n3.count("o") + n3.count("v") + n3.count("e") + n3.count("t") + n3.count("r") + n3.count("u") + n3.count("e")
# print(score) #For some reason I couldn't get .count to work properly, I might look at it again.