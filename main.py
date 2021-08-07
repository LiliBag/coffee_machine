# coffee machine game
import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_sufficiency(order_ingridients):
    for item in order_ingridients:
        if order_ingridients[item]>=resources[item]:
            print(f"sorry not enought {item}")
            return False
        else:
            return True

def processing_coins():
    #Returns total calculated coins inseted
    print("Please insert coins ")
    total=int(input("How many quarters"))*0.25
    total+=int(input("How many dimes"))*0.10
    total+=int(input("How many nickles"))*0.05
    total+=int(input("How many pennies"))*0.01
    return total

def transaction_success(received_coins, cost_of_coffee):
    #Returns true is payment is efficient, false if not enough money
    if received_coins>=cost_of_coffee:
        change=round(received_coins-cost_of_coffee,2)
        print(f"Here is your change: {change}")
        global profit_money
        profit_money +=cost_of_coffee
        return True
    else:
        print("There is not enough money")
        return False

def make_coffee(name_of_the_drink, order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {name_of_the_drink}☕️")


profit_money=0
on= True

while on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice=='off':
        sys.exit()
        is_on=False
    elif user_choice=="report":
        water=resources['water']
        milk=resources['milk']# one can also do this: milk=resources.get("milk")
        coffee=resources["coffee"]
        print(f"the water amount is {water}, the milk amount is {milk},the coffee amount is {coffee}, Money : {profit_money}")
    #elif user_choice in MENU:
    else:
        drink=MENU[user_choice]
        if resource_sufficiency(drink['ingredients']):
            payment= processing_coins()
            if transaction_success(payment, drink['cost']):
                make_coffee(user_choice, drink["ingredients"])


