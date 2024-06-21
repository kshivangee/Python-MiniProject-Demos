# This is a sample Python script.
CoffeeTypes = {
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

resources={
"water" : 300, #300ml
"milk" : 200, #200ml
"coffee" : 100, #100g
}
def printReport():
    print(f"Water={resources['water']}ml \nMilk={resources['milk']}ml \nCoffee={resources['coffee']}g")


def makeEspresso(money):

    if(resources['water']>=50):
        resources['water'] -= 50

    if (resources['coffee'] >= 18):
        resources['coffee'] -= 18

    change = round((money-1.50),2)
    if(money<1.50):
        print("Sorry that's not enough money. Money refunded.")
    elif(money>1.50):
        print(f"Here is {change} in change.")
        print("Here is your Espresso. Enjoy!")
    else:
        print("Here is your Espresso. Enjoy!")
def makeLatte(money):
    if (resources['water'] >= 200):
        resources['water'] -= 200

    if (resources['coffee'] >= 24):
        resources['coffee'] -= 24

    if (resources['milk'] >= 150):
        resources['milk'] -= 150

    change = round((money - 2.50),2)
    if (money < 2.50):
        print("Sorry that's not enough money. Money refunded.")
    elif (money > 2.50):
        print(f"Here is {change} in change.")
        print("Here is your Latte. Enjoy!")
    else:
        print("Here is your Latte. Enjoy!")

def makeCappucino(money):
    if (resources['water'] >= 250):
        resources['water'] -= 250

    if (resources['coffee'] >= 24):
        resources['coffee'] -= 24

    if (resources['milk'] >= 100):
        resources['milk'] -= 100

    change = round((money - 3.00),2)
    if (money < 3.00):
        print("Sorry that's not enough money. Money refunded.")
    elif (money > 3.00):
        print(f"Here is {change} in change.")
        print("Here is your Cappucino. Enjoy!")
    else:
        print("Here is your Cappucino. Enjoy!")


def resourcesSufficient(param):
    for items in param:
        if(param[items]>resources[items]):
            print(f"Sorry there is not enough {items}.")
            return False
        else:
            return True

def coffeemachine():
    machine='on'
    while(machine=='on'):
        option = input("What would you like? (espresso/latte/cappuccino): ").lower()
        drink = CoffeeTypes[option]
        if(resourcesSufficient(drink["ingredients"])):
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))
            money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
            print(f"Money Given:{money}")

            if(option=='report'):
                printReport()
            if(option=='espresso'):
                makeEspresso(money)
            if(option=='latte'):
                makeLatte(money)
            if(option=='cappucino'):
                makeCappucino(money)

        machine = input("Do you want to continue?(if yes then press 'on' and if no press 'off': ")

coffeemachine()


