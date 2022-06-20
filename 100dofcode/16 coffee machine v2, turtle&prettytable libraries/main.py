# from turtle import *
#
# jimmy = Turtle()
# jimmy.shape("turtle")
# print(jimmy)
# while 1 == 1:
#     jimmy.color("pink")
#     jimmy.position()
#     jimmy.forward(300)
#     jimmy.color("blue")
#     jimmy.right(182)
#     jimmy.forward(300)
#
# das_screen = Screen()
# print(das_screen.canvheight)
# das_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("PokeMAN", ["Pika", "seadude", "firemanguy"])
# table.add_column("typo", ["elektrix", "wo ah", "fi ah"])
# table.align = "r"
#
# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine = "on"
while machine == "on":
    coffee_maker.report()
    options = menu.get_items()
    wanted_drink = input(f"\nWhat would you like ({options}): ")

    drink = menu.find_drink(wanted_drink)

    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

    machine = input("Continue? y or n: ")
    if machine == "n":
        machine = "off"
    else:
        machine = "on"
    print()

money_machine.report()
