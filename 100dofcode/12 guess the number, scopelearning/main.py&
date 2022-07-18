# def emotional_damage():
#     global hp
#     hp =- 10
#
# def game():
#     global hp
#     hp += 100
#
# hp = 0
# emotional_damage()
# game()
# print(hp)

# def emotional_damage():
#     return hp - 10
#
# def game():
#     return hp + 100
#
# hp = 0
# hp = game()
# hp = emotional_damage()
# print(hp)

import random
da_number = random.randint(1, 100)
print("Guess da number\nI thought of a number between 1 and 100.")


def hardness_selection():
    hardness = input("Easy or hard?\n").lower()
    if hardness == "easy":
        print("okay cry baby")
        return 10
    elif hardness == "hard":
        print("okay tough guy")
        return 5


def take_a_guess():
    return int(input("\nGuess! "))


def gamestate(guess, da_number, lives):
    while guess != da_number:
        lives = lives - 1
        if guess == da_number:
            print("You won!")
            exit()
        if lives == 0:
            print("You lost!")
            exit()
        if guess > da_number:
            print(f"That was high, lives left: {lives}")
        elif guess < da_number:
            print(f"That was low, lives left: {lives}")
        guess = take_a_guess()


def game():
    lives = hardness_selection()
    guess = take_a_guess()
    gamestate(guess, da_number, lives)


game()
