# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
#
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
#
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
#
# age = int(input("How old are you? "))
# if age >= 18:
#     print(f"You can drive at age {age}.")
# elif age < 18:
#     print(f"You can't drive at the age of {age}")
#
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
#
# def mutate(a_list):
#   b_list = []
#   for items in a_list:
#     new_item = items * 2
#     b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])
#
# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")
#
# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)
