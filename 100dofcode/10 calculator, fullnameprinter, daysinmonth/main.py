def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def basicmath(numb1, operation, numb2):
    if operation == "+":
        return add(numb1, numb2)
    elif operation == "-":
        return subtract(numb1, numb2)
    elif operation == "*":
        return multiply(numb1, numb2)
    elif operation == "/":
        return divide(numb1, numb2)
    else:
        return ("Incorrect operation")


exitchoice = False
calcsdone = 0
Result = 0
continousResult = 0

print("Welcome to the calculator!")
while exitchoice == False:
    if calcsdone == 0:
        num1 = float(input("1: "))
        Soperation = input("+ or - or * or / ?: ")
        num2 = float(input("2: "))
        continousResult = basicmath(num1, Soperation, num2)
        if continousResult == "Incorrect operation":
            print("Incorrect operation")
            exit()
        calcsdone += 1
        print(continousResult)

        exitstate = input("Continue with this number? y or n\n").lower()
        if exitstate == "n":
            Result = continousResult
            exitchoice = True
        elif exitstate == "y":
            exitchoice = False
        else:
            print("Invalid input")
            exit()

    elif calcsdone > 0:
        print(f"\n1: {continousResult}")
        Soperation = input("+ or - or * or / ?: ")
        num2 = float(input("2: "))
        continousResult = basicmath(continousResult, Soperation, num2)
        if continousResult == "Incorrect operation":
            print("Incorrect operation")
            exit()
        print(continousResult)

        exitstate = input("Continue? y or n\n").lower()
        if exitstate == "n":
            Result = continousResult
            exitchoice = True
        elif exitstate == "y":
            exitchoice = False
        else:
            print("Invalid input")
            exit()

# def full_name(f_name, l_name):
#     if f_name == "":
#         if l_name == "":
#             return "Empty last and first name"
#         return "Empty first name"
#     elif l_name == "":
#         return "Empty last name"
#     else:
#         return f"{f_name.title()} {l_name.title()}"
#
# name = full_name(input("first name: "), input("last_name: "))
# print(name)

# def is_leap(year):
#     """Checks an year if it's leap or not and returns True False data."""
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             return False
#         return True
#     return False
#
#
# def days_in_month(year, month):
#     """"Returns how many days are in a month, requesting year and month."""
#     if month>12 or month < 1:
#         return "Non existent month"
#     else:
#         if is_leap(year) == True and month == 2:
#             return 29
#         else: month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#         return month_days[month-1]
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
#
# print(days)
