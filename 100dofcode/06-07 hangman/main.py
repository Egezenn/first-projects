# import random
# words=["boop","leap","yooooooooo","death"]
# selectedword=random.choice(words)
#
# hiddentext=""
# selectedword_amount_of_char=len(selectedword)
#
# for hide in range (selectedword_amount_of_char):
#     hiddentext += "_ "
# print(hiddentext)
#
# uinputlist=""
# uinput=input("word").lower()
# uinputlist += uinput
#
# hangmanstate=0
# #need a way to change the string
# amount_of_hidden_text_reveal=selectedword.count(uinput)
# if amount_of_hidden_text_reveal > 0:
#     print(f"you've guessed right!\n"
#           f"tho I don't have a way to show you what you've guessed correct")
# elif amount_of_hidden_text_reveal == 0:
#     hangmanstate +=1
#     print(f"you've guessed wrong\n{hangmanstate}")
#     if hangmanstate == 6:
#         print(f"you've lost, the word was {selectedword}")

# import random
# word_list = ["hell","bazooka","kangaroo"]
# word = random.choice(word_list)
#
# user_guess=input("please guess a word").lower()
#
# for letters in word:
#     if letters==user_guess:
#         print("Right")
#     elif letters!=user_guess:
#         print("Wrong")

# import random
#
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
#
# hidden_word=[]
# solution=[]
# for characters in chosen_word:
#     solution += characters
# for letters in range(len(chosen_word)):
#     hidden_word += "_"
#
# print(hidden_word)
# print(solution)       #the display somehow adds one _ to every list, dk why couldn't debug
#
# guess = input("Guess a letter: ").lower()
#
# del hidden_word[0:len(chosen_word)-1]
# for letter in chosen_word:
#     if letter == guess:
#         hidden_word.append(letter)
#     elif letter != guess:
#         hidden_word.append("_")
#     else: del hidden_word
# print(hidden_word)
word_list = [
'abruptly',
'absurd',
'abyss',
'affix',
'askew',
'avenue',
'awkward',
'axiom',
'azure',
'bagpipes',
'bandwagon',
'banjo',
'bayou',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'dwarves',
'embezzle',
'equip',
'espionage',
'euouae',
'exodus',
'faking',
'fishhook',
'fixable',
'fjord',
'flapjack',
'flopping',
'fluffiness',
'flyby',
'foxglove',
'frazzled',
'frizzled',
'fuchsia',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jockey',
'jogging',
'joking',
'jovial',
'joyful',
'juicy',
'jukebox',
'jumbo',
'kayak',
'kazoo',
'keyhole',
'khaki',
'kilobyte',
'kiosk',
'kitsch',
'kiwifruit',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'lymph',
'marquis',
'matrix',
'megahertz',
'microwave',
'mnemonic',
'mystify',
'naphtha',
'nightclub',
'nowadays',
'numbskull',
'nymph',
'onyx',
'ovary',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'triphthong',
'twelfth',
'twelfths',
'unknown',
'unworthy',
'unzip',
'uptown',
'vaporize',
'vixen',
'vodka',
'voodoo',
'vortex',
'voyeurism',
'walkway',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie',
]
import random

print("Welcome to hangman!")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
chosen_word_list = []
guesslist = []
hangmanstate = 6

for _ in range(word_length):
    display += "_"
print(display)
for letters in chosen_word:
    chosen_word_list += letters

while display != chosen_word_list and hangmanstate !=0:
    guess = input("\nGuess a letter: ").lower()
    guesslist += guess
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word_list:
        hangmanstate -= 1
    print(f"\n{display}")
    print(f"You have {hangmanstate} lives left\nYou've guessed {guesslist}")
    if hangmanstate == 0:
        print("You've lost!")
        print(f"The word was {chosen_word}")
    elif display == chosen_word_list:
        print("You've won!")
        print(f"The word was {chosen_word}")
