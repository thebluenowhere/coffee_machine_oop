from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    my_coffee_machine = CoffeeMaker()
    my_money_machine = MoneyMachine()
    options = Menu()
    coffee_machine_on = True
    while coffee_machine_on:
        choice = input(f"What would you like? {options.get_items()}\n>>> ")
        if choice == "off":
            coffee_machine_on = False
        elif choice == "report":
            my_coffee_machine.report()
            my_money_machine.report()
        else:
            drink = options.find_drink(choice)
            if my_coffee_machine.is_resource_sufficient(drink):
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_machine.make_coffee(drink)
                else:
                    break
            else:
                break


if __name__ == "__main__":
    main()
