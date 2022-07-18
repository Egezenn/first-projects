# def calc_can_of_paint(dim1,dim2,canCoverage):
#     cans=dim1 * dim2 / canCoverage
#     isthenumberanint=cans - int(cans)
#     if isthenumberanint == 0:
#         print(f"You need {int(cans)} cans of paint.")
#     elif isthenumberanint != 0:
#         print(f"You need {int(cans)+1} cans of paint.")
#
# calc_can_of_paint(int(input("dim1:")), int(input("dim2:")), int(input("canCoverage:")))

# numbertodivide=int(input("don't type negative numbers\nnumber:"))
# primescore = 0
# for number in range(2, numbertodivide-1):
#     z = numbertodivide%number
#     if z == 0:
#         primescore -= 1
# if primescore == 0:
#     if numbertodivide == 0:
#         print("its not prime")
#     elif numbertodivide == 1:
#         print("its not prime")
#     else:
#         print("its prime")


# def prN():
#     print("that was not a prime")
#     exit()
# def prY():
#     print("that was a prime")
#     exit()
# def prime_checker(num):
#     prime_score = 0
#     if num == 0:
#         prN()
#     elif num == 1:
#         prN()
#     elif str(num)[0] == "-":
#         prN()
#     for numbers in range(2, num-1):
#         a = num%numbers
#         if a == 0:
#             prN()
#     prY()
#
# prime_checker(int(input("Number: ")))

# TODO USE DEFINED FUNCTIONS
#
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
CAPSalphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

end = False

while end == False:

    shifted_message = ""
    char_index_num = 0

    message = input("Type the message to be shifted: ")
    shift = int(input("shift(to unshift enter the negative value): "))

    for character in message:
        if character in alphabet:
            char_index_num = alphabet.index(character)
            char_new_index_num = char_index_num + shift
            while char_new_index_num > 25:
                char_new_index_num -= 26
            while char_new_index_num < 0:
                char_new_index_num += 25
            shifted_message += alphabet[char_new_index_num]

        elif character in CAPSalphabet:
            char_index_num = CAPSalphabet.index(character)
            char_new_index_num = char_index_num + shift
            while char_new_index_num > 25:
                char_new_index_num -= 26
            while char_new_index_num < 0:
                char_new_index_num += 25
            shifted_message += CAPSalphabet[char_new_index_num]

        else:
            shifted_message += character

    print(shifted_message)

    endinput = input("\nType 'quit' to quit or anything to continue: ")
    if endinput == "quit":
        end = True
        print(f"variable end is {end}, program will quit.")
