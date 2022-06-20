# TODO for later on maybe:
#   extend the code of take_coins()
#   if the money user gave is higher than the cost of beverages after the transaction don't ask for coin input.
#   resources["money"] should be the profit, not inserted coins
#   USE LOOPS

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 700,
    "milk": 400,
    "coffee": 100,
    "money": 0
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}gr")
    print(f"Money: ${resources['money']}")
#    #TODO   USE LOOPS


def report_beverage(beverage):
    print(f"Water: {MENU[beverage[1:]]['ingredients']['water']}ml")
    print(f"Milk: {MENU[beverage[1:]]['ingredients']['milk']}ml")
    print(f"Coffee {MENU[beverage[1:]]['ingredients']['coffee']}gr")
#    #TODO   USE LOOPS


def take_coins(resourcelist, coinvalues):
    """resources, coins"""
    resourcelist['money'] += int(input("Pennies: ")) * coinvalues["penny"]
    resourcelist['money'] += int(input("Nickels: ")) * coinvalues["nickel"]
    resourcelist['money'] += int(input("Dimes: ")) * coinvalues["dime"]
    resourcelist['money'] += int(input("Quarters: ")) * coinvalues["quarter"]
    resourcelist['money'] = round(resourcelist['money'], 2)
    print(f"${resourcelist['money']}")
#    #TODO   USE LOOPS


def resource_sufficiency(wanted_beverage, menu, resourcelist):
    """beverage_taken, menu, resources"""
    if resourcelist['water'] < menu[wanted_beverage]['ingredients']['water']:
        return "Insufficient water"
    elif resourcelist['milk'] < menu[wanted_beverage]['ingredients']['milk']:
        return "Insufficient milk"
    elif resourcelist['coffee'] < menu[wanted_beverage]['ingredients']['coffee']:
        return "Insufficient coffee"
    elif resourcelist['money'] < menu[wanted_beverage]['cost']:
        return "Insufficient money"
    else:
        return "All is good"
#    #TODO   USE LOOPS


def coffee_machine():
    wanted_beverage = input("\nEspresso, latte, cappucino?"
                            "\n   Add 'r' in front of the beverage if you want to see the ingredients needed for it"
                            "\n   Type 'report' to see machines resources"
                            "\n     ").lower()
    if wanted_beverage == "report":
        report()

    elif wanted_beverage == "respresso" or wanted_beverage == "rlatte" or wanted_beverage == "rcappucino":
        report_beverage(wanted_beverage)

    else:
        take_coins(resources, coins)
        sufficiency = resource_sufficiency(wanted_beverage, MENU, resources)
        print(sufficiency)
        if sufficiency == "All is good":
            change = resources['money'] - MENU[wanted_beverage]['cost']
            resources['water'] = resources['water'] - MENU[wanted_beverage]['ingredients']['water']
            resources['milk'] = resources['milk'] - MENU[wanted_beverage]['ingredients']['milk']
            resources['coffee'] = resources['coffee'] - MENU[wanted_beverage]['ingredients']['coffee']
            print(f"Here is your ${change} and your {wanted_beverage} is ready!")
            resources['money'] = 0
#        #TODO   USE LOOPS


transaction_complete = False
while not transaction_complete:
    coffee_machina()
    after_transaction = input("\nIs that all? y or n\n").lower()
    if after_transaction == "y":
        transaction_complete = True

