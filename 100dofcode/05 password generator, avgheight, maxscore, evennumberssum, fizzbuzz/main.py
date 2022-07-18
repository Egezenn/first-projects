import random
print("Password generator v0.04")

pass_character_amount=int(input("amount of characters:"))+1
pass_symbol_amount=int(input("amount of symbols:"))+1
pass_number_amount=int(input("amount of numbers:"))+1

alphabetlist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
          "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbollist=['\"',"!","\'","^","+","%","&","/","(",")","=","?","_","<",">","£","#","$","{","[","]","}","@","€",
         "₺","~",".",",",":",";","\\"]
numberlist=["0","1","2","3","4","5","6","7","8","9"]

password=[]
reorderedpassword=[]
passwordfinal=""

for alength in range(1, pass_character_amount):
    alphabetrandom=alphabetlist[random.randint(0, 51)]
    password.append(alphabetrandom)

for slenghth in range(1, pass_symbol_amount):
    symbolrandom=symbollist[random.randint(0, 30)]
    password.append(symbolrandom)

for nlength in range(1, pass_number_amount):
    numberrandom=numberlist[random.randint(0, 9)]
    password.append(numberrandom)

for x in range(0, pass_character_amount+pass_symbol_amount+pass_number_amount-3):
    reorderedpassword.append(x)
    random.shuffle(reorderedpassword)

password = [password[f] for f in reorderedpassword]

for x in range(0, pass_character_amount+pass_symbol_amount+pass_number_amount-3):
    passwordfinal += password[x]

print(passwordfinal)

# for h in range(0, 3456):
#     a=random.choice(password)
#     if passstring.count(a) < 1:
#         passstring += a #lul


# student_heights = input("list of student heights\n").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#
# total_amount = 0
# for height in student_heights:
#     total_amount += 1
# print(total_amount)
#
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)
#
# print(round(sum(student_heights)/len(student_heights)))

# student_scores = input("Input a list of student heights ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# highest_score = 0
#
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(highest_score)

# n=int(input("number please\n"))//2
# print(n*(n+1))

# n=int(input("numb\n"))
# tot=0
# for number in range(0, n+1, 2):
#     tot += number
# print(tot)

# number_of_ticks = int(input("tick amount:"))
#
# for tick in range(1, number_of_ticks+1):
#     if tick %3 == 0:
#         if tick%5 == 0:
#             print("FizzBuzz")
#         elif tick%5 != 0:
#             print("Fizz")
#     elif tick %5 == 0:
#         if tick %3 != 0:
#             print("Buzz")
#     else: print(tick)
#
# for tick in range(1, number_of_ticks+1):
#     if tick%3 == 0 and tick%5==0:
#         print("FizzBuzz")
#     elif tick%3 == 0:
#         print("Fizz")
#     elif tick %5 == 0:
#         print("Buzz")
#     else: print(tick)
