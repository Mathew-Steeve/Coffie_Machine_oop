from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_menu = Menu()
item = MenuItem("name", "Water", "milk", "coffee", "cost")
maker = CoffeeMaker()
money = MoneyMachine()
need = True
while need:
    choice = input(f"What would you like ? ({coffee_menu.get_items()}):")
    # drink.name = choice

    if choice == "report":
        maker.report()
        money.report()
    elif choice == "off":
        exit()
    else:
        A = coffee_menu.find_drink(choice)
        B = maker.is_resource_sufficient(A)
        if B is True:
            C = money.make_payment(cost=A.cost)
            if C is True:
                maker.make_coffee(A)
