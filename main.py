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
    "money": 0
}


def payment(coins):
    """Returns the total calculated from coins inserted."""
    quarters = float(input("How many quarters?: ")) * 0.25
    coins["quarters"] = quarters
    dimes = float(input("How many dimes?: ")) * 0.10
    coins["dimes"] = dimes
    nickles = float(input("How many nickles?: ")) * 0.05
    coins["nickles"] = nickles
    pennies = float(input("How many pennies?: ")) * 0.01
    coins["pennies"] = pennies
    return coins


# def sufficient_resource():
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in
def purchase(coins):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if sum(coins.values()) >= MENU[user_selection]["cost"]:
        print("You've got enough")
        can_purchase = True
        global profit
        profit += MENU[user_selection]["cost"]
    elif sum(coins.values()) < MENU[user_selection]["cost"]:
        print("Sorry, not enough money. Money refunded.")
        can_purchase = False
    else:
        can_purchase = False
        print("Unexpected error occurred... Returning money.")
    return can_purchase


def make_drink(drink):
    """Deduct the required ingredients from the resources."""
    if "milk" in MENU[drink]:
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    return resources


is_running = True
coins = {}
profit = 0

while is_running:
    user_selection = input("What would you like? (espresso/latte/cappuccino): ")
    if user_selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif user_selection == "off":
        is_running = False
    else:
        coins_in = payment(coins)
        resources["money"] += sum(coins_in.values())
        sufficient_payment = purchase(coins_in)
        if sufficient_payment:
            make_drink(user_selection)
            print(f"Here is your {user_selection} ☕. Enjoy!")
            if sum(coins_in.values()) > MENU[user_selection]['cost']:
                change = round(sum(coins_in.values()) - (MENU[user_selection]["cost"]), 2)
                print(f"Here's your change: ${change}")
        elif not sufficient_payment:
            print("Problem with purchase. Returning money.")
