print("Welcome to the tip calculator")
bill = input("Bill:₺")
tip_percentage = input("Tip percentage:")
amount_of_people = input("Amount of people:")

tip = (int(tip_percentage) + int(100))/100
print(f"Your tip percentage is {(float(tip)*100)-100}%!")

bill_with_tip = float(bill)*float(tip)
print(f"Your bill with tip is {round(bill_with_tip, 3)}₺!")

bill_per_person = float(bill_with_tip)/int(amount_of_people)
print(f"Each person will pay {round(bill_per_person, 3)}₺!")


#   a = input("write a two digit number\n")
#   b = int(a[0])
#   c = int(a[1])
#   res = b - c
#   print(res)


# weight = input("your weight please\n")
# height = input("your height please\n")
# BMI = float(weight) / float(height)**2
# BMI_int = int(BMI)
# print(BMI_int, BMI)
